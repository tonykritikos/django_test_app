from django.contrib import admin

# Register your models here.
from .models import Question, Choice


# @admin.register(Question, site=admin.site)
class QuestionAdmin(admin.ModelAdmin):
    pass
    # list_display = []
    # list_display_links = (, )
    # fields = []


# @admin.register(Choice, site=admin.site)
class ChoiceAdmin(admin.ModelAdmin):
    pass
    # list_display = []
    # list_display_links = (, )
    # fields = []


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)