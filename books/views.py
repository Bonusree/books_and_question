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
                ct,_= course_title.objects.get_or_create(name=Course_title)
               
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
                context={'review':'','msg':''}
                ct=course_title.objects.filter(Course_title=Course_title).exists()
                if not ct:
                    c=course_title(Course_title=Course_title)
                    c.save()
                try:
                    books=need_books(Course_title=Course_title, books_name=books_name,borrower_name=borrower_name,
                                        writer_name=writer_name,roll=roll,session=session)
                    
                    books.save()
                    context={'review':'yes', 'msg': 'added successfully'}
                except:
                    context={'review':'no', 'msg': 'try again, something went wrong'}
        return render(request, 'books.html', context=context)

    
    return redirect(request, 'books') 

def books_overview(request):
    allBooks=available_books.objects.all()
    title=course_title.objects.all()
    
#     books={[]:{'available':[], 'need':[]}}
#     for ct in title:
        
    # for b in allBooks:
    #     bks['course_title'].append(b.Course_title)
    #     for c in 
        
    #     for bn in b.books_name:
    #        book['books_name'].append(bn)
    #     for bn in b.writer_name:
    #        book['writter_name'].append(bn)
    #     for bn in b.owner_name:
    #        book['owner_name'].append(bn)
    #     for bn in b.session:
    #        book['session'].append(bn)
    #     for bn in b.roll:
    #        book['roll'].append(bn)
    #     bks['course_title'['available']].append(book)
    # needbooks=need_books.objects.all()
    # for b in needbooks:
    #     print(b.books_name)
    #     book={'books_name':[],'writter_name':[],'owner_name':[],'session':[],
    #           'roll':[]} 
    #     for bn in b.books_name:
    #        book['books_name'].append(bn)
    #     for bn in b.writer_name:
    #        book['writter_name'].append(bn)
    #     for bn in b.owner_name:
    #        book['owner_name'].append(bn)
    #     for bn in b.session:
    #        book['session'].append(bn)
    #     for bn in b.roll:
    #        book['roll'].append(bn)
    #     bks['course_title'['need']].append(book)
    # #b={'available':books['available'],'need':books['need']}
    return render(request, 'books.html')

