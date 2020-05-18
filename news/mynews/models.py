from django.db import models
from django.urls import reverse
from django.conf import settings
from PIL import Image
from os import path
# Create your models here.

def image_folder(instance, filename):
	filename = instance.slug +'.'+filename.split('.')[1]
	return"{0}/{1}".format(instance.slug, filename)


class Category(models.Model):

	title = models.CharField('Kategoriya nomi *',max_length=50)
	slug = models.SlugField('Kalit so`z *',max_length=25, blank=True)
	
	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

	def __str__(self):
		return "{}".format(self.title)
	
	def get_absolute_url(self):
		return reverse ('mynews:category_view', kwargs={'category_slug':self.slug})

class SubCategory(models.Model):
	category =  models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name="Kategoriya *")	
	title = models.CharField('SubKategoriya nomi *',max_length=50)
	slug = models.SlugField('Kalit so`z *',max_length=25, blank=True)
	

	class Meta:
		verbose_name = 'SubKategoriya'
		verbose_name_plural = 'SubKategoriyalar'

	def __str__(self):
		return "{}".format(self.title)
	
	def get_absolute_url(self):
		return reverse ('mynews:category_view', kwargs={'category_slug':self.slug})

class News(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name="Kategoriya *")		
	subcategory = models.ForeignKey(SubCategory, on_delete = models.PROTECT, verbose_name="SubKategoriya ",blank=True, null=True)		
	title = models.CharField('Yanglik nomi *',max_length=90)
	slug = models.SlugField('Kalit so`z *',max_length=25)	
	description = models.TextField('Yanglik matni *',max_length=1550)
	views = models.PositiveIntegerField("Ko'rildi",default=0, blank=True)
	home = models.BooleanField("Bosh saxifaga",default=False)
	popular = models.BooleanField("Populyar",default=False)
	slider = models.BooleanField("Sliderga",default=False)
	shared = models.PositiveIntegerField("Ulashishlar soni",default=0, blank=True)
	comment = models.PositiveIntegerField("Muxokamalar soni",default=0, blank=True)
	info = models.CharField('Qisqa ma`lumot masalan yangi,new,ko`p ko`rildi kabi',max_length=5, blank=True)
	image_one = models.ImageField("Foto bosh saxifaga N:1 850x630px",upload_to=image_folder, blank=True)
	image_two = models.ImageField("Foto bosh saxifaga N:2 670x390", upload_to=image_folder,blank=True)
	image_there = models.ImageField("Foto boshqalar N:3 700x600*", upload_to=image_folder,blank=True)
	added = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True , verbose_name="Qo'shdi")
	avialable = models.BooleanField("Status",default=True)
	reg_data = models.DateTimeField("Qo'shilgan sana",auto_now_add=True)
	updated = models.DateField("Yangilandi",auto_now=True)


	class Meta:
		verbose_name = 'Yangilik'
		verbose_name_plural = 'Yangiliklar'

	def __str__(self):
		return "{}".format(self.title)

	def get_absolute_url(self):
		return reverse ('mynews:news_view', kwargs={'news_slug':self.slug})

	def save(self, *args, **kwargs):
		# Сначала - обычное сохранение
		super(News, self).save(*args, **kwargs)

		# Проверяем, указан ли логотип
		if self.image_one:
			filepath = self.image_one.path
			width = self.image_one.width
			height = self.image_one.height
			max_size = max(width, height)
			# Может, и не надо ничего менять?
			if max_size < 850:
			# Надо, Федя, надо
				image = Image.open(filepath)
				# resize - безопасная функция, она создаёт новый объект, а не
				# вносит изменения в исходный, поэтому так
				image = image.resize(
				(round(width / width * 850),  # Сохраняем пропорции
				round(height / height * 530)),
				Image.ANTIALIAS
				)
				# И не забыть сохраниться
				image.save(filepath)
		if self.image_two:
			filepath = self.image_two.path
			width = self.image_two.width
			height = self.image_two.height
			max_size = max(width, height)
			if max_size < 670:
				image = Image.open(filepath)
				image = image.resize((round(width / width * 670), round(height / height * 390)),
				Image.ANTIALIAS
				)
				image.save(filepath)
		if self.image_there:
			filepath = self.image_there.path
			width = self.image_there.width
			height = self.image_there.height
			max_size = max(width, height)
			if max_size > 125:
				image = Image.open(filepath)
				image = image.resize((round(width / width * 125), round(height / height * 125)),
				Image.ANTIALIAS
				)
				image.save(filepath)


class Comments(models.Model):
	news = models.ForeignKey(News, on_delete=models.CASCADE)
	author = models.CharField(max_length=25)
	email = models.CharField(max_length=45)
	comment = models.TextField()
			