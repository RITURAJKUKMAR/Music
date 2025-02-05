from django.shortcuts import render
from django.http import HttpResponseRedirect
from MusicPlayer.models import *
import random


def welcome(request):
    res = render(request, "welcome.html")
    return res


def registration(request):
    res = render(request, "registration.html")
    return res


def registered(request):
    if request.method == "POST":
        username = request.POST["username"]
        if len(User.objects.filter(Username=username)):
            userStatus = 1
        else:
            user = User()
            user.Username = request.POST["username"]
            user.password = request.POST["password"]
            user.name = request.POST["name"]
            user.mobile = request.POST["mobile"]
            user.email = request.POST["email"]
            user.save()
            userStatus = 2
    else:
        userStatus = 3
    context = {"userStatus": userStatus}
    res = render(request, "registered.html", context)
    return res


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.filter(Username=username, password=password)
        if len(user) == 0:
            loginErroe = "Invalid Username of Password"
            res = render(request, "login.html", {"loginErroe": loginErroe})
        else:
            request.session["username"] = user[0].Username
            request.session["name"] = user[0].name
            request.session["firstLetter"] = (user[0].name)[0]
            musics = list(Musics.objects.all())
            hindiSongs = list(Musics.objects.filter(medium="Hindi"))
            BhojpuriSongs = list(Musics.objects.filter(medium="Bhojpuri"))
            punjabiSongs = list(Musics.objects.filter(medium="PUNJABI"))
            bhaktiSongs = list(Musics.objects.filter(medium="BHAKTI"))
            TotalMusics = musics.__len__()
            TotalMusicsHindi = hindiSongs.__len__()
            TotalMusicsBhojpuri = BhojpuriSongs.__len__()
            TotalMusicsPunjabi = punjabiSongs.__len__()
            TotalMusicsBhakti = bhaktiSongs.__len__()
            random.shuffle(musics)
            random.shuffle(hindiSongs)
            random.shuffle(BhojpuriSongs)
            random.shuffle(punjabiSongs)
            random.shuffle(bhaktiSongs)
            context = {
                "musics": musics,
                "TotalMusics": TotalMusics,
                "hindiSongs": hindiSongs,
                "BhojpuriSongs": BhojpuriSongs,
                "punjabiSongs": punjabiSongs,
                "bhaktiSongs":bhaktiSongs,
                "TotalMusicsHindi": TotalMusicsHindi,
                "TotalMusicsBhojpuri": TotalMusicsBhojpuri,
                "TotalMusicsPunjabi": TotalMusicsPunjabi,
                "TotalMusicsBhakti":TotalMusicsBhakti,
            }
            res = render(request, "home.html", context)
    else:
        res = render(request, "login.html")
    return res


def home(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        hindiSongs = list(Musics.objects.filter(medium="Hindi"))
        BhojpuriSongs = list(Musics.objects.filter(medium="Bhojpuri"))
        punjabiSongs = list(Musics.objects.filter(medium="PUNJABI"))
        bhaktiSongs = list(Musics.objects.filter(medium="BHAKTI"))
        musics = list(Musics.objects.all())
        TotalMusics = musics.__len__()
        TotalMusicsHindi = hindiSongs.__len__()
        TotalMusicsBhojpuri = BhojpuriSongs.__len__()
        TotalMusicsPunjabi = punjabiSongs.__len__()
        TotalMusicsBhakti = bhaktiSongs.__len__()
        random.shuffle(musics)
        random.shuffle(hindiSongs)
        random.shuffle(BhojpuriSongs)
        random.shuffle(punjabiSongs)
        random.shuffle(bhaktiSongs)
        context = {
            "musics": musics,
            "TotalMusics": TotalMusics,
            "hindiSongs": hindiSongs,
            "BhojpuriSongs": BhojpuriSongs,
            "punjabiSongs": punjabiSongs,
            "bhaktiSongs":bhaktiSongs,
            "TotalMusicsHindi": TotalMusicsHindi,
            "TotalMusicsBhojpuri": TotalMusicsBhojpuri,
            "TotalMusicsPunjabi": TotalMusicsPunjabi,
            "TotalMusicsBhakti":TotalMusicsBhakti,
        }
        res = render(request, "home.html", context)
    return res


def profile(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        user = User.objects.filter(Username=request.session["username"])
        context = {"user": user[0]}
        res = render(request, "profile.html", context)
    return res


def editProfile(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            user = User()
            user.Username = request.session["username"]
            user.password = request.POST["password"]
            user.name = request.POST["name"]
            user.mobile = request.POST["mobile"]
            user.email = request.POST["email"]
            user.save()
            res = HttpResponseRedirect("home")
        else:
            res = render(request, "profile.html")
    return res


def musicUpload(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            music = Musics()
            music.name = request.POST["name"]
            music.type = request.POST["type"]
            music.medium = request.POST["medium"]
            music.singer = request.POST["singer"]
            music.writer = request.POST["writer"]
            music.musicFile = request.FILES["musicFile"]
            try:
                music.musicThumbnail = request.FILES["musicThumbnail"]
            except:
                pass
            music.save()
            musicStatus = 1
        else:
            musicStatus = 2
        context = {"musicStatus": musicStatus}
        res = render(request, "musicUpload.html", context)
    return res


def musicDelete(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            doc = Musics.objects.filter(musicId=request.POST["musicId"])
            doc.delete()
            musicStatus = 1
        else:
            musicStatus = 2
        context = {"musicStatus": musicStatus}
        res = render(request, "musicDelete.html", context)
    return res


def logout(request):
    if "name" in request.session.keys():
        del request.session["username"]
        del request.session["name"]
    res = HttpResponseRedirect("login")
    return res
