from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^about/$', 'profiles.views.home'),
    url(r'^contact/$', 'profiles.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
