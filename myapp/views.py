from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


def predictions(request):
    predicted_song_urls = Data.objects.all().last()
    context = {
        'predicted_sports': predicted_song_urls
    }
    return render(request, 'dashboard/predictions.html', context)
