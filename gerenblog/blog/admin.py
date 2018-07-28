from django.contrib import admin
from .models import Blog,BlogType
# Register your models here.

@admin.register(BlogType)
class BlogType(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','type_name','author','read_datails','created_time','last_update_time')