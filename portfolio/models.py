from django.db import models
from django.template.defaultfilters import slugify

from markdown2 import markdown


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
    slug = models.SlugField(max_length=100, blank=True)
    tech = models.ForeignKey(Tech)

    def __unicode__(self):
        return "%s [%s]" % (self.name, self.tech.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Job, self).save(*args, **kwargs)


class Shot(models.Model):
    image = models.ImageField(upload_to="portfolio/")
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.image.name


class Project(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=255, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True, null=True, verify_exists=True)
    intro = models.ImageField(upload_to="portfolio/")
    short_raw = models.TextField()
    short = models.TextField(blank=True)
    content_raw = models.TextField()
    content = models.TextField(blank=True)
    testimonial_raw = models.TextField(blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)
    jobs = models.ManyToManyField(Job)
    shots = models.ManyToManyField(Shot)

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.short = markdown(self.short_raw)
        self.content = markdown(self.content_raw)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        details = {
            'id': self.id,
            'slug': self.slug
        }
        return ('portfolio:project', (), details)
