#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext


def menu(request):
	restaurants = Restaurant.objects.all()
	path = request.path
	host = request.get_host()
	full_path = request.get_full_path()
	https_Y = request.is_secure()

	return render_to_response('menu.html',locals())

def menu2(request):
	restaurants = Restaurant.objects.all()

	return render_to_response('menu2.html',locals())

def menu3(request):
	#restaurant = Restaurant.objects.get(id=1)
	#return render_to_response('menu3.html',locals())
	if 'id' in request.GET and request.GET['id'] !='':
		restaurant = Restaurant.objects.get(id=request.GET['id'])
		return render_to_response('menu3.html', locals())
	else:
		return HttpResponseRedirect("/restaurants_list/")


def menu4(request,id):
	if id:
		restaurant = Restaurant.objects.get(id=id)
		return render_to_response('menu4.html', locals())
	else:
		return HttpResponseRedirect("/restaurants_list/")

def meta(request):
	values = request.META.items()
	values.sort()
	html =[]
	for k ,v in values:
		html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k,v))

	return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))


def welcome(request):
	if 'user_name' in request.GET and request.GET['user_name'] !='':
		return HttpResponse('Welcome!' + request.GET['user_name'])
	else:
		return render_to_response('welcome.html', locals())

def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('retaurants_list.html',locals())


def comment(request,id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect("/restaurants_list/")

	if request.POST:
		visitor = request.POST['visitor']
		content = request.POST['content']
		email	= request.POST['email']
		date_time = timezone.localtime(timezone.now())
		#下面for database
		Comment.objects.create(
			visitor = visitor,
			email	= email,
			content	= content,
			date_time  = date_time,
			restaurant = r
		)

	return render_to_response('comments.html',RequestContext(request,locals()))