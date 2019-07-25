from django.shortcuts import render
from .models import Book
# Create your views here.

def detail(request):
	book_list = Book.objects.order_by('-pub_date')[:5]
	context = {'book_list':book_list}
	return render(request,'lib/detail.html',context)
