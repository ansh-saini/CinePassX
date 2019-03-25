from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from main import views as main_views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('home/', main_views.payment, name = 'home'),
    path('register/', main_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name = 'logout'),
    path('success/', main_views.payment_success, name = 'payment_success'),
    path('failure/', main_views.payment_failure, name = 'payment_failure'),
]
