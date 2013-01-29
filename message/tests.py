# -*- coding: utf-8 -*-
from django.test import TestCase

from message.models import Message


class ModelTestCase(TestCase):
    fixtures = ['unittest']

    def setUp(self):
        self.messages = Message.objects.all()

    def test_done_true(self):
        self.assertEqual(self.messages[1].done, True)

    def test_done_false(self):
        self.assertEqual(self.messages[0].done, False)
