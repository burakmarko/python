from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

from .models import Credit
def index(request):
	return render(request, 'articles/list.html')

def detail(request, article_id):
	'''
	 a = Pil.objects.get(id=pk)
    record = Credit(name=request.POST['name'],
                   text=request.POST['amoumt'])
    record.save()
'''
	'''
	try:
		a= Credit.objects.get(id = article_id)
	except:
		raise Http404("немає =(((")
	'''
	return render(request, 'articles/detail.html')

def test(request):
	return HttpResponse('test')

def get_credit(request,sum):
	sum = Credit.objects.all().annotate(Sum('sum_title'))
	return render(request, 'articles/detail.html',{'sum':sum})

def give_credit(request,data1):
	data1 = Credit.objects.all().annotate('pub_date')
	return render(request, 'articles/detail123.html',{'data1':data1})

def forma_fin(request,ide):
	try:
		a= Credit.objects.get(id = ide)
	except:
		raise Http404("немає =(((")
    record = Credit(credit_title=request.POST['credit_title'],
                   sum_title=request.POST['sum_title'],
                   pub_date=request.POST['pub_date'])
    record.save()
	return render(request, 'articles/forma.html')

def balance(request, ide):
	try:
		a= Credit.objects.get(id = ide)
	except:
		raise Http404("немає =(((")
	
	record = Credit(credit_title=request.POST['credit_title'],
					pub_date= request.POST['pub_date'])

	data2 = Credit.objects.all().annotate('pub_date')
	fund = Credit.objects.all().annotate('sum_title')
	dif =data1-data2
	kist=dif//365
	for i in range(kist):
		fund*=1.3
	fund = request.POST['sum_title']
	record.save()

	return render(request, 'articles/balance.html')

