from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title','slug']	
	prepopulated_fields = {"slug": ("title",)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ['title','category','slug']	
	prepopulated_fields = {"slug": ("title",)}	


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ['id','title','category','views','popular','shared']
	list_display_links = ['id','title']
	prepopulated_fields = {"slug": ("title",)}
	list_filter = ['category',  'reg_data']
	search_fields = ['title','id']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
	list_display = ['news','author']	
	