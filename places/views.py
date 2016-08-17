from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from places.models import Place
from places.forms import PlaceCreationForm, MediaCreationForm


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

def new_place(request):
    form = PlaceCreationForm()

    if request.method == "POST":
        form = PlaceCreationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.info(
                request,
                'Tebrikler. Yer bildiriminiz başarıyla alındı. '
                'Editör onayından geçtikten sonra yayınlanacaktır.'
            )
            return redirect('/')

    return render(
        request,
        'new_place.html',
        {
            'form': form,
        }
    )

def new_media(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    form = MediaCreationForm()

    if request.method == "POST":
        form = MediaCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.place = place
            form.save()
            return redirect(place.get_absolute_url())

    return render(
        request,
        'new_media.html',
        {
            'place': place,
            'form': form,
        }
    )

