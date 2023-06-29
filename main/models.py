from django.db import models

# Create your models here.
class TodoLists(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name;

class Tasks(models.Model):
    todolist = models.ForeignKey(TodoLists,on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    stat = models.BooleanField()

    def __str__(self): 
        return self.task
    
class FileUpload(models.Model):
    text = models.CharField(max_length=255)
    fil = models.FileField(upload_to="word",max_length=250,null=True,default=None)

