from django.shortcuts import render, redirect
from .models import Book
from .forms import BorrowedBookForm

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

def book_list(request):
    books = Book.objects.all
    if request.method == 'POST':
        form = BorrowedBookForm(request.POST)
        if form.is_valid():
            book_id = request.POST.get('book_id')
            book = Book.objects.get(id=book_id)
            book.borrowed_by = form.cleaned_data['borrowed_by']
            book.due_date = form.cleaned_data['due_date']
            book.save()

            return redirect('book_list')
    else:
        form = BorrowedBookForm
    return render(request, 'books/book_list.html', {'books': books, 'form': form})