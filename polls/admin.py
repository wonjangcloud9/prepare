from django.contrib import admin

# Register your models here.

from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject']}),
        ('Question information', {'fields': ['content']}),
        ('Date information', {'fields': ['create_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
