from django.shortcuts import render
from carapp.forms import car_form
# Create your views here.
def car_form_view(request):
    form=car_form()
    if request.method=="POST":
        form=car_form(request.POST)
        if form.is_valid():
            form.save()
            # print("validation Success")
    return render(request,'cars.html',{'form':form})