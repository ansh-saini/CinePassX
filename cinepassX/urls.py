from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', main_views.home, name = 'home'), 
    path('dashboard/', main_views.dashboard, name = 'dashboard'),    
    path('payment/', main_views.payment, name = 'payment'),
    path('register/', main_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name = 'logout'),
    path('success/', main_views.payment_success, name = 'payment_success'),
    path('failure/', main_views.payment_failure, name = 'payment_failure'),
    path('book/', main_views.book, name = 'book-show'),
    path('mail-subscribe/', main_views.mail_subscribe, name = 'mail-subscribe'),
    path('movie/<tag>', main_views.movie_detail, name = 'movie-detail'),
    path('terms/', main_views.terms, name = 'terms'),
    path('contact/', main_views.contact_us, name = 'contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)