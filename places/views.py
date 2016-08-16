from django.shortcuts import render, get_object_or_404
from places.models import Place


def index(request):
    return render(
        request,
        'index.html',
        {
            'places': Place.objects.all(),
        }
    )


def detail(request, id):
	return render(
        request,
        'place.html',
        {
            'place': get_object_or_404(Place, id=id),
        }
    )
