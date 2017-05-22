from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import RequestContext, Template, loader
from django.shortcuts import render_to_response, render


def test(request):
    return render_to_response('test.html', locals())

def test1(request):
    return render_to_response('test1.html', locals())

def test2(request):
    return render_to_response('test2.html', locals())


def test5(request):
    t = get_template('test5.html')
    a = 1
    b = 2
    m = 'haha'
    c = template.Context({'a':a,'b':b,'m':m})
    return (HttpResponse(t.render(c)))



def test6(request):
    return {
        'a': 1,
        'b': 2
    }

def test7(request):
    t = loader.get_template('test6.html')
    rc = RequestContext(request, {'m': 'test7'}, processors=[test6])
    return (HttpResponse(t.render(rc)))


def test9(request):
    return render_to_response(
        'test6.html', {'m':'test9'}, context_instance = RequestContext(request,processors=[test6])
    )

def test10(request):
    return render_to_response(
        'test6.html', {'m':'test10'}, context_instance = RequestContext(request)
    )

def test11(request):
    return render(
        request,'test6.html', {'m':'test11'}
    )
