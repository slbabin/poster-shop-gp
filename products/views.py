from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Poster, Category
from .forms import PosterForm
from django.contrib.auth.decorators import login_required


def all_posters(request):
    """ A view to display all posters"""

    posters= Poster.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                posters = posters.annotate(lower_name=Lower('title'))

            if sortkey == 'category':
                    sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posters = posters.order_by(sortkey)        
        

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posters = posters.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error("request, You didn't enter any search query")
                return redirect(reverse('posters'))

            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(artist__icontains=query)
            posters = posters.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posters' : posters, 
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'products/posters.html', context)


def poster_detail(request, poster_id):
    """ A view to display a poster details"""

    poster = get_object_or_404(Poster, pk=poster_id)

    context = {
        'poster' : poster, 
    }
    
    return render(request, 'products/poster_detail.html', context)

@login_required
def add_poster(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, this action can be performed only by admin.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            poster = form.save()
            messages.success(request, 'Successfully added poster')
            return redirect(reverse('poster_detail', args=[poster.id]))
        else:
            messages.error(request, 'Failed to add poster. Check if all fields a valid.')    
    else:

        form = PosterForm()
    template = 'products/add_poster.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_poster(request, poster_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, this action can be performed only by admin.")
        return redirect(reverse('home'))

    poster = get_object_or_404(Poster, pk=poster_id)

    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES, instance = poster)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the poster')
            return redirect(reverse('poster_detail', args=[poster.id]))
        else:
            messages.error(request, 'Failed to update poster. Check if all fields a valid.') 
    else:        
        form = PosterForm(instance=poster)
        messages.info(request, f'You are editing {poster.title}')

    template = 'products/edit_poster.html'
    context = {
        'form': form,
        'poster': poster
    }

    return render(request, template, context)


@login_required
def delete_poster(request, poster_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, this action can be performed only by admin.")
        return redirect(reverse('home'))
        
    poster = get_object_or_404(Poster, pk=poster_id)
    poster.delete()
    messages.success(request, 'Successfully deleted  poster')
    return redirect(reverse('posters'))
