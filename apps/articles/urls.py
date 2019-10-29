from django.urls import path
from django.conf.urls import url
from . import views

app_name= 'articles'
urlpatterns = [
	path('', views.index, name= 'index'),
	url(r'^getcredit',views.get_credit,name = 'credit'),
	url(r'^givecredit',views.give_credit,name = 'credit22'),
	url(r'^forma',views.forma_fin,name = 'forma123'),

	# url(r'^getcredit/forma',views.forma,name = 'forma'),
	
]