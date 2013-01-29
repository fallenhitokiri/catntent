# -*- coding: utf-8 -*-
from django.test import TestCase

from profiles.models import Profile
from profiles.utils import normalize_username


class ModelTestCase(TestCase):
    fixtures = ['unittest']

    def setUp(self):
        self.profile = Profile.objects.get(id=1)

    def test_social(self):
        twitter = self.profile.social.all()[0]
        self.assertEqual(twitter.username, "fallenhitokiri")


class UtilsTestCase(TestCase):
    def test_normalization(self):
        user = normalize_username("T", "@fallenhitokiri")
        self.assertEqual(user, "fallenhitokiri")
