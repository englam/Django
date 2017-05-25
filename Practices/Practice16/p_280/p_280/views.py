#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from restaurants.models import Restaurant, Food, Comment
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404
from form import CommentForm


from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView



from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin



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


def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('retaurants_list.html',locals())

class list_restaurants2(ListView):

    #資料庫 Model
    model = Restaurant
    #使用的模版
    template_name = 'retaurants_list.html'
    #取出Model裡的變量
    context_object_name = 'restaurant'
    #設定排序名稱
    #queryset = Restaurant.objects.order_by("-name")

    #這段取消 list_restaurants2 就可以用了，因為目前沒有login, 這邊是login example
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(list_restaurants2,self).dispatch(request,*args, **kwargs)




def menu3(request):
	#restaurant = Restaurant.objects.get(id=1)
	#return render_to_response('menu3.html',locals())
	if 'id' in request.GET and request.GET['id'] !='':
		restaurant = Restaurant.objects.get(id=request.GET['id'])
		return render_to_response('menu3.html', locals())
	else:
		return HttpResponseRedirect("/restaurants_list/")


class menu3View(DetailView):

    model = Restaurant
    template_name = 'menu3.html'
    context_object_name = 'restaurant'
    #pk_url_kwarg = 'id'

	#def get(self, request, pk, *args, **kwargs):
		#try:
			#return super(menu3View, self).get(self, request, pk=pk, *args, **kwargs)
		#except Http404:
			#return HttpResponseRedirect('/restaurants_list/')


'''

self.render_to_response(self.get_context_data(form = self.form_class(initial=self.initial))) 等於

context = self.get_context_data()
context['form'] = self.form_class(initial=self.initial)
return self.render_to_response(context(

'''



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




class comment2(FormView):

	form_class 		= CommentForm #代入的表單類別
	template_name 	= 'comments2.html'
	success_url 	= '/comment2/' #指定成功後要代入的位置
	initial		 	= {'content' : u'我沒意見'}
	model 			= Restaurant
	context_object_name= 'r'

	def form_valid(self, form):
		Comment.objects.create(
			visitor=visitor,
			email=email,
			content=content,
			date_time=date_time,
			restaurant=self.get_object()
		)
		return self.render_to_response(self.get_context_data(
			form = self.form_class(initial=self.initial))
		)

	#def get_context_data(self, **kwargs):
		#self.object = self.get_object()
		#return super(CommentView, self).get_context_data(object=self.object, **kwargs)


'''

在comments2.html裡面有些參數是r, 因為在原始的comment是用r去取資料庫的
這邊是用def get_context_data的方法，這邊還沒成功需要再修改

	#def get_context_data(self, **kwargs):
		#self.object = self.get_object()
		#return super(CommentView, self).get_context_data(object=self.object, **kwargs)

'''
