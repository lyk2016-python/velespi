from django.contrib import admin

from places.models import (
	Place, Category, Review, Media
)

class MediaInline(admin.TabularInline):
	model = Media
	extra = 0

class ReviewInline(admin.TabularInline):
	model = Review
	extra = 0

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('name', 'user', 'category', 'has_wifi')
	list_editable = ('category', 'has_wifi')
	inlines = [
		MediaInline,
		ReviewInline,
	]

admin.site.register(Place, PlaceAdmin)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Media)
