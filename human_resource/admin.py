from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
# Register your models here.


@admin.register(Job)
class JobAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(SendMail)
class SendMailAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(TraningApplication)
class TableApplicationAdmin(admin.ModelAdmin):
    model = TraningApplication
    extra = 0


class TableAdmin(admin.TabularInline):
    model = Traning
    extra = 0

    
@admin.register(TraningCategory)
class AdminTraning(admin.ModelAdmin):
    inlines = [TableAdmin]
    