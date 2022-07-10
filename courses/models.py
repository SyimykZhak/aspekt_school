from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория для курсов"
        verbose_name_plural = "Категории для курсов"

class Teachers(models.Model):
    name = models.CharField("Имя", max_length=100)
    speciality = models.CharField("Специалность", max_length=20)
    age = models.PositiveIntegerField("Возраст", default=0)
    image = models.ImageField("Фото")
    description = models.TextField("Описание")
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'slug': self.name})
    
    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'
        ordering = ['name']

class Coursess(models.Model):
    title = models.CharField("название курса",max_length=255)
    tagline = models.CharField("Слоган", max_length=100, default='')
    image = models.ImageField(blank=False)
    price = models.IntegerField(default=0)
    description = models.TextField(null=False, blank=False) 
    teacher = models.ManyToManyField(Teachers, verbose_name="преподаватель", related_name="course_teachers")
    time = models.IntegerField("длительность одного урока(в часах)",default=0)
    term = models.IntegerField("срок(в месяцах)",default=0)
    modul = models.IntegerField("модуль",default=0)
    created_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Опубликовать", default=False)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ['title']

class Group(models.Model):
    start_time = models.TimeField("Начало урока")
    end_time = models.TimeField("Конец урока")
    teacher = models.CharField("преподаватель", max_length=20,blank=True)
    course = models.ForeignKey(Coursess,verbose_name="курс",on_delete=models.CASCADE,blank=True, related_name="course_name")
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы для курсов"



class Register(models.Model):
    name = models.CharField("Имя", max_length=100)
    lastname = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Email")
    telephone = models.CharField("Телефон", max_length=25)
    goal = models.CharField("Цель изучения",max_length=255)
    group = models.CharField("Группа", max_length=100)
    course = models.ForeignKey(Coursess, verbose_name="Курс", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.update_at = timezone.now()
        return super(Register, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Зарегистрированные"