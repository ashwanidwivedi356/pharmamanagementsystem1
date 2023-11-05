from django.shortcuts import render, HttpResponseRedirect
from .forms import DoctorRegistration
from .models import User
# Create your views here.

# This Function Will Add new Item and Show All Items
def add_show(request):
 if request.method == 'POST':
  fm = DoctorRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['Doctor_name']
   sm = fm.cleaned_data['Specialization']
   op = fm.cleaned_data['Openning_time']
   oc = fm.cleaned_data['Closing_time']
   oD = fm.cleaned_data['Doctor_fees']
   reg = User(Doctor_name=nm, Specialization=sm, Openning_time=op,Closing_time=oc,Doctor_fees=oD)
   reg.save()
   fm = DoctorRegistration()
 else:
  fm = DoctorRegistration()
 doct = User.objects.all()
 return render(request, 'enroll/addandshow.html', {'form':fm, 'doc':doct})

# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  fm = DoctorRegistration(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = User.objects.get(pk=id)
  fm = DoctorRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')