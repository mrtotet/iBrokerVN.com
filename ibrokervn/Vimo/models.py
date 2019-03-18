from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
"""
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
        
"""


class Vimo(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(User,
                               related_name='Vimo', on_delete=models.CASCADE)
    publish = models.DateField(default=date.today)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    #published = PublishedManager()

    Tenthongtin = models.CharField(max_length=200)
    AH_CHOICES = (
        (0, 'Xấu'),
        (1, 'Tốt'),
        (2, 'Chưa XĐ')
    )
    Anhhuong = models.IntegerField(default=2,
                                   choices=AH_CHOICES
                                   # validators=[MaxValueValidator(1),MinValueValidator(0)]
                                   )

    @staticmethod
    def sohoa(a):
        So = int(a)
        if So == 0:
            color = "red"
        elif So == 1:
            color = "green"
        else:
            color = "yellow"
        return color

    def AH(self):
        return self.sohoa(self.Anhhuong)

    @staticmethod
    def sohoa1(a):
        So = int(a)
        if So == 0:
            anhhuong = "Xấu"
        elif So == 1:
            anhhuong = "Tốt"
        else:
            anhhuong = "~~"
        return anhhuong

    def anh_huong(self):
        return self.sohoa1(self.Anhhuong)

    Mucdo = models.IntegerField(default=0,
                                validators=[MaxValueValidator(100),
                                            MinValueValidator(0)])

    CP_anhhuong = models.CharField(max_length=200)
    ConAH_CHOICES = (
        (0, 'Hết AH'),
        (1, 'Còn AH'),
    )
    DangAH = models.IntegerField(default=1,
                                 choices=ConAH_CHOICES
                                 # validators=[MaxValueValidator(1),MinValueValidator(0)]
                                 )

    @staticmethod
    def sohoa3(a):
        So = int(a)
        return So

    def dang_AH(self):
        return self.sohoa3(self.DangAH)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.Tenthongtin


# Theo doi viewed tren cac trang
class Viewed(models.Model):
    viewed_list_Vimo = models.IntegerField(default=0)


