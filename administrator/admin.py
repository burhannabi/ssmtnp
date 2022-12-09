from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import *
# Register your models here.


@admin.register(Notice)
class NoticeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['title','description','date','course']



@admin.register(Teacher)
class TecherAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name','designation','is_show']
    list_editable = ['is_show']


@admin.register(Event)
class EventAdmin(ImportExportMixin,admin.ModelAdmin):
    pass



@admin.register(Gallery)
class GalleryAdmin(ImportExportMixin,admin.ModelAdmin):
    pass



@admin.register(WhatsappMessage)
class WhatsappMessageAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(WhatsappGroup)
class WhatsappGroupAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(TechnicalStaff)
class TechnicalStaffAdmin(ImportExportMixin,admin.ModelAdmin):
    pass

@admin.register(AboutUs)
class AboutUsAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
