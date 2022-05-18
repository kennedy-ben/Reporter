from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from flag.views import PersonViewSet, SpeciesViewSet
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns=[
    # path('', views.home, name='home'),
    # path('', views.login, name='login'),
    # path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),   
    # path('', include(router.urls)),


    path('',views.index,name = 'index'),
    path('new/post', views.new_post, name='newpost'),
    path('hoods', views.all_hoods, name='hoods'),
    path('business/',views.create_business,name = 'business'),
    path('profile/', views.profile, name='profile'),
    path('createHood/', views.createHood, name='createHood'),
    path('update/profile', views.updateprofile, name='updateprofile'),
    path('index/', views.join, name='index'),
    path('search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)