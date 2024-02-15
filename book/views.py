from django.shortcuts import render
from . import models


def book_store(request):
    if request.method == 'GET':
        book = models.Book.objects.all()
        return render(request, template_name='book.html',
                      context={'book': book})
