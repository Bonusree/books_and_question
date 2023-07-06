from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
from books.models import available_books, need_books, course_title

User = get_user_model()

def add_available_books(request):
    if request.method == 'POST':
        Course_title = request.POST.get("course_title")
        books_name = request.POST.get("book_name")
        owner_name = request.user.get_full_name()
        writer_name = request.POST.get("writer_name")
        roll = request.user.roll
        session = request.user.session
        ex = available_books.objects.filter(books_name=books_name, owner_name=owner_name,
                                            writer_name=writer_name, roll=roll, session=session).exists()

        print(ex)
        context = {'review': '', 'msg': ''}
        if ex:
            context = {'review': 'no', 'msg': 'It has already been added'}
            return render(request, 'books.html', context=context)
        else:
            try:
                ct,x= course_title.objects.get_or_create(name=Course_title)
               
                books = available_books(Course_title=ct,books_name=books_name, owner_name=owner_name,
                                        writer_name=writer_name, roll=roll, session=session)
                books.save()
                # Assign the course_title using set()

                context = {'review': 'yes', 'msg': 'Added successfully'}
            except Exception as e:
                print(e)
                context = {'review': 'no', 'msg': 'An error occurred while saving the book'}

        return render(request, 'books.html', context=context)

    return redirect('books')

def add_need_books(request):
    if request.method=='POST':
        Course_title=request.POST.get("course_title")
        books_name=request.POST.get("book_name")
        borrower_name=request.user.get_full_name()
        writer_name=request.POST.get("writer_name")
        roll=request.user.roll
        session=request.user.session
        
        ex=need_books.objects.filter( books_name=books_name,borrower_name=borrower_name,
                                        writer_name=writer_name,roll=roll,session=session).exists()
                
        context={'review':'','msg':''}
        if ex:
                context={'review':'no', 'msg':'it has already added'}
        else:
            try:
                ct,x= course_title.objects.get_or_create(name=Course_title)
               
                books = need_books(Course_title=ct,books_name=books_name, borrower_name=borrower_name,
                                        writer_name=writer_name, roll=roll, session=session)
                books.save()
                # Assign the course_title using set()

                context = {'review': 'yes', 'msg': 'Added successfully'}
            except Exception as e:
                print(e)
                context = {'review': 'no', 'msg': 'An error occurred while saving the book'}
        return render(request, 'books.html', context=context)

    
    return redirect(request, 'books') 

def books_overview(request):
    allBooks=available_books.objects.all()
    title=course_title.objects.all()
    
    books={}
    for t in title:
        books.update({t.name:{'available':[],'need':[]}})
       
    for b in allBooks:
        ct=b.Course_title.name
        a={'b_name':b.books_name, 'owner_name':b.owner_name,
           'writer_name':b.writer_name, 'roll':b.roll, 'session':b.session}
       # print(a)
        if ct in books:
            books[ct]['available'].append(a)
        #print(books[ct]['available'])
    needbooks=need_books.objects.all()
    for b in needbooks:
        ct=b.Course_title.name
        a={'b_name':b.books_name, 'borrower':b.borrower_name,
           'writer_name':b.writer_name, 'roll':b.roll, 'session':b.session}
        if ct in books:
            books[ct]['need'].append(a)
    print(books)
    #b={'available':books['available'],'need':books['need']}
    return render(request, 'books.html', context={'books': books})

