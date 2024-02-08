from django.shortcuts import render

def index(request):
    """ A view to return the index page """
    
    return render(request, 'homeapp/index.html')


def terms(request):
    """ A view to return terms page """
    
    return render(request, 'homeapp/terms.html')


def about(request):
    """ A view to return about page  """
    
    return render(request, 'homeapp/about-company.html')


def returnpolicy (request):
    """ A view to return return page  """
    
    return render(request, 'homeapp/return.html')


def contact (request):
    """ A view to return contact page  """
    
    return render(request, 'homeapp/contact.html')    