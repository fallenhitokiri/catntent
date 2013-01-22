# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator

from blog.models import Entry


def home(request):
    ci = RequestContext(request)
    tmpl = {}

    entry_list = Entry.objects.all()
    paginator = Paginator(entry_list, 5)

    try:
        current_page = int(request.GET.get('page', '1'))
    except:
        current_page = 1

    try:
        tmpl['entries'] = paginator.page(current_page)
    except:
        tmpl['entries'] = paginator.page(paginator.num_pages)

    return render_to_response('blog/home.html', tmpl, ci)


def archive(request):
    ci = RequestContext(request)
    tmpl = {
        'entries': Entry.public.all()
    }
    return render_to_response('blog/archive.html', tmpl, ci)


def category_archive(request, id, slug):
    pass


def tag_archive(request, id, slug):
    pass


def entry(request, id, slug):
    ci = RequestContext(request)
    tmpl = {
        'entry': get_object_or_404(Entry.public, id=id)
    }
    return render_to_response('blog/entry.html', tmpl, ci)
