from django.db import models

class Catagory(models.Model):
	"""docstring for Catagory"""
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	def __str__(self):
		return self.name


class Project(models.Model):
	"""A basic project type"""
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	code_location = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date published')
	catagory = models.ForeignKey(Catagory)
	def __str__(self):
		return self.name


class Update(models.Model):
	"""docstring for Update"""
	project = models.ForeignKey(Project)
	subject = models.CharField(max_length=200)
	update_date = models.DateTimeField('date of update')
	description = models.CharField(max_length=1000)
	def __str__(self):
		return self.subject


