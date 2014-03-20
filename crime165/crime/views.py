from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


from django.template import Context
from django.template.loader import get_template
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template import RequestContext

from crime.models import CategoryForm
 
#from crime.forms import CategoryForm
 
 
def addCategory(request):
    	if request.method == 'GET':
        	form = CategoryForm()
    	else:
       	        form = CategoryForm(request.POST)
	         
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('addCategory')
            
    	
    	return render(request,'crime/addCategory.html', {'form': form})

def index(request, **kwargs):
	
	if request.method == 'GET':
        	form = CategoryForm()
    	else:

        	form = CategoryForm(request.POST)  
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('')
	
    	return render(request,'crime/index.html', {'form': form})
	

#class IndexView(generic.ListView):
#    template_name = 'crime/index.html'
#    context_object_name = 'latest_crime_list'

#    def get_queryset(self):
#        ""Return the last five published polls."""
#        return Crime.objects.order_by('-timedate')[:5]


#class DetailView(generic.DetailView):
#    model = Crime
#    template_name = 'crime/detail.html'


#class ResultsView(generic.DetailView):
#    model = Crime
#    template_name = 'crime/results.html'

#def vote(request, crime_id):
#    model = Crime
#    template_name = 'crime/results.html'
