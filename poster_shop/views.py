from django.shortcuts import render


def handler404(request, exception):
    """ Error 404 Handler  - Page Not Found """
    return render(request, "errors/404.html", status=404)