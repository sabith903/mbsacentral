from django.contrib import admin
from .models import Category, Program, Result, Stage, Team, Student

admin.site.register(Program)
admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Stage)
admin.site.register(Result)
