# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from .forms import ContactForm

def hello(request):
    return HttpResponse('hello world')

def template_test(request):
    return render_to_response('employee/list.html', {'response_key' : 'response key value hurray'},
                              context_instance=RequestContext(request))
    
def form_test(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponse('Test Complete') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('employee/detail.html',
                              {'form': form,},
                              context_instance=RequestContext(request))