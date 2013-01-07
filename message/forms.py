# -*- coding: utf-8 -*-
from django.forms import ModelForm

from message.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
