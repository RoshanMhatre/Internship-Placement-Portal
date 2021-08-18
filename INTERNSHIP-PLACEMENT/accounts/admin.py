from django.contrib import admin

# Register your models here.
from .models import studentUser, companyUser


class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'yourname', 'email', 'branch',
                    'yog', 'contact', 'stuImage')


admin.site.register(studentUser, StudentAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('username', 'companyname', 'companyemail',
                    'address', 'contact', 'comImage')


admin.site.register(companyUser, CompanyAdmin)
