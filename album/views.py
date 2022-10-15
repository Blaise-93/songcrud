from django.shortcuts import render, redirect
from django.views import View
from .forms import AlbumForm
from .models import Song, Artiste, Lyric

# Creating a website that encompasses CRUD + L  implementaion on the frontend


def album_list(request):
    album = Artiste.objects.all()
    context = {
        'album': album
    }
    return render(request, 'album/album_list.html', context)


def album_detail(request, pk):

    artiste = Artiste.objects.get(id=pk)
    context = {
        "artiste": artiste
    }
    return render(request, "album/album_detail.html", context)


def album_create(request):
    form = AlbumForm()  # we reassign the data if not validated
    if request.method == 'POST':
        print('Receiving a post request')
        form = AlbumForm(request.POST)
        # we can check if form is valid
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            song = Song.objects.first()  # created a first instance of song variable
            lyric = Lyric.objects.first()
            Artiste.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                song=song,
                lyric=lyric
            )
            print('The album has been created.')
            return redirect('/album')  # redirect us back to our homepage
    context = {
        'form': form
    }

    return render(request, 'album/album_create.html', context)
