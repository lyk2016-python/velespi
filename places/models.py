from django.db import models
from django.conf import settings
from django.utils.encoding import smart_text


class Category(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return smart_text(self.name)

class Place(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=False)
	coordinates = models.CharField(max_length=255, null=True, blank=True)
	category = models.ForeignKey(Category, blank=True, null=True)
	has_wifi = models.BooleanField(default=False)
	telephone = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return smart_text(self.name)

class Review(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	place = models.ForeignKey(Place)
	comment = models.TextField(null=True, blank=True)
	vote = models.IntegerField(default=3)

	def __str__(self):
		return smart_text(self.comment)

class Media(models.Model):
	place = models.ForeignKey(Place)
	image = models.ImageField(upload_to="places")

	class Meta:
		verbose_name_plural = "Media"

	def __str__(self):
		return smart_text(self.image.url)







