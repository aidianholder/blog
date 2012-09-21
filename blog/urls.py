from django.conf.urls.defaults import *

urlpatterns = patterns('azhsite.blog.views',
                      url(r'^$', 'entries_index', name="index"),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>\D+)/$', 'entry_detail', name="post"),
                      url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'month_archive', name="month-archive"),
                      url(r'^category/(?P<category>\D+)/$', 'category_detail', name="category"),
                      )