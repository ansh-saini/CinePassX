from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Movie(models.Model):
	title = models.CharField(max_length=50, blank=False)
	tag = models.CharField(max_length=50, blank=False)
	image = models.ImageField(default='default.jpg', upload_to='movie_thumbnails')
	LANGUAGE_CHOICES = (
		('hindi', 'Hindi'),
		('english', 'English'),
	)
	language = models.CharField(max_length=10, blank=True, choices=LANGUAGE_CHOICES)
	DIMENSION_CHOICES = (
		('2d', '2D'),
		('3d', '3D'),
	)
	dimension = models.CharField(max_length=2, default='2d', blank=False, choices=DIMENSION_CHOICES)
	rating = models.IntegerField(null=True, blank=True)
	link = models.CharField(null=True, max_length=50, blank=True)
	
	
	def __str__(self):
		return self.title


class Show(models.Model):
	movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
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
	booked_show = models.BooleanField(default=False, blank=True)
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