from django.db import models
import datetime
from markdown import markdown


class Category(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum 250 characters.")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ("category", (), {'category':self.slug })
    
class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
                      (LIVE_STATUS, 'Live'),
                      (DRAFT_STATUS, 'Draft'),
    )
    
    #content
    head = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    
    #output
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)
    
    #meta
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    jump = models.BooleanField(default=False)
    
    #tagging
    category = models.ManyToManyField(Category)
    
        
    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
        
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.head
    
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'year':self.pub_date.strftime("%Y"),
                             'month':self.pub_date.strftime("%b").lower(),
                             'day':self.pub_date.strftime("%d"),
                             'slug':self.slug})
        


    