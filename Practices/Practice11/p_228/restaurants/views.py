from django.shortcuts import render
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food, Comment
from django.template import RequestContext


def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('retaurants_list.html',locals())
