import datetime
from django.db import models

# Create your models here.
class Credit(models.Model):
	article_title = models.CharField('ім\'я', max_length = 200)
	article_text  = models.TextField('кількість коштів')
	pub_date =models.DateTimeField('дата')
	def __str__(self):
		return self.article_title


'''
class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name =models.CharField('ім\'я', max_length = 200)
	comment_text = models.CharField('text commect', max_length =200)
	def __str__(self):
		return self.author_name
'''
