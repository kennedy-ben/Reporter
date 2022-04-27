from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns=[
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    
]

