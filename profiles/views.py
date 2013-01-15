from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from profiles.models import Profile


def home(request):
    ci = RequestContext(request)
    tmpl = {
        'profiles': Profile.objects.all()
    }
    return render_to_response('profiles/home.html', tmpl, ci)


def profile(request, id, last_name, first_name):
    ci = RequestContext(request)
    tmpl = {
        'profile': get_object_or_404(Profile, id=id)
    }
    return render_to_response('profiles/profile.html', tmpl, ci)
