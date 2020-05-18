from .models import *

def news(request):
		categories = Category.objects.all()
		home = News.objects.filter(home=True).order_by('-id')[:4]
		last_4 = News.objects.filter(home=False,slider=False).order_by('-id')[:4]
		footer = News.objects.filter(home=False,slider=False).order_by('?')[:3]
		try:
			mini = News.objects.filter(home=False,slider=False).order_by('-id')[4:8]
			mini_2 = News.objects.filter(home=False,slider=False).order_by('-id')[8:12]
			slider = News.objects.filter(slider=True).order_by('-id')[:6]
			popular = News.objects.filter(popular=True).order_by('-id')[:3]
			reviews = News.objects.all().order_by('-views')[:3]
			most_commented = News.objects.all().order_by('-comment')[:3]
			print(most_commented)
		except:
			mini_2 = News.objects.all().order_by('?')[:4]
			slider = News.objects.all().order_by('?')[:4]
			mini = News.objects.all().order_by('?')[:4]
			popular = News.objects.all().order_by('?')[:3]
			reviews = News.objects.all().order_by('?')[:3]
			most_commented = News.objects.all().order_by('?')[:3]	
		context = {'categories':categories, 'last_4':last_4}
		context['slider'] = slider
		context['mini'] = mini
		context['mini_2'] = mini_2
		context['popular'] = popular
		context['reviews'] = reviews
		context['most_commented'] = most_commented
		context['home'] = home
		context['footer'] = footer
		return context