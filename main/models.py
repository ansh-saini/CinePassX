from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_imgur.storage import ImgurStorage
import datetime

STORAGE = ImgurStorage()

class Movie(models.Model):
	title = models.CharField(max_length=50, blank=True)
	tag = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return f'{self.tag} ~ {self.title}'


class Show(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	date = models.DateField(blank=False)
	time = models.TimeField(blank=False)

	def __str__(self):
		return f'{self.movie.title} at {self. time}'

class Booked(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE) 

	def __str__(self):
		return f'{user} booked {show}'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=10, blank=False)
	subscribed = models.BooleanField(default=False, blank=True)
	sub_date = models.DateTimeField(default=datetime.datetime.now())
	booked_show = models.BooleanField(default=False, blank=True)
	book_counter = models.IntegerField(default=0)
	plan = models.IntegerField(default=0)
	friend = models.ManyToManyField(User, related_name='mates', blank=True)
	# mail_subscribed = models.BooleanField(default=False, blank=True)
	# show = models.OneToOneField(Show, on_delete=models.SET_DEFAULT, default=None)
	# location = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.user.username

class MailSubscriber(models.Model):
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.email


#Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		print("uwuwwuwu")
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print("owowowowo")
	instance.profile.save()