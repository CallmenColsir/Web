from django.shortcuts import render, redirect
from .models import StudentData


def home(request):
    return render(request, 'Student/home.html', {})

from .forms import StudentCreateForm
def add_student(request):
    form = StudentCreateForm()
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add')
        
    return render(request, 'Student/add-student.html', {'form': form})


def view_student(request):
    
    return render(request, 'Student/view-student.html', {'data': StudentData.objects.all()})


def detail_student(request, id):
    student = StudentData.objects.get(id=id)
    
    return render(request, 'Student/detail-student.html', {'data': student})


def delete_student(request, id):
    if request.method == 'POST':
        d_student = StudentData.objects.get(id=id)
        d_student.delete()
        
        return redirect('/view')
    

def update_form(request, id):
    if request.method == 'POST':
        student = StudentData.objects.get(id=id)
    return render(request, 'Student/update-student.html', {'data': student})

def update_student(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        major = request.POST['major']
        
        StudentData.objects.filter(id=id).update(name=name, age=age, major=major)
        return redirect('/view')