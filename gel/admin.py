from django.contrib import admin

# Register your models here.

from .models import category, location, faq

admin.site.register(category)
admin.site.register(location)
admin.site.register(faq)