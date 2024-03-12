from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
from books.models import course_title
from questions.models import *
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
@login_required
def add_question(request):
    if request.method=='POST':
        Course_title = request.POST.get("course_title")
        exam_type = request.POST.get("Exam_type")
        faculty = request.POST.get("faculty")
        session = request.user.session
        pdf_file = request.FILES['pdf_file']
            
        ex = Question_bank.objects.filter(session=session, Exam_type=exam_type,
                                            faculty=faculty, pdf_file=pdf_file).exists()

    return redirect('question')
def question(request):
    return render(request, 'question.html')