from django.contrib import admin
from .models import *
from student.models import *
from import_export.admin import ImportExportMixin

# Register your models here.



class UserQualification(admin.TabularInline):
    model = StudentQualification
    extra = 0


class UserResume(admin.TabularInline):
    model = Resume 
    extra = 0


class UserAdmin(ImportExportMixin,admin.ModelAdmin):
    inlines = [UserQualification, UserResume]
    list_display = ['username','email','phone_number','is_superuser','is_staff','is_active']
    list_filter = ['username','email','phone_number','is_superuser','is_staff','is_active']
    search_fields = ['username','email','phone_number','is_superuser','is_staff','is_active']
    list_editable = ['is_staff','is_active']
    list_max_show_all = 10
    list_per_page = 20  
    
admin.site.register(User,UserAdmin)



@admin.register(ContactDetails)
class ContactDetailAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(ImportExportMixin,admin.ModelAdmin):
    pass

@admin.register(Addres)
class AddresAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscriber)
class SubAdmin(admin.ModelAdmin):
    pass