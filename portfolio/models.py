from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from common.utils.markup import markup
from common.managers.published import PubManager


class Tech(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tech, self).save(*args, **kwargs)


class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    tech = models.ForeignKey(Tech)

    def __unicode__(self):
        return "%s [%s]" % (self.name, self.tech.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Job, self).save(*args, **kwargs)


class Shot(models.Model):
    image = models.ImageField(upload_to="portfolio/shots")
    description = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.image.name


class Testimonial(models.Model):
    statement_raw = models.TextField()
    statement = models.TextField(blank=True)

    def __unicode__(self):
        if len(self.customer.all()) > 0:
            return self.customer.all()[0].company
        else:
            return self.statement_raw

    def save(self, *args, **kwargs):
        self.statement = markup(self.statement_raw)
        super(Testimonial, self).save(*args, **kwargs)


class Customer(models.Model):
    company = models.CharField(max_length=500)
    contact = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to="portfolio/logos", blank=True, null=True)
    testimonial = models.ForeignKey(Testimonial, blank=True, null=True, related_name='customer')

    def __unicode__(self):
        return self.company


class Project(models.Model):
    name = models.CharField(max_length=500)
    customer = models.ForeignKey(Customer, blank=True, null=True, related_name='projects')
    slug = models.SlugField(max_length=255, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    url = models.URLField(blank=True, verify_exists=True)
    intro = models.ImageField(upload_to="portfolio/intros")
    summary_raw = models.TextField()
    summery = models.TextField(blank=True)
    description_raw = models.TextField()
    description = models.TextField(blank=True)
    jobs = models.ManyToManyField(Job, blank=True, null=True, related_name='project')
    shots = models.ManyToManyField(Shot, blank=True, null=True, related_name='project')
    user = models.ForeignKey(User, blank=True, null=True, related_name='projects')
    objects = models.Manager()
    public = PubManager()

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.summary = markup(self.summary_raw)
        self.description = markup(self.description_raw)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        details = {
            'id': self.id,
            'slug': self.slug
        }
        return ('portfolio:project', (), details)
