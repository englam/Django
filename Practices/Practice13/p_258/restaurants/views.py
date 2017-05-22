#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response

def menu(request):
	food = {'name' : '蕃茄炒蛋', 'price' : 60, 'comment' : 'Delicious', 'is_spice': False}

	return render_to_response('menu.html',locals())

def menu2(request):
	food1 = {'name' : '蕃茄炒蛋', 'price' : 60, 'comment' : 'Delicious', 'is_spice': False}
	food2 = {'name' : '蒜泥白肉', 'price' : 160, 'comment' : '人氣推薦', 'is_spice': True}

	foods = [food1, food2]

	return render_to_response('menu2.html',locals())


def menu3(request):
	food1 = {'name' : '蕃茄炒蛋', 'price' : 60, 'comment' : 'Delicious', 'is_spice': False}
	food2 = {'name' : '蒜泥白肉', 'price' : 160, 'comment' : '人氣推薦', 'is_spice': True}

	foods = [food1, food2]

	return render_to_response('menu3.html',locals())
