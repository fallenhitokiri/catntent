# -*- coding: utf-8 -*-
from django.test import TestCase

from blog.models import Article, Note, Link, Picture, Entry
from blog.utils import paginate, merge_query_sets


class ModelTestCase(TestCase):
    fixtures = ['unittest']

    def setUp(self):
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


class UtilsTest(TestCase):
    fixtures = ['unittest']
    
    def test_pagination(self):
        entries = Entry.objects.all()
        article = Article.objects.all()[1]
        
        page = paginate(entries, count=1)
        
        self.assertFalse(page.has_previous())
        self.assertTrue(page.has_next())
        self.assertEqual(page.object_list[0].content_object, article)
        self.assertEqual(page.number, 1)
    
    def test_merge_query_sets(self):
        article = Article.objects.all()
        note = Note.objects.all()
        link = Link.objects.all()
        picture = Picture.objects.all()
        
        merged = merge_query_sets(article, note, link, picture)
        
        self.assertEqual(len(merged), 4)
