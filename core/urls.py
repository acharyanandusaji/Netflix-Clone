from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import Home
from .views import ProfileList,ProfileCreate

app_name = 'core'

urlpatterns = [
    path('', Home.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/',ProfileCreate.as_view(), name='profile_create')

]
