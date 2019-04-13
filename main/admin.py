from django.contrib import admin
from .models import Profile, Movie, Show, MailSubscriber


admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(MailSubscriber)

