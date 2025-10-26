from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category (models.Model):
#config metadatas
    # class Meta:
    #     verbose_name = 'Category'
    #     verbose_name_pluraç = 'Categories' 

    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Contact (models.Model):
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show =  models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') #This path is automatic create folder in media that config in settings
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    owner =  models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, #CASCADE APAGA TUDO
        blank=True, null=True
        )

    def __str__(self):
        return f'{self.firts_name} {self.last_name}'

