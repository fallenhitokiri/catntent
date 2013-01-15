# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Entry


def home(request):
    ci = RequestContext(request)
    tmpl = {
        'entries': Entry.public.all()[:5]
    }
    return render_to_response('blog/home.html', tmpl, ci)


def archive(request):
    ci = RequestContext(request)
    tmpl = {
        'entries': Entry.public.all()
    }
    return render_to_response('blog/archive.html', tmpl, ci)


def entry(request, id, slug):
    ci = RequestContext(request)
    tmpl = {
        'entry': get_object_or_404(Entry.public, id=id)
    }
    return render_to_response('blog/entry.html', tmpl, ci)
