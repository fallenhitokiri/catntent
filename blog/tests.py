# -*- coding: utf-8 -*-
from django.test import TestCase

from blog.models import Article, Note, Link, Picture, Entry


class ModelTestCase(TestCase):
    fixtures = ['test_data', 'navigation']

    def setUp(self):
        """
        Entries in DB
        [4]: Article
        [3]: Artilce
        [2]: Note
        [1]: Link
        [0]: Picture
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
        self.assertEqual(self.link.url, "www.screamingatmyscreen.com")
        self.assertEqual(self.link.content, "<p>content</p>\n")

    def test_pictue(self):
        self.assertEqual(self.picture.content, "<p>content</p>\n")

    def test_entry(self):
        self.assertEqual(self.entries[4].slug, "test-article")
        self.assertEqual(self.entries[4].published, True)
        self.assertEqual(self.entries[3].slug, "test-article-2")
        self.assertEqual(self.entries[3].published, False)
        self.assertEqual(self.entries[2].slug, "test-note")
        self.assertEqual(self.entries[1].slug, "test-link")
        self.assertEqual(self.entries[0].slug, "test-picture")
