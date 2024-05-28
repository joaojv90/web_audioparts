from django.shortcuts import render, HttpResponse
from django.http import FileResponse, Http404
from django.conf import settings
import os

def index(request):
    return render(request, 'core/index.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def privacypolicy(request):
    return render(request, 'core/privacypolicy.html')

def about(request):
    return render(request, 'core/about.html')

def error404(request, exception):
    return render(request, 'core/error404.html')

def download_pdf(request, filename):
    file_path = os.path.join(settings.STATIC_ROOT, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf', as_attachment=True, filename=filename)
    else:
        raise Http404("Archivo no encontrado")