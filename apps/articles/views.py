from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .models import Credit
def index(request):
	return render(request, 'articles/list.html')

def detail(request, article_id):
	 a = Pil.objects.get(id=pk)
    record = Credit(name=request.POST['name'],
                   text=request.POST['amoumt'])
    record.save()

	'''
	try:
		a= Credit.objects.get(id = article_id)
	except:
		raise Http404("немає =(((")
	'''
	return render(request, 'articles/detail.html')

def test(request):
	return HttpResponse('test')

def get_credit(request):
	return render(request, 'articles/detail.html')

def give_credit(request):
	return render(request, 'articles/detail123.html')

def forma_fin(request):
	return render(request, 'articles/forma.html')

