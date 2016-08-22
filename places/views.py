import json

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from places.models import Place
from places.forms import PlaceCreationForm, MediaCreationForm, ReviewCreationForm


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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def new_review(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    form = ReviewCreationForm()

    if request.method == "POST":
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.place = place
            form.save()
            return redirect(place.get_absolute_url())

    return render(
        request,
        'new_review.html',
        {
            'place': place,
            'form': form,
        }
    )


@login_required(login_url='login')
def like_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    if request.method == "POST":

        if request.user in place.likes.all():
            place.likes.remove(request.user)
            action = 'unlike'
        else:
            place.likes.add(request.user)
            action = 'like'

        if request.is_ajax():
            return HttpResponse(
                json.dumps({
                    'count': place.likes.count(),
                    'action': action
                })
            )

    else:
        return HttpResponse(status_code=403)

    return redirect(place.get_absolute_url())
