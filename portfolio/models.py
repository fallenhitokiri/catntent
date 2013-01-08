from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from utils.markup import markup


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
    description = models.CharField(max_length=2000, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True)
    tech = models.ForeignKey(Tech)

    def __unicode__(self):
        return "%s [%s]" % (self.name, self.tech.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Job, self).save(*args, **kwargs)


class Shot(models.Model):
    image = models.ImageField(upload_to="portfolio/shots")
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.image.name


class Testimonial(models.Model):
    who = models.CharField(max_length=300)
    company = models.CharField(max_length=300, blank=True, null=True)
    logo = models.ImageField(upload_to="portfolio/logos")
    statement_raw = models.TextField()
    statement = models.TextField()

    def __unicode__(self):
        return "{0} {1}".format(self.who, self.company)

    def save(self, *args, **kwargs):
        self.statement = markup(self.statement_raw)
        super(Testimonial, self).save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=255, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True, null=True, verify_exists=True)
    intro = models.ImageField(upload_to="portfolio/intros")
    summary_raw = models.TextField()
    summery = models.TextField(blank=True)
    description_raw = models.TextField()
    description = models.TextField(blank=True)
    jobs = models.ManyToManyField(Job, blank=True, null=True, related_name='project')
    shots = models.ManyToManyField(Shot, blank=True, null=True, related_name='project')
    testimonial = models.ForeignKey(Testimonial, blank=True, null=True, related_name='project')
    user = models.ForeignKey(User, blank=True, null=True, related_name='projects')

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.summary_raw = markup(self.summery_raw)
        self.description = markup(self.description_raw)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        details = {
            'id': self.id,
            'slug': self.slug
        }
        return ('portfolio:project', (), details)
