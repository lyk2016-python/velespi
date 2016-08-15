from django.shortcuts import render
from places.models import Place


def index(request):
	return render(
		request,
		'index.html',
		{
			'places': Place.objects.all(),
		}
	)
