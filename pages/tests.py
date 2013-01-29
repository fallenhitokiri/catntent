# -*- coding: utf-8 -*-
from django.test import TestCase

from pages.models import Page


class ModelTestCase(TestCase):
    fixtures = ['unittest']

    def setUp(self):
        self.pages = Page.objects.all()
        self.child = self.pages[0]
        self.hidden = self.pages[1]
        self.test = self.pages[2]
        self.unpublished = self.pages[3]

    def test_child(self):
        self.assertEqual(self.child.parent, self.test)

    def test_hidden(self):
        self.assertEqual(self.hidden.hidden, True)
    
    def test_page(self):
        self.assertEqual(self.test.published, True)
        self.assertEqual(self.test.hidden, False)
        self.assertEqual(self.test.parent, None)
    
    def test_unpublished(self):
        self.assertEqual(self.unpublished.published, False)
