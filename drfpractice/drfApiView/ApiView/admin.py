from django.contrib import admin
from ApiView.models import StudentDetail
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','gender')

admin.site.register(StudentDetail, StudentAdmin)
