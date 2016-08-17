from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from places.models import Place
from places.forms import PlaceCreationForm


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
