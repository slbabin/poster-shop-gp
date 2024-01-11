from django.shortcuts import render, get_object_or_404
from .models import Poster

def all_posters(request):
    """ A view to display all posters"""

    posters= Poster.objects.all()

    context = {
        'posters' : posters, 
    }
    
    return render(request, 'products/posters.html', context)


def poster_detail(request, poster_id):
    """ A view to display a poster details"""

    poster = get_object_or_404(Poster, pk=poster_id)

    context = {
        'poster' : poster, 
    }
    
    return render(request, 'products/poster_detail.html', context)
