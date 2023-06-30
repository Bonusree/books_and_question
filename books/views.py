from django.shortcuts import render,HttpResponse
from django.contrib.auth import get_user_model

from books.models import available_books,need_books
User = get_user_model()

# Create your views here.
def add_available_books(request):
    if request.method=='POST':
        
        Course_title=request.POST.get("course_title")
        books_name=request.POST.get("book_name")
        owner_name=request.user.get_full_name()
        writer_name=request.POST.get("writer_name")
        roll=request.user.id
        session=request.user.session
        ex=available_books.objects.filter(Course_title=Course_title, books_name=books_name,owner_name=owner_name,
                                writer_name=writer_name,roll=roll,session=session).exists()
        
            
        context={'review':'','msg':''}
        if ex:
            context={'review':'no', 'msg':'it has already added'}
        else:
            try:
                books=available_books(Course_title=Course_title, books_name=books_name,owner_name=owner_name,
                                    writer_name=writer_name,roll=roll,session=session)
                
                books.save()
                context={'review':'yes', 'msg': 'added successfully'}
            except:
                context={'review':'no', 'msg': 'try again, something went wrong'}
        return render(request, 'books.html', context=context)
    return render(request, 'books.html')

def add_need_books(request):
    if request.method=='POST':
        Course_title=request.POST.get("course_title")
        books_name=request.POST.get("book_name")
        borrower_name=request.user.get_full_name()
        writer_name=request.POST.get("writer_name")
        roll=request.user.id
        session=request.user.session
        
        ex=need_books.objects.filter(Course_title=Course_title, books_name=books_name,borrower_name=borrower_name,
                                        writer_name=writer_name,roll=roll,session=session).exists()
                
        context={'review':'','msg':''}
        if ex:
                context={'review':'no', 'msg':'it has already added'}
        else:
                context={'review':'','msg':''}
                try:
                    books=need_books(Course_title=Course_title, books_name=books_name,borrower_name=borrower_name,
                                        writer_name=writer_name,roll=roll,session=session)
                    
                    books.save()
                    context={'review':'yes', 'msg': 'added successfully'}
                except:
                    context={'review':'no', 'msg': 'try again, something went wrong'}
        return render(request, 'books.html', context=context)

    
    return render(request, 'books.html') 

def books_overview(request):
    allBooks=available_books.objects.all()
    context={'available':[], 'need':[]}
    for b in allBooks:
       books={'books_name':b.books_name,'course_title':b.Course_title,
              'writter_name':b.writer_name,'owner_name':b.owner_name,'session':b.session,
              'roll':b.roll} 
       context['available'].append(books)
    needbooks=need_books.objects.all()
    for a in needbooks:
        books={'books_name':a.books_name,'course_title':a.Course_title,
              'writter_name':a.writer_name,'borrower_name':a.borrower_name,'session':a.session,
              'roll':a.roll} 
        context['need'].append(books)
    return render(request, 'books.html', books=context)