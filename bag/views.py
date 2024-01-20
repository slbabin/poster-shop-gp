from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_bag(request):
    """ A view to view a bug page """
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'poster_size' in request.POST:
        size = request.POST['poster_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):

            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

    else:

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """Adjust quantity of the specified product"""  

    
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'poster_size' in request.POST:
        size = request.POST['poster_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]

    else:

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
