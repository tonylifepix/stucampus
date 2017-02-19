from django.conf.urls import patterns, url

from stucampus.comment.views import *

urlpatterns = [
    url(r'^get$', get_comment, name='getComment'),
    url(r'^add$', add_comment, name='addComment'),
]
