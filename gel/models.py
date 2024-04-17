from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    

class location(models.Model):
    cep = models.CharField(unique=True,max_length=8)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(blank=True,max_length=5)
    bairro = models.CharField(blank=True,max_length=30)
    municipio = models.CharField(blank=True,max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    show = models.BooleanField(default=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.cep

class faq(models.Model):
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    location = models.ForeignKey(
        location,
        on_delete=models.SET_NULL,
        null=True
        )

    category = models.ForeignKey(
        category,
        
        on_delete=models.SET_NULL,
        null=True
    
        
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.description