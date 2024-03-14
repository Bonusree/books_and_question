from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
from books.models import course_title
from questions.models import Session, Course
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
@login_required
def add_question(request):
    if request.method=='POST':
        Course_title = request.POST.get("course_title")
        exam_type = request.POST.get("Exam_type")
        fa= request.POST.get("faculty")
        session = request.POST.get("session")
        pdf_file = request.FILES['pdf_file']
        
        ct,x= course_title.objects.get_or_create(name=Course_title)
        se,s = Session.objects.get_or_create(faculty=fa, date=session,file=pdf_file)      
        ques,ex = Course.objects.get_or_create(Course_title=ct,sessions=se, exam_type=exam_type)
        return redirect('question')
        # except Exception as e:
        #     print(e)
        #     return redirect('question')
    return redirect('question')
def question(request):
    qs=Course.objects.all()

       
    context={'ques':qs}

    return render(request, 'question.html', context)
