from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.utils import DatabaseError
# Create your views here.
def home(request):
    return render(request, 'home.html')

def question(request):
    return render(request, 'question.html')
def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        roll=request.POST.get('ID')
        session=request.POST.get('session')
        context={'type':'error','message':''}
        # if User.objects.filter(id=id).exists():
        #     context['message']="Already registered  with this ID"
        #     return render(request,'signup.html',context=context)
        user=User.objects.create_user(username=name, roll=roll,session=session)
        user.save()
        login(request,user)
        return redirect( 'home')
    return render(request, 'signup.html')
def login_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        roll=request.POST.get('ID')
        context={'type':'error','message':''}
        user=authenticate(request,username=name,roll=roll)
        print(user)
        if user is not None:
            login(request,user)
            context = {'type':'success','message':'Successfully you are logged in.'}
            return redirect('home')
            
            
        context['message']="you have to signup before login"
        return render(request, 'signup.html', context=context)
    return render(request, 'login.html')
def LogoutPage(request):
    logout(request)
    context = {'type':'success','message':'You are logout'}
    return redirect('login')