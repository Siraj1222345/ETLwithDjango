from django.db import models

class Sstudent(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()

    class Meta:
        managed = False
        app_label = 'Sstudent'
        db_table = 'Sstudent'

class Dstudent(models.Model):
    fullname = models.CharField(max_length=100)
    dob = models.DateField()

    class Meta:
        managed = False
        app_label = 'Dstudent'
        db_table = 'dstudent'
