# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from message.forms import MessageForm
from message.models import Message


def home(request):
    """render contact form

    if a form is submitted check if it is valid and save it
    """
    ci = RequestContext(request)
    tmpl = {}
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(
                    name=form.cleaned_data['name'],
                    mail=form.cleaned_data['mail'],
                    message=form.cleaned_data['message']
                )
            message.save()
            tmpl['form'] = MessageForm()
            tmpl['success'] = 1
        else:
            tmpl['form'] = form
            tmpl['error'] = 1
    else:
        form = MessageForm()
        tmpl['form'] = form
    return render_to_response("message/home.html", tmpl, ci)
