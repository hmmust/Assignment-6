from django.shortcuts import render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
# Create your views here.
from .forms import CarForm,CarModelForm
from .models import Car,Owner
def info(request):
    return render(request,'car/base.html',{"info":Owner.objects.all()})
def add(request):
   if request.method=='GET':
       return render(request, 'car/add.html',{'form':CarModelForm()})
   else:
       if 'cancel' in request.POST:
           return render(request, 'car/base.html', {"info": Owner.objects.all()})
       else:
           f2= CarModelForm(request.POST)
           if f2.is_valid():
               f2.save()
               return HttpResponseRedirect(reverse("car:homepage"))
           else:
               return render(request, 'car/add.html', {'form':f2})

def edit(request,id):
   if request.method=='GET':
       f2 = CarModelForm(instance=Owner.objects.get(pk=id))
       return render(request, 'car/edit.html',{'form':f2,'id':id})
   else:
       if 'cancel' in request.POST:
           return render(request, 'car/base.html', {"info": Owner.objects.all()})
       else:
           f2= CarModelForm(request.POST)
           if f2.is_valid():
               f2.save()
               return HttpResponseRedirect(reverse("car:homepage"))
           else:
               return render(request, 'car/edit.html', {'form':f2})

def delete(request,id):
   if request.method=='GET':
       Owner.objects.get(pk=id).delete()

       return HttpResponseRedirect(reverse("car:homepage"))
   else:
       return HttpResponseRedirect(reverse("car:homepage"))


