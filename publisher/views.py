from django.shortcuts import render, redirect, HttpResponse
from .models import Publisher, Book, Author


# Create your views here.
def publisher_list(request):
    publisher_all = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_all': publisher_all})


def publisher_add(request):
    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')
        publisher = Publisher.objects.filter(name=publisher_name)
        if not publisher_name:
            errmsg = '输入不能为空'
            return render(request, 'publisher_add.html', {'errmsg': errmsg})
        if publisher:
            errmsg = '您添加的出版社名称已存在'
            return render(request, 'publisher_add.html', {'errmsg': errmsg})
        Publisher.objects.create(name=publisher_name)
        return redirect('/publisher_list/')
    return render(request, 'publisher_add.html')


def publisher_edit(request):
    pk = request.GET.get('pk')

    publisher = Publisher.objects.get(pk=pk)
    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')
        if publisher_name == publisher.name:
            errmsg = '您没做任何修改'
            return render(request, 'publisher_edit.html', {'publisher': publisher, 'errmsg': errmsg})
        if not publisher_name:
            errmsg = '输入不能为空'
            return render(request, 'publisher_edit.html', {'publisher': publisher, 'errmsg': errmsg})
        publisher.name = publisher_name
        publisher.save()
        return redirect('/publisher_list/')
    return render(request, 'publisher_edit.html', {'publisher': publisher})


def publisher_del(request):
    pk = request.GET.get('pk')
    Publisher.objects.filter(pk=pk).delete()
    return redirect('/publisher_list/')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_add(request):
    errmsg = ''
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        publisher_pk = request.POST.get('publisher_pk')
        if not book_name:
            errmsg = '书籍名不能为空'
        elif Book.objects.filter(name=book_name):
            errmsg = '书籍已存在'
        else:
            Book.objects.create(name=book_name, publisher_id=publisher_pk)
            return redirect('/book_list/')
    publishers = Publisher.objects.all()
    return render(request, 'book_add.html', {'publishers': publishers, 'errmsg': errmsg})


def book_edit(request):
    pk = request.GET.get('pk')
    book_obj = Book.objects.get(pk=pk)
    book_name = request.GET.get('book_name')
    publishers = Publisher.objects.all()
    return render(request, 'book_edit.html', {'book_obj':book_obj, 'publishers':publishers})


def book_del(request):
    pk = request.GET.get('pk')
    Book.objects.get(pk=pk).delete()
    return redirect('/book_list')


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors':authors})