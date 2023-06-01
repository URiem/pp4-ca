from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4
from django.urls import reverse
from cloudinary.models import CloudinaryField


# class Country(models.Model):
#     title = models.CharField(max_length=200)

#     # Utility Variables
#     uniqueId = models.CharField(null=True, blank=True, max_length=100)
#     slug = models.SlugField(max_length=500, unique=True)
#     date_created = models.DateTimeField()
#     last_updated = models.DateTimeField()

#     def __str__(self):
#         return '{} {}'.format(self.title, self.uniqueId)

#     def get_absolute_url(self):
#         return reverse('country-detail', kwargs={'slug': self.slug})

#     def save(self, *args, **kwargs):
#         if self.date_created is None:
#             self.date_created = timezone.localtime(timezone.now())
#         if self.uniqueId is None:
#             self.uniqueId = str(uuid4()).split('-')[4]
#             self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

#         self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
#         self.last_updated = timezone.localtime(timezone.now())
#         super(Country, self).save(*args, **kwargs)


STATUS = ((0, "Draft"), (1, "Published"))
PRIVACY = ((0, "Privat"), (1, "Public"))


class Logentry(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    privacy = models.IntegerField(choices=PRIVACY, default=0)
    featured_image = CloudinaryField('image', default='placeholder')

    # Related Fields
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="log_entry")
    # country = models.ForeignKey(
    #     Country, on_delete=models.CASCADE, related_name="countries")

    # slug = models.SlugField(max_length=200, unique=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-created_on']

    # def __str__(self):
    #     return self.title

    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('logentry-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(
                self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Logentry, self).save(*args, **kwargs)
