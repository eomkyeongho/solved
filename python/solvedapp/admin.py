from django.contrib import admin

from solvedapp.models import Solvedapp

# Register your models here.
@admin.register(Solvedapp)
class SolvedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo')

# admin 사이트에서 보여줄 column들 정의
