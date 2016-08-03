from django.shortcuts import render

from django.template import loader, Context, RequestContext
from dbapp.models import Person
from dbapp.forms import PersonForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def insert(request):
	if request.method=='GET':
		form = PersonForm()
	else:
		form = PersonForm(request.POST)
	#if request.method == 'POST':
		if form.is_valid():
			name = form.cleaned_data['name']
			phone = form.cleaned_data['phone']
			age = form.cleaned_data['age']
			p = Person.objects.create(name=name, phone = phone, age = age)
			print name,phone,age
			return HttpResponseRedirect('/db/show/')
			#p.save()
	# t = loader.get_template('insert.html')
	# c = RequestContext(request)
	#return HttpResponse(t.render(c))
	return render(request, 'insert.html', { 'form':form })
 
def show(request):
	query_results = Person.objects.all()
	return render (request,'show.html',{'query_results': query_results})

def delete(request, person_id):
	p = Person.objects.get(pk=person_id)
	p.delete()
	return HttpResponseRedirect('/db/show/')


def edit_favorites(request):
	# if request.is_ajax():
	# 	message = "Yes, AJAX"
	# else:
	# 	message = "Not Ajax"
	# return HttpResponse(message)
	# # if request.POST:
	# # 	name = request.POST['name']
	# # 	age = request.POST['age']
	# # 	message = "yes, got it"
	return render(request,'chek.html',{})


def edit(request, person_id):
	p = Person.objects.get(pk=person_id)
	#usr = Person(name = request.name)
	lform = PersonForm({'name': p.name, 'phone': p.phone, 'age': p.age }) # (..., request.FILES or None, p ) also used
	# if request.method =='POST':
	# 	if form.is_valid():
	# 		form.save()
	# 		return HttpResponseRedirect('/db/show')	
	# p.phone = form.cleaned_data['phone']
	# p.age = form.cleaned_data['age']
	if request.method=='POST':
		p.name = request.POST['name']
		p.phone = request.POST['phone']
		p.age = request.POST['age']
		p.save()
		return HttpResponseRedirect('/db/show')      #2
	t = loader.get_template('insert.html')
	c = RequestContext(request,{'form': lform})
	return HttpResponse(t.render(c)
	#return render (request, 'insert.html',{'form':lform})

# added new items for merging
# testing files here
