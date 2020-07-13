from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

# Create your views here.
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article,Comment,Live,Lyric,Chord
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import permissions
from blog.serializers import UserSerializer, GroupSerializer, LiveSerializer, LyricSerializer, ChordSerializer

def articles(request):
    articles = Article.objects.all()

    return HttpResponse(articles[1].content)

def index(request):
    return render(request,"index.html")

class UserViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = GroupSerializer

class LiveViewSet(viewsets.ModelViewSet):
    queryset = Live.objects.all()
    serializer_class = LiveSerializer

class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

class ChordViewSet(viewsets.ModelViewSet):
    queryset = Chord.objects.all()
    serializer_class = ChordSerializer
