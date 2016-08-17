from django.forms import ModelForm

from places.models import Place

class PlaceCreationForm(ModelForm):
	class Meta:
		model = Place
		fields = (
			'name',
			'coordinates',
			'category',
			'has_wifi',
			'telephone',
			'description',
		)
