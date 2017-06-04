# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Scholarship
from app.models import Student
from app.models import Course
from app.models import Selectcourse


class ScholarshipAdmin(admin.ModelAdmin):
	list_display = ('scholarship_level','money')
admin.site.register(Scholarship,ScholarshipAdmin)

class StudentAdmin(admin.ModelAdmin):
        list_display = ('sid','sname','gender',
			'classes','birthpalce','scholarship_level')
	list_filter = ('classes','scholarship_level')
	search_fields = ['sname','classes','sid','gender']
admin.site.register(Student,StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
        list_display = ('cid','cname','learnhours',
			'credit','precourse')
	search_fields = ['cid','cname']
admin.site.register(Course,CourseAdmin)

class SelectcourseAdmin(admin.ModelAdmin):
	list_display = ('cid','sid','grade')
	search_fields = ['sid__sname','cid__cname']
	list_filter = ('cid','sid')
admin.site.register(Selectcourse,SelectcourseAdmin)

# Register your models here.
