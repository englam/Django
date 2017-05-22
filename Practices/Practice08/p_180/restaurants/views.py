#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext
from form import CommentForm
from django.contrib.sessions.models import Session

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
		#單一check error的方法
		#error = any(not request.POST[k] for k in request.POST)
		errors = []

		if any(not request.POST[k] for k in request.POST):
			errors.append('*有空白欄位，請不要留空白')

		if '@' not in email:
			errors.append('*E-Mail格式有錯誤')


		if not errors:
			#下面for database
			Comment.objects.create(
				visitor = visitor,
				email	= email,
				content	= content,
				date_time  = date_time,
				restaurant = r
			)
			'''輸入完後，將格子上的參數清除'''
			visitor, email, content =('','','')

	return render_to_response('comments.html',RequestContext(request,locals()))

'''For form'''
def comment2(request,id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect("/restaurants_list/")

	if request.POST:
		f = CommentForm(request.POST)
		if f.is_valid():
			visitor = f.cleaned_data['visitor']
			content = f.cleaned_data['content']
			email	= f.cleaned_data['email']
			date_time = timezone.localtime(timezone.now())

			c = Comment.objects.create(
				visitor=visitor,
				email=email,
				content=content,
				date_time=date_time,
				restaurant=r
			)
			f = CommentForm(initial={'content':'我沒意見'})
	else:
		#f = CommentForm()
		f = CommentForm(initial={'content': '我沒意見'})
	return render_to_response('comments2.html',RequestContext(request,locals()))


# cookie set  http://127.0.0.1:8000/set_c/
def set_c(request):
	response = HttpResponse('Cookie Test')
	response.set_cookie('cookie_number', 8)
	return response


#cookie get http://127.0.0.1:8000/get_c/,
def get_c(request):

	if 'cookie_number' in request.COOKIES:
		return HttpResponse('Your Cookie Number is {0}'.format(request.COOKIES['cookie_number']))
	else:
		return HttpResponse('No Cookie')


#session
def use_session(request):
	request.session['lucky_session_number'] = 8
	if 'lucky_session_number' in request.session:
		lucky_number = request.session['lucky_session_number']
		response = HttpResponse('Session Number : {0}'.format(lucky_number))
	del request.session['lucky_session_number']
	return response


def session_test(request):
	#sid = request.COOKIES['sessionid']
	#s = Session.objects.get(pk=sid)
	#s_info = 'Session ID: ' + sid + '<br>Expire_date: ' + str(s.expire_date) + '<br>Data:' +str(s.get_decoded())
	response = HttpResponse('Cookie Test')
	response.set_cookie('cookie_number', 8)

	a = 8
	return (a)



