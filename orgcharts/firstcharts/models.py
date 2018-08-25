import datetime

from django.db import models

from django.utils import timezone

# Create your models here.
# class Users(models.Model):
# 	name = models.CharField(max_length=200)
# 	organisation = 
# 	linkedin_id


class Users(models.Model):
	full_name = models.CharField(max_length=200)
	org_name = models.CharField(max_length=100)
	linkedin = models.CharField(max_length=200)
	date_added = models.DateField()
	def __str__(self):
		return self.full_name

class Organisations(models.Model):
	org_name = models.CharField(max_length=200)
	linkedin = models.CharField(max_length=200)
	# date_added = models.DateField()
	def __str__(self):
		return self.full_name

class Relationships(models.Model):
	junior = models.ForeignKey(Users, on_delete=models.CASCADE)
	senior = models.ForeignKey(Users, on_delete=models.CASCADE)
	date_added = models.DateField()
	def __str__(self):
		return self.junior

