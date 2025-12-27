from django.db import models
from django.contrib.auth.models import User

class PortfolioWork(models.Model):
    title = models.CharField('Название работы', max_length=200)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='works/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    user_name = models.CharField('Имя заказчика', max_length=100)
    user_email = models.EmailField('Email заказчика')
    description = models.TextField('Детали заказа')
    status = models.CharField(
        'Статус', 
        max_length=50,
        choices=[
            ('new', 'Новый'),
            ('in_progress', 'В работе'),
            ('completed', 'Выполнен'),
            ('cancelled', 'Отменён')
        ],
        default='new'
    )
    created_at = models.DateTimeField('Дата заказа', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return f"Заказ {self.id} от {self.user_name}"

class SocialLink(models.Model):
    platform = models.CharField('Платформа', max_length=50)
    url = models.URLField('Ссылка')
    icon_class = models.CharField('Класс иконки', max_length=100, blank=True)

    def __str__(self):
        return self.platform

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.subject}"    
