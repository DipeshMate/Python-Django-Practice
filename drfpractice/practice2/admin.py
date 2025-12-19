from django.contrib import admin
from practice2.models import EmpModel
# Register your models here.

class empAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','gender')

admin.site.register(EmpModel,empAdmin)

# user & pass = empadmin


