
from django.shortcuts import render, redirect
from django.views import View
from .forms import AlbumForm, AlbumModelForm
from django.contrib import messages
from .models import Song, Artiste, Lyric

# Creating a website that encompasses CRUD + L  implementaion on the frontend


class navigation(View):
    template_name = 'album/navigation.  html'


def album_list(request):
    album = Artiste.objects.all()
    context = {
        'album': album
    }
    return render(request, 'album/album_list.html', context)


def album_detail(request, pk):

    album = Artiste.objects.get(id=pk)
    context = {
        "album": album
    }
    return render(request, "album/album_detail.html", context)


def album_create(request):
    form = AlbumModelForm()  # we reassign the data if not validated
    if request.method == 'POST':
        print('Receiving a post request')
        form = AlbumModelForm(request.POST)
        # we can check if form is valid
        if form.is_valid():
            form.save()
            return redirect('/album')  # redirect us back to our homepage
    context = {
        'form': form
    }
    messages.info(request, "You have successfully created your Album choice.")
    return render(request, 'album/album_create.html', context)

# Update a lead using existing form


def album_update(request, pk):
    album = Artiste.objects.get(id=pk)
    form = AlbumModelForm(instance=album)
    if request.method == 'POST':
        form = AlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('/album')
    context = {
        'form': form,
        'artiste': album
    }
    messages.info(
        request, "You have successfully updated your Artiste choice.Thank you!")
    return render(request, 'album/album_update.html', context)


def album_delete(request, pk):
    album = Artiste.objects.get(id=pk)
    album.delete()
    messages.info(
        request, "You have successfully deleted your Artiste.Thank you!")
    return render(request, 'album/album_delete.html')


"""
def album_update(request, pk):
    album = Artiste.objects.get(id=pk)
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
       # we can check if form is valid
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            artiste.first_name = first_name
            artiste.last_name = last_name
            artiste.age = age
            artiste.first_name = first_name
            artiste.save()  # commit the changes to database to update

            return redirect('/album')  # redirect us back to our homepage
    context = {
        'form': form,
        'album': album
    }
    return render(request, 'album/album_update.html', context)
"""


# def album_create(request):
#  # if request.method == 'POST':
#        form = AlbumForm(request.POST)
#       # we can check if form is valid
#       if form.is_valid():
#           print('The form is valid')
#           print(form.cleaned_data)
#           first_name = form.cleaned_data['first_name']
#           last_name = form.cleaned_data['last_name']
#           age = form.cleaned_data['age']
#           song = Song.objects.first()  # created a first instance of song variable
#           lyric = Lyric.objects.first()
#          Artiste.objects.create(
#               first_name=first_name,
#               last_name=last_name,
#               age=age,
#               song=song,
#               lyric=lyric
#         )
#          print('The album has been created.')
#          return redirect('/album')  # redirect us back to our homepage
#  context = {
#       'form': form
#  }

#  return render(request, 'album/album_create.html', context)
