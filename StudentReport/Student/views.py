from django.shortcuts import render, redirect
from .models import StudentData
from .forms import StudentCreateForm

def home(request):
    return render(request, 'Student/home.html', {})


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
