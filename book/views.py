from django.shortcuts import render
from .models import BooK


def book(request):
    book_list = BooK.objects.all()
    return render(request, "book.html", {"book_list": book_list})
