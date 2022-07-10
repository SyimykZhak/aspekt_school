from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description=models.TextField("Описание",null=False, blank=False)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Теги для новостей"
        verbose_name_plural = "Теги для новостей"

# News Model
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="news_category")
    title=models.CharField("Тема",max_length=300)
    tagline = models.CharField("Слоган", max_length=500, default=False)
    desccription=models.TextField("Описание",blank=False)
    image=models.ImageField("фото", blank=False)
    add_time=models.DateTimeField("Добавлено в",auto_now_add=True)
    url = models.SlugField(max_length=200, unique=True)
    draft = models.BooleanField("Опубликовать", default=False)

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
