import requests
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Box, Category, Activity
# Create your views here.

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    print
    return HttpResponse('<pre>' + r.text + '</pre>', content_type="text/html; charset=utf-8")

def box_list(request):
    boxes = Box.objects.all()
    return render(request, 'bigbox/box.html', {"boxes": boxes})

def box(request,pk):
    box = get_object_or_404(Box, pk=pk)
    details = list(box.activities.all()[:5])
    category = get_category(box.category_id)
    disponibilidad = box_disponibilidad(box)
    return render(request, 'bigbox/box-details.html', {"box": box, "details": details, "category":category, "disponibilidad": disponibilidad})

def get_category(id):
    category = Category.objects.get(id=id)
    return category

def box_disponibilidad(box):

    return "Disponible" if box.purchase_available else "No disponible"

def box_activities(request,pk):

    box = get_object_or_404(Box, pk=pk)
    details = list(box.activities.all())
    paginator = Paginator(details, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'bigbox/box-activities.html', {'page_obj': page_obj})

def box_slug(request,slug):

    linked_box = Box.objects.get(slug = slug)

    return box(request,linked_box.pk)

def box_relation_status(request,box_pk,activity_id):
    try:
        box = get_object_or_404(Box, pk=box_pk)
    except:
        return render(request,'bigbox/non-existent-box.html', {'box_pk': box_pk})
    try:
        activity = get_object_or_404(Activity, id=activity_id)
    except:
        return render(request,'bigbox/non-existent-activity.html', {'activity_id': activity_id})

    status = status_relation(box_pk,activity_id)

    return render(request, 'bigbox/box-status-related.html', {'status': status,'box_name': box.name, 'activity_name': activity.name})

def status_relation(box_pk, activity_id):
    box = get_object_or_404(Box, pk = box_pk)
    activities = box.activities.all()
    return "relacionado" if activities.filter(id=activity_id) else "no relacionado"
