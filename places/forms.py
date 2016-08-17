from django.forms import ModelForm, HiddenInput

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
		widgets = {
			'coordinates': HiddenInput
		}
