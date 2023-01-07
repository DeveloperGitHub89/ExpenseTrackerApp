from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=10)
    class Meta:
        db_table='user'

class Expense(models.Model):
    date=models.DateField()
    time=models.TimeField()
    remarks=models.CharField(max_length=300)
    amount=models.FloatField()
    category=models.CharField(max_length=40)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='expense'

class Income(models.Model):
    date=models.DateField()
    time=models.TimeField()
    remarks=models.CharField(max_length=300)
    amount=models.FloatField()
    category=models.CharField(max_length=40)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='income'