from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^create/', include('issue.urls.create', namespace='create')),
)