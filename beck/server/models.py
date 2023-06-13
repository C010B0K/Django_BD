from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Price(models.Model):
    price = models.CharField(max_length=5)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.price


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=255)
    whats = models.CharField(max_length=12)
    inst = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Photo(models.Model):
    photo = models.ImageField(upload_to='images', null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.photo.url}" width = "300"/>')
    img_preview.short_description = 'Изображение'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def img_preview_list(self):
        return mark_safe(f'<img src = "{self.photo.url}" width = "100"/>')

    img_preview_list.short_description = 'Изображение'

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)