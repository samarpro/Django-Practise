from django.contrib import admin
from .models import TodoLists,Tasks,FileUpload
# Register your models here.
admin.site.register(TodoLists)
admin.site.register(Tasks)
admin.site.register(FileUpload)