from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
# Register your models here.





@admin.register(ApplyForJob)
class ApplyForJobAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['user','job','date','interview_start_time','interview_end_time','application_status']
    search_fields =  ['user','job','date','interview_start_time','interview_end_time','application_status']
    list_editable = ['date','interview_start_time','interview_end_time','application_status']
    