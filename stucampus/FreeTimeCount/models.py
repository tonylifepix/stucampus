#-*- coding: utf-8
from django.db import models

# Create your models here.

class Member(models.Model):

	class Meta:
		permissions = (
			('usable', u'查看成员空闲时间'),
		)



	stuID 			= models.CharField(max_length=20)
	'''name 			= models.CharField(max_length=20)
	grade	 		= models.CharField(max_length=20)
	sex 			= models.CharField(max_length=20)
	department 		= models.CharField(max_length=20)
	stuID 			= models.CharField(max_length=20)
	dormitory		= models.CharField(max_length=20)
	phone_num_long 	= models.CharField(max_length=20)
	phone_num_short = models.CharField(max_length=20)
	birthday 		= models.DateField()
	is_work 		= models.IntegerField()
	qq 				= models.CharField(max_length=20)
	wechat 			= models.CharField(max_length=20)
	#photo 			= models.ImageField()'''

	def __str__(self):
		return self.stuID





class Students(models.Model):
	stu_no			= models.CharField(max_length=32)
	name 			= models.CharField(max_length=32)
	college			= models.CharField(max_length=32)
	major			= models.CharField(max_length=32)
	sex				= models.CharField(max_length=32)

	def __str__(self):
		return self.name

class Course(models.Model):
	course_id		= models.IntegerField()
	weekday 		= models.CharField(max_length=32)
	time 			= models.CharField(max_length=32)
	course_name 	= models.CharField(max_length=32)
	place 			= models.CharField(max_length=32)

	def __str__(self):
		return self.course_name

class CourseTable(models.Model):
	student 		= models.ForeignKey(Students)
	course_id 		= models.IntegerField()
