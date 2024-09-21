from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp.forms import StudentForm
def home(request):
    stud=Student.objects.all()
    return render(request,'apps/result.html', {'s':stud})
def insert(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/message')
    return render(request,'apps/insert.html',{'form':form,'show_table':False})
def msg(request):
    return render(request,'apps/message.html')
def delete(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('/result')
def update(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/result')
    return render(request,'apps/update.html',{'s':student})



# Create your views here.
