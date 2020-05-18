from django.urls import path, include
from . import views

app_name = 'mynews'

urlpatterns = [
  
    path('',views.IndexView.as_view(), name="index" ),
    path('category/<str:category_slug>',views.CategoryView.as_view(), name="category_view" ),
    path('news/<str:news_slug>',views.NewsView.as_view(), name="news_view" ),
    path('shared',views.count_shared, name="count_shared" ),
    path('news_comments',views.news_comments, name="news_comments" ),
    path('add_comment',views.add_comment, name="add_comment" ),
    path('search_news',views.search_news, name="search_news" ),
]