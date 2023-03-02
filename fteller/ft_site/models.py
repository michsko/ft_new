from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
	name = models.CharField('Představení', max_length=120, blank=True)
	date = models.DateTimeField('Datum', blank=True)
	venue = models.CharField('Místo konání', max_length=120, blank=True)
	tickets = models.CharField('Vstupenky', max_length=120, blank=True)
	description = models.TextField('Popis', blank=True)


	def __str__(self):
		return self.name

class Member(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	member_email = models.EmailField('Member Email')


	def __str__(self):
		return self.first_name + ' ' + self.last_name


class ProductionTheater(models.Model):
	name = models.CharField('Představení', max_length=120, blank=True)
	description = models.TextField('Popis', blank=True)
	authors = models.TextField('Autori', blank=True)
	fotoPath = models.TextField('Foto', blank=True)
	def __str__(self):
			return self.name

class ProductionStandup(models.Model):
	name = models.CharField('Představení', max_length=120, blank=True)
	description = models.TextField('Popis', blank=True)
	authors = models.TextField('Autori', blank=True)
	fotoPath = models.TextField('Foto', blank=True)

	def __str__(self):
		return self.name