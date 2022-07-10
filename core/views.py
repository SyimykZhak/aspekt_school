from django.shortcuts import redirect, render
from django.views.generic import ListView, View
from .models import *
from .form import QuestionForm
from django.contrib import messages
# Create your views here.

class MainListView(ListView):
    model = Information
    template_name ='core/main.html'
    context_object_name = "main"

class ContactListView(ListView):
    model = Information
    template_name ='core/contact.html'
    context_object_name = "contacts"

class QustionsView(View):
    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш вопрос принять!!')
        else:
            messages.error(request, 'Ваш вопрос не принять, введите данных правильно!!')
        return redirect("/")
    

def handle_not_found(request, exception):
    return render(request, 'core/not-found.html')