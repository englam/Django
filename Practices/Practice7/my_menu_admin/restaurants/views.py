#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food

def menu(request):
	restaurants = Restaurant.objects.all()

	return render_to_response('menu.html',locals())

def menu2(request):
	restaurants = Restaurant.objects.all()

	return render_to_response('menu2.html',locals())
