from django.shortcuts import render
from .models import Poster

def all_posters(request):
    """ A view to display all posters"""

    posters= Poster.objects.all()

    context = {
        'posters' : posters, 
    }
    
    return render(request, 'products/posters.html', context)
