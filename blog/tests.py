# -*- coding: utf-8 -*-
from django.test import TestCase

from blog.models import Article, Note, Link, Picture, Entry


class ModelTestCase(TestCase):
    fixtures = ['unittest']

    def setUp(self):
        """
        Entries in DB
        [4]: Article
        [3]: Note
        [2]: Link
        [1]: Picture
        [0]: Article
        """
        self.entries = Entry.objects.all()
        self.article = Article.objects.all()[0]
        self.note = Note.objects.all()[0]
        self.link = Link.objects.all()[0]
        self.picture = Picture.objects.all()[0]

    def test_article(self):
        self.assertEqual(self.article.teaser, "<p>teaser</p>\n")
        self.assertEqual(self.article.content, "<p>content</p>\n")

    def test_note(self):
        self.assertEqual(self.note.content, "<p>content</p>\n")

    def test_link(self):
        self.assertEqual(self.link.url, "http://www.screamingatmyscreen.com/")
        self.assertEqual(self.link.content, "<p>content</p>\n")

    def test_pictue(self):
        self.assertEqual(self.picture.content, "<p>content</p>\n")

    def test_entry(self):
        self.assertEqual(self.entries[4].slug, "test-article")
        self.assertEqual(self.entries[4].published, True)
        self.assertEqual(self.entries[3].slug, "test-note")
        self.assertEqual(self.entries[2].slug, "test-link")
        self.assertEqual(self.entries[1].slug, "test-picture")
        self.assertEqual(self.entries[0].slug, "unpublished-article")
        self.assertEqual(self.entries[0].published, False)
