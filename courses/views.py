from django.views.generic import ListView, DeleteView, View
from .models import *
from django.shortcuts import redirect
from .form import UserForm
from django.contrib import messages
# Create your views here.

class CoursesListView(ListView):
    model = Coursess
    template_name ='courses/courses.html'
    context_object_name = "courses"
    queryset = Coursess.objects.filter(draft = False)
    ordering = ['-update_at']
    paginate_by = 10

class CoursesDetailView(DeleteView):
    model = Coursess
    template_name ='courses/course.html'
    context_object_name = "course"
    slug_field = "url"

class RegisterView(View):
    def post(self, request,pk):
        form = UserForm(request.POST)
        course = Coursess.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.course = course
            form.save()
            messages.success(request, 'Успешно зарегистрировались к курсу!!')
        else:
            messages.error(request, 'Вы не зарегистрировались, введите данных правильно!!!')
        return redirect("coursess")