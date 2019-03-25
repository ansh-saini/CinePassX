from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
import logging, traceback
from . import CONSTANTS as constants
from . import CONFIG as config
import hashlib
import requests
from random import randint
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Created!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


def payment(request):   
	data = {}
	txnid = get_transaction_id()
	hash_ = generate_hash(request, txnid)
	print(hash_)
	hash_string = get_hash_string(request, txnid)
	print(hash_string)
	# use constants file to store constant values.
	# use test URL for testing
	data['action'] = constants.PAYMENT_URL_TEST 
	data['amount'] = float(constants.PAID_FEE_AMOUNT)
	data['productinfo']  = constants.PAID_FEE_PRODUCT_INFO
	data['key'] = config.KEY
	data['txnid'] = txnid
	data['hash'] = hash_
	data['hash_string'] = hash_string
	data['first_name'] = request.user.first_name
	data['email'] = request.user.email
	data['phone'] = request.user.profile.phone
	data['service_provider'] = constants.SERVICE_PROVIDER
	data['furl'] = request.build_absolute_uri(reverse('payment_failure'))
	data['surl'] = request.build_absolute_uri(reverse('payment_success'))
	
	return render(request, 'main/payment_form.html', data)        
	
# generate the hash
def generate_hash(request, txnid):
	try:
		# get keys and SALT from dashboard once account is created.
		# hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
		hash_string = get_hash_string(request, txnid)
		generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
		return generated_hash
	except Exception as e:
		print("owowowo")
		# log the error here.
		logging.getLogger('error_logger').error(traceback.format_exc())
		return None

# create hash string using all the fields
def get_hash_string(request, txnid):
	user = request.user
	hash_string = config.KEY+"|"+txnid+"|"+str(float(constants.PAID_FEE_AMOUNT))+"|"+constants.PAID_FEE_PRODUCT_INFO+"|"
	hash_string += request.user.first_name+"|"+request.user.email+"|"
	hash_string += "||||||||||"+config.SALT

	return hash_string

# generate a random transaction Id.
def get_transaction_id():
	hash_object = hashlib.sha256(str(randint(0,9999)).encode('utf-8'))
	# take approprite length
	txnid = hash_object.hexdigest().lower()[0:32]
	return txnid

# no csrf token require to go to Success page. 
# This page displays the success/confirmation message to user indicating the completion of transaction.
@csrf_exempt
def payment_success(request):
	print(request.__dict__)
	return render(request, 'main/payment_success.html')

# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
	# print(request.data)
	return render(request, 'main/payment_failure.html')


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

	
