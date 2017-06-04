# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Scholarship(models.Model):
        scholarship_level = models.CharField(primary_key=True,max_length=10)
        money = models.IntegerField()
	
	def __unicode__(self):
		return self.scholarship_level

class Student(models.Model):
	sid = models.IntegerField(primary_key=True)
	sname = models.CharField(max_length=20)
	gender = models.CharField(max_length=20)
	classes = models.CharField(max_length=20)
	birthpalce = models.CharField(max_length=20)
	scholarship_level = models.ForeignKey(Scholarship,blank=True,null=True)
	
	def __unicode__(self):
                return str(self.sid)

class Course(models.Model):
        cid = models.CharField(primary_key=True,max_length=15)
        cname = models.CharField(max_length=20)
        learnhours = models.IntegerField()
	credit = models.FloatField()
	precourse = models.CharField(max_length=20,blank=True,null=True)

	def __unicode__(self):
                return str(self.cid)

class Selectcourse(models.Model):
	sid = models.ForeignKey(Student)
	cid = models.ForeignKey(Course)
	grade = models.FloatField()

	class Meta:
		unique_together = ('sid', 'cid')
