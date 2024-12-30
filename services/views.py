from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    services = Service.objects.all()
    return render(request, "index.html", {"services": services})


def service(request, id):
    service = get_object_or_404(Service, id=id)
    details = ServiceDetail.objects.filter(service_id=id)
    return render(request, "service.html", {"service": service, "details": details})
