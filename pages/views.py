from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from pages.models import Page


def index(request):
    '''option for default index page - not implemented'''
    ci = RequestContext(request)
    tmpl = {
        'content': get_object_or_404(Page, name="index")
    }
    return render_to_response('pages/index.html', tmpl, ci)


def page(request, id, slug):
    ci = RequestContext(request)
    tmpl = {
        'content': get_object_or_404(Page, id=id)
    }
    return render_to_response('pages/page.html', tmpl, ci)
