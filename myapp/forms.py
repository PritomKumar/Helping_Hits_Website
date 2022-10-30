from django import forms
from .models import Data


class DataForm(forms.ModelForm):
    song_url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a valid Spotify Song URL'}))
    class Meta:
        model = Data
        fields = ['song_url']

