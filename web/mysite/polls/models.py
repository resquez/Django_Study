from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'member'