#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django import template
from django.template.loader import get_template

#http://127.0.0.1:8000/here1/
def here(request):
	return HttpResponse("I am here !!")

#http://127.0.0.1:8000/11/plus/31/
def add(request, a,b):
	s = int(a) + int(b)
	return HttpResponse(str(s))

def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a+b
	d = a-b
	p = a*b
	q = a/b


	#html = "<html>sum = {s} <br>dif = {d} <br>pro = {p} <br>quo = {q} <br></html>".format(s=s,d=d,p=p,q=q)

	html = '''<html>
			sum = {s} <br>
			dif = {d} <br>
			pro = {p} <br>
			quo = {q} <br>
	</html>'''.format(s=s,d=d,p=p,q=q)

	return HttpResponse(html)


#http://127.0.0.1:8000/11/math2/31/
def math2(request, a, b):
	a = int(a)
	b = int(b)
	s = a+b
	d = a-b
	p = a*b
	q = a/b

	t = template.Template('<html> s = {{s}} <br> d = {{d}} <br> p = {{p}} <br>q = {{q}}</html>')

	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
	return (HttpResponse(t.render(c)))



#http://127.0.0.1:8000/11/math3/10/
def math3(request, a, b):
	a = int(a)
	b = int(b)
	s = a+b
	d = a-b
	p = a*b
	q = a/b

	with open('templates/math.html','r') as reader:
		t = template.Template(reader.read())

	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
	return (HttpResponse(t.render(c)))



# 要新增template folder的路徑到settings裡面 就可以直接呼叫物件
# add TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),) to settings.py
# http://127.0.0.1:8000/11/math4/10/
def math4(request, a, b):
	a = int(a)
	b = int(b)
	s = a+b
	d = a-b
	p = a*b
	q = a/b

	t = get_template('math.html')

	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
	return (HttpResponse(t.render(c)))



from django.shortcuts import render_to_response

def math5(request, a, b):
	a = int(a)
	b = int(b)
	s = a+b
	d = a-b
	p = a*b
	q = a/b

	#locals <-外部的參數進來為值 所以 a 跟 b都是為值，內部的參數有 s , d , p , q, 會被轉成字典
	return (render_to_response('math.html',locals()))
	#return (render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q}))
