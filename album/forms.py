from django import forms

from album.models import Artiste
# To house all our forms logics in one file


class AlbumForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
