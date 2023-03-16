from django.db import models

# Create your models here.
class show(models.Model):
 title=models.CharField(max_length=20)
 class Meta:  
        db_table = "web"