# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Selectcourse,Student,Scholarship,Course

def grade(request):
#	context = {}
#       	context['hello'] = 'r^grade' 
	return render(request,'grade.html')

def classes(request):
	context = {}
	context['sort']=[]
	total1=0
	total2=0
	count1=0
	count2=0
        for sc in Selectcourse.objects.all():
		if sc.sid.classes=='1班':
			total1 +=sc.grade
			count1 +=1
		else:
			total2 +=sc.grade
			count2 +=1
	context['total1']= total1
	context['average1']= total1/count1	
	context['total2']= total2
        context['average2']= total2/count2
	context['sort'].append(['1班', total1/count1])
	context['sort'].append(['2班', total2/count2])
	context['sort'] = sorted(context['sort'], cmp=lambda x,y:cmp(x[1],y[1]))
	return render(request,'classes.html',context)



def failed(request):
	context = {}
	context['failed']=[]
	for sc in Selectcourse.objects.all():
		if sc.grade < 60:
			sname=sc.sid.sname
			cname=sc.cid.cname
			classes=sc.sid.classes
			context['failed'].append([sname,classes,cname,sc.grade])
		else:
			pass
	return render(request,'failed.html',context)

def scholarship(request):
	context = {}
        context['st']=[]
	for st in Student.objects.all():
		if st.scholarship_level is not None:
			money=st.scholarship_level.money
			context['st'].append([st.sname,st.classes,
					      st.scholarship_level,money])
		else:
			pass
	return render(request,'scholarship.html',context)

def all(request):
	context = {}
        context['grade']=[]
	context['single']=[]
        for st in Student.objects.all():
		total=0
		count=0
		for sc in Selectcourse.objects.filter(sid=st.sid):
			total += sc.grade
			count += 1
		average=total/count
		context['grade'].append([st.classes,st.sname,total,average])

	context['higher'] = sorted(context['grade'], cmp=lambda x,y:cmp(x[2],y[2]))[-1]
		
	for single in Course.objects.all():
	        totals=0
        	counts=0
		for sc in Selectcourse.objects.filter(cid=single.cid):
			totals += sc.grade
			counts += 1
		averages=totals/counts
		context['single'].append([single.cname,averages])

	context['higher_average_course'] = sorted(
		context['single'], cmp=lambda x,y:cmp(x[1],y[1]))[-1]

	context['higher_single_course'] = []
	for course in Course.objects.all():
		context['higher_single_course'].append(sorted(Selectcourse.objects.filter(cid=course.cid), cmp=lambda x,y:cmp(x.grade, y.grade))[-1])

	return render(request,'all.html',context)

def test(request):
        context = {}
        total = 0
        count = 0
        for sc in Selectcourse.objects.all():
                total += sc.grade
                count += 1
        context['hello'] = total/count
        return render(request,'hello.html',context)
# Create your views here.

