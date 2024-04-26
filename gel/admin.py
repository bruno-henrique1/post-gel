from django.contrib import admin

# Register your models here.

from .models import category, location, faq
from .forms import RegisterForm

@admin.register(faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = 'id', 'description', 'created_date',"location","category","owner",
    list_display_links = 'description',
    search_fields = 'id', 'description', 'location',
    ordering = 'id',

@admin.register(location)
class LocationAdmin(admin.ModelAdmin):
    list_display = 'id', 'bairro', 'cep',"endereco","numero","municipio","created_date","show","owner"
    list_display_links = 'bairro',
    search_fields = 'id', 'bairro', 'cep',
    ordering = 'id',


@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'name',
    search_fields = 'id', 'name',
    ordering = 'id',

# admin.site.register(location)
# admin.site.register(category)
# admin.site.register(faq)

