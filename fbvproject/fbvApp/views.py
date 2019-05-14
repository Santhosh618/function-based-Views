from django.shortcuts import render,redirect
from .models import Employee
from .import forms


# Create your views here.
def thank_view(request):
    return render(request,'testApp/tnk.html')


def form_view(request):
    form=forms.EmployeeForm()

    if request.method=='POST':
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form Data Added Successfully')
            print('Name:',form.cleaned_data['ename'])
            print('ID:',form.cleaned_data['eid'])
            print('Salary:',form.cleaned_data['esalary'])
            print('Address:',form.cleaned_data['eadd'])
            return thank_view(request)

    return render(request,'testApp/form.html',{'form':form})

def data_view(request):
    form=Employee.objects.all()
    return render(request,'testApp/empdata.html',{'form':form})

def Delete_view(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return data_view(request)

def Update_view(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return data_view(request)
    return render(request,'testApp/Update.html',{'emp':emp})
