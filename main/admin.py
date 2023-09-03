
from django.contrib import admin
from .models import Filter
# Register your models here.


class FilterAdmin(admin.ModelAdmin):
    list_display = ['slug']

admin.site.register(Filter, FilterAdmin)