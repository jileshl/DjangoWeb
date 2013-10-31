# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from .forms import ContactForm


def job_list(request):
    jobs = [{'JobId':9329,
                'Job_title': 'Kamlesh',
                'Max_salary': 'Nitin',
                'Min_salary' : 'Project Manager'
                },
                 {'JobId':333,
                'Job_title': 'Kapil',
                'Max_salary': 'Himali',
                'Min_salary' : 'SE'
                }]
    return render_to_response('Job/JobList.html', {'value': jobs}, context_instance=RequestContext(request))