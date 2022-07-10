from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Information(models.Model):
    title = models.CharField("Название школы", max_length=20)
    backround = models.ImageField("Главный шаблон", blank=False)
    about = models.TextField("О нас",blank=False)
    image_for_about = models.ImageField("фото для информации ", blank=False)
    address = models.CharField("Cтрана и  город", max_length=30,blank=False)
    street = models.CharField("Улица", max_length=30,blank=False)
    email = models.EmailField("Email")
    telephone = models.CharField("Телефон", max_length=15,blank=False)
    whatsapp = models.URLField(verbose_name="ссылка на whatsapp", blank=False)
    instagram = models.URLField(verbose_name="ссылка на instagram", blank=False)
    facebook = models.URLField(verbose_name="ссылка на facebook", blank=False)
    twitter = models.URLField(verbose_name="ссылка на twitter", blank=False)
    map = models.URLField(verbose_name="ссылка на карту", blank=False)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Информация о школе"
        verbose_name_plural = "О школе"

class Benefits(models.Model):
    logo = models.ImageField("логотип", blank=False)
    description = models.TextField(blank=False)
    main = models.ForeignKey(Information, verbose_name="связывать", on_delete=models.CASCADE, related_name="benefits")
    
    def __str__(self):
        return self.description 

    class Meta:
        verbose_name = "Почему нужно выбрать нас?"
        verbose_name_plural = "преимущества"


class License(models.Model):
    title = models.CharField("Описание", max_length=100)
    logo = models.ImageField("Фото лицензии", blank=False)
    school = models.ForeignKey(Information, verbose_name="школа", on_delete=models.CASCADE, related_name="license")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Лицензия и грамоты"
        verbose_name_plural = "Лицензия или грамоты"

class Reviews(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    image = models.ImageField("Фото", blank=False)
    school = models.ForeignKey(Information, verbose_name="школа", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.school}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class SchoolShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="school_shots/")
    school = models.ForeignKey(Information, verbose_name="школа", on_delete=models.CASCADE, related_name="shots")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотографии"


class Questions(models.Model):
    name = models.CharField("Имя", max_length=100)
    telephone = models.CharField("Телефон", max_length=20)
    question= models.TextField("Вопросы", null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.update_at = timezone.now()
        return super(Questions, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вопросы"
        verbose_name_plural = "Вопросы"