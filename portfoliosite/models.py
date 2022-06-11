from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False) 
    stack = models.CharField(max_length=150,null=False) 
    description = models.CharField(max_length=200,null=False) 
    live = models.CharField(max_length=100,null=True) 
    github = models.CharField(max_length=100,null=True) 
    image = models.FileField(upload_to='static/assets',null=True)