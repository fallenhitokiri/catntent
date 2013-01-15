# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from managers.published import PubManager
from utils.markup import markup


class Entry(models.Model):
    """Entry Model for various blog post types

    only this model will be queried
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    added = models.DateTimeField()
    published = models.BooleanField()
    slug = models.SlugField(max_length=255, blank=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, blank=True, null=True, related_name="entries")
    objects = models.Manager()
    public = PubManager()

    class Meta:
        ordering = ['-added']
        get_latest_by = "added"

    def __unicode__(self):
        return self.content_object.title

    @models.permalink
    def get_absolute_url(self):
        """absolute url for entry -> based on id and slug"""
        details = {
            'id': self.id,
            'slug': self.content_object.slug
        }
        return ('blog:entry', (), details)

    @property
    def title(self):
        return self.content_object.title

    @property
    def changed(self):
        return self.content_object.changed

    @property
    def content(self):
        return self.content_object.content

    @property
    def tags(self):
        return self.content_object.tags

    @property
    def categories(self):
        return self.content_object.categories

    @property
    def teaser(self):
        return self.content_object.teaser

    @property
    def image(self):
        return str(self.content_object.image)

    @property
    def ct(self):
        """return content type as string for template propose"""
        return str(self.content_type)


class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __unicode__(self):
        """title as name"""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Attachment(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, related_name="%(class)s")

    class Meta:
        abstract = True


class ImageAttachment(Attachment):
    image = models.ImageField(upload_to="blog/attachments/images")

    def __unicode__(self):
        return "[{0}] {1}".format(self.added, self.image)


class Base(models.Model):
    """Base class for various post types"""
    title = models.CharField(max_length=1000)
    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, blank=True)
    tags = models.ManyToManyField(Tag, related_name="%(class)s_tag", blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="%(class)s_categories", blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        """date and title as name"""
        return "%s %s" % (self.added, self.title)

    def save(self, *args, **kwargs):
        """generate slug and run content markup"""
        self.slug = slugify(self.title)
        super(Base, self).save(*args, **kwargs)


class Article(Base):
    teaser_raw = models.TextField(blank=True)
    teaser = models.TextField(blank=True)
    content_raw = models.TextField()
    content = models.TextField(blank=True)
    images = models.ManyToManyField(ImageAttachment, blank=True, null=True, related_name='images')

    def save(self, *args, **kwargs):
        """run teaser and content markup"""
        self.teaser = markup(self.teaser_raw)
        self.content = markup(self.content_raw)
        super(Article, self).save(*args, **kwargs)


class Note(Base):
    content_raw = models.TextField()
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """run content markup"""
        self.content = markup(self.content_raw)
        super(Note, self).save(*args, **kwargs)


class Link(Base):
    url = models.URLField(blank=True, verify_exists=True)
    content_raw = models.TextField(blank=True)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """run content markup"""
        self.content = markup(self.content_raw)
        super(Link, self).save(*args, **kwargs)


class Picture(Base):
    image = models.ImageField(upload_to="blog/picture")
    content_raw = models.TextField(blank=True)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """run content markup"""
        self.content = markup(self.content_raw)
        super(Picture, self).save(*args, **kwargs)


def create_entry(sender, **kwargs):
    """if a new post is made, create or update entry model"""
    if 'created' in kwargs:
        if kwargs['created']:
            # new entry created
            instance = kwargs['instance']
            ctype = ContentType.objects.get_for_model(instance)
            entry = Entry.objects.get_or_create(content_type=ctype,
                                                object_id=instance.id,
                                                added=instance.added,
                                                published=instance.published,
                                                slug=instance.slug,
                                                user=instance.user)
        else:
            # updated entry
            instance = kwargs['instance']
            ctype = ContentType.objects.get_for_model(instance)
            entry = Entry.objects.get(content_type=ctype,
                                      object_id=instance.id)
            entry.published = instance.published
            entry.save()


post_save.connect(create_entry, sender=Article)
post_save.connect(create_entry, sender=Note)
post_save.connect(create_entry, sender=Link)
post_save.connect(create_entry, sender=Picture)
