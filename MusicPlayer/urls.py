from django.urls import path
from MusicPlayer.views import *
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


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
