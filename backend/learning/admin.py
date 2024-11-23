from django.contrib import admin
from .models import Tome, Lesson, Word, QuizHistory, QuizScore
# Register your models here.


admin.site.register(Tome)
admin.site.register(Lesson)
admin.site.register(Word)
admin.site.register(QuizHistory)
admin.site.register(QuizScore)
