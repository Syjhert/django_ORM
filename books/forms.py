from django import forms
from .models import Book

class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['borrowed_by', 'due_date']