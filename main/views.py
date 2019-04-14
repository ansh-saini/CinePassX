from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import logging, traceback
import hashlib
import requests
import json
import datetime
from random import randint
from .forms import UserRegisterForm, BookForm, MailSubscriberForm, FriendForm
from .models import Show, MailSubscriber, Movie
from . import CONSTANTS as constants
from . import CONFIG as config

@login_required
def book(request, tag):
	if request.user.profile.subscribed:
		if request.user.profile.booked_show:
			messages.error(request, f'You have already booked a show today!')
			return redirect('home')
		else:
			print("ELSE")
			if request.method == 'POST':	
				# date = datetime.datetime.now()
				# formated_date = date.strftime("%Y-%m-%d")
				# shows = Show.objects.filter(date=formated_date)
				form = BookForm(tag, request.POST)
				try:
					data = dict(request.POST)['shows'][0]
					print(data)
					book_show = Show.objects.get(id=data)
					# request.user.profile.booked_show = True
					request.user.profile.book_counter += 1
					request.user.profile.save()
					messages.success(request, f'Your Show [{book_show}] has been Boooked!')
					return render(request, 'main/book_success.html')
				except Exception as e:
					return render(request, 'main/book_failure.html')
			else:

				form = BookForm(tag)
			return render(request, 'main/book.html', {'form': form})
	else:
		messages.error(request, 'Please <a href="/payment">Click Here</a> to buy a Subscription First!', extra_tags='safe')
		return redirect('home')


@login_required
def movie_detail(request, tag):
	date = datetime.datetime.now()
	formated_date = date.strftime("%Y-%m-%d")
	data = get_movie_detail(tag)
	return render(request, 'main/movie-detail.html', {'data': data})
		

@login_required
def dashboard(request):
	date = datetime.datetime.now()
	formated_date = date.strftime("%Y-%m-%d")
	shows = Show.objects.filter(date=formated_date)
	# shows = Show.objects.all()
	print(shows)
	return render(request, 'main/dashboard.html', {'shows': shows, 'date': formated_date})

def home(request):
	shows = []
	data = []
	home = True
	form = MailSubscriberForm()
	# date = datetime.datetime.now()
	# formated_date = date.strftime("%Y-%m-%d")

	# show_ids = Show.objects.order_by().values('movie').distinct()
	# for x in list(show_ids):
	# 	show = Show.objects.get(id=x['movie'])
	# 	shows.append(show)

	# for show in shows:
	# 	data.append(get_movie_detail(show.movie.tag))
	movies = Movie.objects.all()
	for movie in movies:
		data.append(get_movie_detail(movie.tag))
		
	return render(request, 'main/index.html', {'home': home, 'form': form, 'data': data})



@login_required
def add_friend(request):
	if request.user.profile.subscribed:
		if request.method == 'POST':
			form = FriendForm(request.POST)
			friend_username = form.data['username']
			try:
				friend = User.objects.get(username=friend_username)
			except Exception as e:
				friend = None
				messages.error(request, f'User Not Found!')
			if friend:
				print(list(request.user.profile.friend.all()))
				if friend in list(request.user.profile.friend.all()):
					messages.success(request, f'{friend.username} is already your friend!')
				else:
					request.user.profile.friend.add(friend)
					messages.success(request, f'{friend.username} is now your friend!')
		else:
			form = FriendForm()
	else:
		messages.error(request, f'Please buy a subscription first!')
		# return redirect('home')
	return render(request, 'main/friends.html', {'form': form})

@csrf_exempt
def mail_subscribe(request):
	if request.method == 'POST':
		form = MailSubscriberForm(request.POST)
		if form.is_valid():
			MailSubscriber.objects.create(email=form.cleaned_data.get('email'))
			messages.success(request, f'You are now subscribed to our emails!')
		else:
			form = MailSubscriberForm()
	return redirect('home')

def get_movie_detail(tag):
	apikey = '25890e89'
	url = "http://www.omdbapi.com/"
	params = {'i': tag, 'apikey': apikey} 
	r = requests.get(url=url, params=params) 
	data = r.json()
	return data




def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			phone = form.cleaned_data.get('phone')
			username = form.cleaned_data.get('username')
			print(phone)
			print(username)
			form.save()
			user = User.objects.get(username=username)
			user.profile.phone = phone
			user.profile.save()
			print(user)
			messages.success(request, f'Your Account has been Created!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'main/register.html', {'form': form})


@login_required
def payment(request):   
	data = {}
	plan = dict(request.POST)['plan'][0]
	if plan == 'plan1':
		data['amount'] = float(249)
		data['productinfo'] = 'One month CinePassX Subscription'
	elif plan == 'plan2':
		data['amount'] = float(899)
		data['productinfo'] = 'Three month CinePassX Subscription'
	elif plan == 'plan3':
		data['amount'] = float(699)
		data['productinfo'] = 'Three month CinePassX Subscription'
	amount = data['amount']
	info = data['productinfo']
	txnid = get_transaction_id()
	hash_ = generate_hash(request, txnid, amount, info)
	print(hash_)
	hash_string = get_hash_string(request, txnid, amount, info)
	print(hash_string)
	data['action'] = constants.PAYMENT_URL_TEST 
	
	# data['amount'] = float(constants.PAID_FEE_AMOUNT)
	# data['productinfo']  = constants.PAID_FEE_PRODUCT_INFO
	data['key'] = config.KEY
	data['txnid'] = txnid
	data['hash'] = hash_
	data['hash_string'] = hash_string
	data['first_name'] = request.user.first_name
	data['email'] = request.user.email
	data['phone'] = request.user.profile.phone
	data['service_provider'] = constants.SERVICE_PROVIDER
	data['furl'] = request.build_absolute_uri(reverse('payment_failure'))
	data['surl'] = request.build_absolute_uri(reverse('payment_success', args=([request.user.username])))
	print(data['surl'])
	print(data['furl'])
	
	return render(request, 'main/payment_form.html', data)        
	
# generate the hash
def generate_hash(request, txnid, amount, info):
	try:
		# get keys and SALT from dashboard once account is created.
		# hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
		hash_string = get_hash_string(request, txnid, amount, info)
		generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
		return generated_hash
	except Exception as e:
		# log the error here.
		logging.getLogger('error_logger').error(traceback.format_exc())
		return None

# create hash string using all the fields
def get_hash_string(request, txnid, amount, info):
	hash_string = config.KEY+"|"+txnid+"|"+str(amount)+"|"+info+"|"
	hash_string += request.user.first_name+"|"+request.user.email+"|"
	hash_string += "||||||||||"+config.SALT
	return hash_string

# generate a random transaction Id.
def get_transaction_id():
	hash_object = hashlib.sha256(str(randint(0,9999)).encode('utf-8'))
	txnid = hash_object.hexdigest().lower()[0:32]
	return txnid

@csrf_exempt
def payment_success(request, user):
	user = User.objects.get(username=user)
	r = request.POST.dict()
	if user.first_name == r['firstname']:
		

		plan = 0
		# hashSequence = salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key
		hashSequence = config.SALT + '|' + r['status'] + '||||||' + r['udf5'] + '|' + r['udf4'] + '|' + r['udf3'] + '|' + r['udf2'] + '|' + r['udf1'] + '|' + r['email'] + '|' + r['firstname'] + '|' + r['productinfo'] + '|' + r['amount'] + '|' + r['txnid'] + '|' + config.KEY
		print(hashSequence)
		generated_hash = hashlib.sha512(hashSequence.encode('utf-8')).hexdigest().lower()
		if generated_hash == r['hash']:
			print(r['amount'])
			if r['amount'] == '249.00':
				plan = 1
			elif r['amount'] == '899.00':
				plan = 2
			elif r['amount'] == '699.00':
				plan = 3
			print(plan)
			user.profile.plan = plan
			user.profile.subscribed = True
			user.profile.sub_date = datetime.datetime.now()
			user.profile.save()
			print(user.profile.plan)
			data = {'status': r['status'],
					'txnid': r['txnid'],
					'amount': r['amount'],
			}
			return render(request, 'main/payment_success.html', data)
		else:
			return render(request, 'main/payment_failure.html')
	else:
		print("fuck")
		return redirect('home')

@csrf_exempt
def payment_failure(request):
	return render(request, 'main/payment_failure.html')

def terms(request):
	return render(request, 'main/terms.html')

def contact_us(request):
	return render(request, 'main/contact-us.html')

def error_404_view(request, exception):
	return render(request,'main/404.html')


# def home(request):
# 	MERCHANT_KEY = ""
# 	key=""
# 	SALT = ""
# 	PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
# 	action = ''
# 	posted={}
# 	# Merchant Key and Salt provided y the PayU.
# 	for i in request.POST:
# 		posted[i]=request.POST[i]
# 	hash_object = hashlib.sha256(b'randint(0,20)')
# 	txnid=hash_object.hexdigest()[0:20]
# 	hashh = ''
# 	posted['txnid']=txnid
# 	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
# 	posted['key']=key
# 	hash_string=''
# 	hashVarsSeq=hashSequence.split('|')
# 	for i in hashVarsSeq:
# 		try:
# 			hash_string+=str(posted[i])
# 		except Exception:
# 			hash_string+=''
# 		hash_string+='|'
# 	hash_string+=SALT
# 	hashh=hashlib.sha512(hash_string).hexdigest().lower()
# 	action =PAYU_BASE_URL
# 	if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
# 		return render_to_response('main/current_datetime.html',RequestContext(request,{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://test.payu.in/_payment" }))
# 	else:
# 		return render_to_response('main/current_datetime.html',RequestContext(request,{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." }))


# def success(request):
# 	c = {}
# 	c.update(csrf(request))
# 	status=request.POST["status"]
# 	firstname=request.POST["firstname"]
# 	amount=request.POST["amount"]
# 	txnid=request.POST["txnid"]
# 	posted_hash=request.POST["hash"]
# 	key=request.POST["key"]
# 	productinfo=request.POST["productinfo"]
# 	email=request.POST["email"]
# 	salt="GQs7yium"
# 	try:
# 		additionalCharges=request.POST["additionalCharges"]
# 		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
# 	except Exception:
# 		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
# 	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
# 	if(hashh !=posted_hash):
# 		print("Invalid Transaction. Please try again")
# 	else:
# 		print("Thank You. Your order status is " + status)
# 		print("Your Transaction ID for this transaction is " + txnid)
# 		print("We have received a payment of Rs. " + amount + ". Your order will soon be shipped.")
# 	return render_to_response('sucess.html',RequestContext(request,{"txnid":txnid,"status":status,"amount":amount}))



# def failure(request):
# 	c = {}
# 	c.update(csrf(request))
# 	status=request.POST["status"]
# 	firstname=request.POST["firstname"]
# 	amount=request.POST["amount"]
# 	txnid=request.POST["txnid"]
# 	posted_hash=request.POST["hash"]
# 	key=request.POST["key"]
# 	productinfo=request.POST["productinfo"]
# 	email=request.POST["email"]
# 	salt=""
# 	try:
# 		additionalCharges=request.POST["additionalCharges"]
# 		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
# 	except Exception:
# 		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
# 	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
# 	if(hashh !=posted_hash):
# 		print("Invalid Transaction. Please try again")
# 	else:
# 		print("Thank You. Your order status is " + status)
# 		print("Your Transaction ID for this transaction is " + txnid)
# 		print("We have received a payment of Rs. " + amount + ". Your order will soon be shipped.")
# 	return render_to_response("Failure.html",RequestContext(request,c))

	
