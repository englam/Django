from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html', RequestContext(request,locals()))

def index(request):
    return render_to_response('index.html', RequestContext(request,locals()))

def login(request):
    #if request.user.is_authenticated():
        #return HttpResponseRedirect('/index/')

    #username = request.POST.get['username']
    #password = request.POST.get['password']
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    #if user is not None and user.is_active:
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html',RequestContext(request,locals()))