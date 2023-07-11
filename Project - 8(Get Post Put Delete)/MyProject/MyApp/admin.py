from django.contrib import admin
from .models import StudentModel
# Register your models here.
@admin.register(StudentModel)
class AdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'course']

    @admin.display(description='name')
    def cn_name(self, obj):
        return obj
    
