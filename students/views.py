from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def create_idcard(request):
    if request.method=="POST":
        form=StudentForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect("student_cards")
    else:
        form=StudentForm()
    return render(request, 'students/student_form.html', {'form':form})

def student_cards(request):
    students=Student.objects.all()
    return render(request, 'students/student_cards.html', {'students':students})