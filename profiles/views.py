from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404


def home(request):
    ci = RequestContext(request)
    tmpl = {}
    return render_to_response('profiles/home.html', tmpl, ci)


def detail(request, id, last_name, first_name):
    ci = RequestContext(request)
    tmpl = {
        'user': get_object_or_404(User, id=id, last_name=last_name, first_name=first_name)
    }
    return render_to_response('profile/detail.html', tmpl, ci)
