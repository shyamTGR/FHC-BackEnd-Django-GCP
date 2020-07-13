from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.utils.text import slugify
from datetime import datetime
from django import forms
# Create your models here.
CHOICES = ["Yes","No"]

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    english_title = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    content = RichTextField()
    Optional_english_version_content = RichTextField(blank = True,null = True)
    created_date = models.DateTimeField(editable=True, blank=True)
    editing =  models.BooleanField(default=False)
    article_image = models.FileField(blank = True,null = True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

    def _get_unique_slug(self):
        slug = slugify(self.english_title)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,related_name="comments")
    comment_author = models.CharField(max_length = 50)
    comment_content = models.CharField(max_length = 200)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

class Live(models.Model):
    video_id = models.CharField(max_length = 100, unique=True, blank=False)
    title = models.CharField(max_length = 300, blank=False)
    caption_or_description = models.CharField(max_length = 300, blank=False)
    created_date = models.DateTimeField( blank=True)
    class Meta:
        ordering = ['-created_date']


class Lyric(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    telugu_name = models.CharField(max_length = 50)
    english_name = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    telugu_lyrics = RichTextField()
    english_lyrics = RichTextField(blank = True,null = True)
    created_date = models.DateTimeField(editable=True, blank=True)
    editing =  models.BooleanField(default=False)
    composer = models.CharField(default="Unknown",max_length = 150)
    singer = models.CharField(default="Unknown",max_length = 150)
    youTube_video = models.URLField(max_length=350, null=True, blank=True)
    TELUGU = 'TL'
    ENGLISH = 'EN'
    HINDI = 'HN'
    LANGUAGES = [
        (TELUGU, 'Telugu'),
        (ENGLISH, 'English'),
        (HINDI, 'Hindi'),
    ]
    language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default=TELUGU,
    )


    class Meta:
        ordering = ['-created_date']

    def _get_unique_slug(self):
        slug = slugify(self.english_name)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

class Chord(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    telugu_name = models.CharField(max_length = 50)
    english_name = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    key = models.CharField(max_length = 10, null = True)
    telugu_lyrics = RichTextField()
    english_lyrics = RichTextField(blank = True,null = True)
    created_date = models.DateTimeField(editable=True, blank=True)
    editing =  models.BooleanField(default=False)
    composer = models.CharField(default="Unknown",max_length = 150)
    singer = models.CharField(default="Unknown",max_length = 150)
    youTube_video = models.URLField(max_length=350, null=True, blank=True)
    TELUGU = 'TL'
    ENGLISH = 'EN'
    HINDI = 'HN'
    LANGUAGES = [
        (TELUGU, 'Telugu'),
        (ENGLISH, 'English'),
        (HINDI, 'Hindi'),
    ]
    language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default=TELUGU,
    )

    class Meta:
        ordering = ['-created_date']

    def _get_unique_slug(self):
        slug = slugify(self.english_name)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
    
    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
