from django.shortcuts import render
from django.http import HttpResponse
from . models import Department, Doctore
from . forms import BookingForm
def index(request):
    return render(request,"index.html")
def department(request):
    department=Department.objects.all()
    return render(request,"department.html",{"department":department})
def doctor(request):
    doctor=Doctore.objects.all()
    return render(request,"doctor.html",{"doctor":doctor})
def booking(requst):
    form=BookingForm()
    if requst.method=='POST':
        form=BookingForm(requst.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Booking Success</h1>")
    return render(requst,"booking.html",{"form":form})

# Create your views here.
