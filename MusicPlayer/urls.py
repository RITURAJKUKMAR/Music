from django.urls import path
from MusicPlayer.views import *
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
from django.conf import settings



app_name = "MusicPlayer"

urlpatterns = [
    path("", welcome, name="welcome"),
    path("registration", registration, name="registration"),
    path("registered", registered, name="registered"),
    path("login", login, name="login"),
    path("home", home, name="home"),
    path("profile", profile, name="profile"),
    path("editProfile", editProfile, name="editProfile"),
    path("musicUpload", musicUpload, name="musicUpload"),
    path("musicDelete", musicDelete, name="musicDelete"),
    path("logout", logout, name="logout"),
]
