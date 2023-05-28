from django.contrib import admin
from .models import *



admin.site.site_header = 'QuizApp'
admin.site.site_title = 'QuizApp'
admin.site.index_title = 'QuizApp.com'


class RegisterAdmin(admin.ModelAdmin):
    list_display= ["id","name","mobile_no","email","city","created_date"]
    search_fields=["name","mobile_no","city","email"]
    list_filter = ["name","created_date"]
    list_display_links = ("name","mobile_no","email","city","created_date")
    
admin.site.register(Register,RegisterAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display= ["question","cr_date"]
    search_fields=["question","answer"]
    list_filter = ["cr_date"]
    list_display_links = ("question","cr_date")
    readonly_fields = ("answer_hidden",)

admin.site.register(Question,QuestionAdmin)

class SubmitAnswerAdmin(admin.ModelAdmin):
    list_display= ["name","score","cr_date"]
    search_fields=["name","score","cr_date"]
    list_filter = ["cr_date"]
    list_display_links = ("name","score","cr_date")
    readonly_fields = ("name","score")

admin.site.register(SubmitAnswer,SubmitAnswerAdmin)