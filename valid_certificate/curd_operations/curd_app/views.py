from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from curd_app.models import  Students


def index(request):
    students = Students.objects.all()
    return render(request, 'curd_app/index.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        Students.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age'],
            address=request.POST['address']
        )
        return redirect('index')
    return render(request, 'curd_app/student_form.html')

def student_update(request, id):
    student = get_object_or_404(Students, id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.address = request.POST['address']
        student.save()
        return redirect('index')
    return render(request, 'curd_app/student_form.html', {'student': student})

def student_delete(request, id):
    student = get_object_or_404(Students, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('index')
    return render(request, 'curd_app/student_confirm_delete.html', {'student': student})


# Create your views here.
