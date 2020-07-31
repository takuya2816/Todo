from django.contrib import admin
from .models import TodoModel

# Register your models here.

admin.site.register(TodoModel)  # adminにモデルを追加