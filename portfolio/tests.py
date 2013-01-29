# -*- coding: utf-8 -*-
from django.test import TestCase

from portfolio.models import Project


class ModelTestCase(TestCase):
    fixtures = ['unittest']

    def setUp(self):
        self.project = Project.objects.get(id=1)

    def test_project(self):
        self.assertEqual(self.project.published, True)
    
    def test_customer(self):
        self.assertEqual(self.project.customer.title, "Janitor")
    
    def test_testimonial(self):
        self.assertEqual(self.project.customer.testimonial.statement, "<p>testimonial</p>\n")
    
    def test_job(self):
        job = self.project.jobs.all()[0]
        self.assertEqual(job.slug, "job-1")
    
    def test_tech(self):
        tech = self.project.jobs.all()[0].tech
        self.assertEqual(tech.slug, "tech")
