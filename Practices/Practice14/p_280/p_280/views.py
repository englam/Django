#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext

from django.views.generic.base import View, TemplateView

def here(request):
	return HttpResponse('I am Here')


class here2(View):

    def get(self,request):
        return HttpResponse('I am Here 2')


def index(request):
    return render_to_response('index.html', RequestContext(request,locals()))

class index2(TemplateView):

    template_name = 'index.html'

    def get(self,request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['request'] = request
        return self.render_to_response(context)
