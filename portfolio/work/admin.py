from django.contrib import admin
from .models import Work

# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    model = Work
    list_display = ["title","url"]
