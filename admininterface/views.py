# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    ci = RequestContext(request)
    tmpl = {}
    return render_to_response('admininterface/home.html', tmpl, ci)
