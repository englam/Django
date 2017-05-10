from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', RequestContext(request,locals()))

