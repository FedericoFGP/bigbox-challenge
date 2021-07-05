from django.shortcuts import render
from .models import Box
# Create your views here.

def box(request):

    boxes = Box.objects.all()
    return render(request, 'bigbox/box.html', {"boxes": boxes})
