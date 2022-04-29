from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice

admin.site.register(Question) # this will help us to modify the models in the admins side board
admin.site.register(Choice)