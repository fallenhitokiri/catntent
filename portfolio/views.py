from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from portfolio.models import Project


def home(request):
    ci = RequestContext(request)
    tmpl = {
        'projects': Project.public.all()
    }
    return render_to_response('portfolio/home.html', tmpl, ci)


def project(request, id, slug):
    ci = RequestContext(request)
    tmpl = {
        'project': get_object_or_404(Project.public, id=id)
    }
    return render_to_response('portfolio/project.html', tmpl, ci)
