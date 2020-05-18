from django.shortcuts import render
from .models import *
from django.db.models  import Q
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse,Http404


# Create your views here.

class IndexView(View):
	def get(self, request):
		return render(request, 'index.html' )

class CategoryView(View):
	def get(self, request, category_slug):
		print(request)
		try:
			category = get_object_or_404(Category, slug__iexact=category_slug)
		except:	
			c = get_object_or_404(SubCategory, slug__iexact=category_slug)
			category = c.category
			print('C cat {}'.format(c))
			print('Category {}'.format(category))
		# else:
		# 	raise Http404("Category no matches the given query") 	
		news = News.objects.filter(category=category)
		context = {'news':news,'category':category}
		return render(request, 'category.html', context)

class NewsView(View):
	def get(self, request, news_slug):
		categories = Category.objects.all()
		news = get_object_or_404(News, slug__iexact=news_slug)
		news.views += 1
		news.save()
		category = news.category
		context = {'news':news, 'categories':categories,'category':category}	
		return render(request, 'single.html', context)


def count_shared(request):
	news_id = request.GET.get('data')
	try:
		news = News.objects.get(id=news_id)
		news.shared += 1
		news.save()
		data = {'code':400}			
	except:	
		data = {'code':200}
	return JsonResponse(data)

def news_comments(request):
	news_id = request.GET.get('data')
	news = News.objects.get(id=news_id)
	c = news.comments_set.all()
	comment_count = c.count()
	if comment_count > 0:
		data = {'status':'ok','comments':[]}
		for c in c:
			l = []
			l.append(c.author)					
			l.append(c.comment)
			data['comments'].append(l)
	else:
		data = {'status':'no-comment','comments':[]}
			
	return JsonResponse(data)

def add_comment(request):
	name = request.POST['name']							
	email = request.POST['email']							
	message = request.POST['message']							
	news_id = request.POST['news_id']
	try:
		news = News.objects.get(id=news_id)
		news.comment += 1
		news.save()
		print(news.comment)
		c = Comments.objects.create(author=name,email=email,comment=message,news=news)
		data = {'code':400}			
	except:	
		data = {'code':200}
	return JsonResponse(data)

def search_news(request):
	query = request.GET.get('q')
	q = Q(title__icontains=query) | Q(description__icontains=query)
	try:
		news = News.objects.filter(q)
		data = {'status':'ok','news':[]}
		for c in news:
			l = []
			l.append(c.title)					
			l.append(c.slug)
			data['news'].append(l)
	except:
		data = {'status':'error','news':[]}
	print(data)	
	return JsonResponse(data)						


