from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Box
# Create your views here.

def box_list(request):

    boxes = Box.objects.all()

    return render(request, 'bigbox/box.html', {"boxes": boxes})

def box(request,pk):

    box = get_object_or_404(Box, pk=pk)
    details = list(box.activities.all()[:5])

    return render(request, 'bigbox/box-details.html', {"box": box, "details": details})

def box_activities(request,pk):

    box = get_object_or_404(Box, pk=pk)
    details = list(box.activities.all())
    paginator = Paginator(details, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'bigbox/box-activities.html', {'page_obj': page_obj})
