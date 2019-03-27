from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
	title = models.CharField(max_length=50, blank=False)
	tag = models.CharField(max_length=50, blank=False)
	language = models.CharField(max_length=10, blank=False)

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
	# show = models.OneToOneField(Show, on_delete=models.SET_DEFAULT, default=None)
	# location = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.user.username

#Signals
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
	# instance.profile.save()