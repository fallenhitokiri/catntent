# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Entry, Tag, Category
from blog.utils import merge_query_sets, paginate


def home(request):
    ci = RequestContext(request)
    tmpl = {}
    page = int(request.GET.get('page', '1'))

    entry_list = Entry.public.all()
    tmpl['entries'] = paginate(entry_list, page)

    return render_to_response('blog/home.html', tmpl, ci)


def archive(request):
    ci = RequestContext(request)
    tmpl = {}
    page = int(request.GET.get('page', '1'))

    entry_list = Entry.public.all()
    tmpl['entries'] = paginate(entry_list, page, 10)

    return render_to_response('blog/archive.html', tmpl, ci)


def category(request, id, slug):
    ci = RequestContext(request)
    tmpl = {}
    page = int(request.GET.get('page', '1'))

    category = Category.objects.get(id=id)
    articles = category.article_category.all()
    notes = category.note_category.all()
    links = category.link_category.all()
    pictures = category.picture_category.all()

    entries = merge_query_sets(articles, notes, links, pictures)

    tmpl['entries'] = paginate(entries, page, 10)
    tmpl['category'] = category

    return render_to_response('blog/categories.html', tmpl, ci)


def tag(request, id, slug):
    ci = RequestContext(request)
    tmpl = {}
    page = int(request.GET.get('page', '1'))

    tag = Tag.objects.get(id=id)
    articles = tag.article_tag.all()
    notes = tag.note_tag.all()
    links = tag.link_tag.all()
    pictures = tag.picture_tag.all()

    entries = merge_query_sets(articles, notes, links, pictures)

    tmpl['entries'] = paginate(entries, page, 10)
    tmpl['tag'] = tag

    return render_to_response('blog/tags.html', tmpl, ci)


def entry(request, id, slug):
    ci = RequestContext(request)
    tmpl = {
        'entry': get_object_or_404(Entry.public, id=id)
    }
    return render_to_response('blog/entry.html', tmpl, ci)
