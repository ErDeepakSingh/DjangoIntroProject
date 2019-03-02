from django.conf.urls import url
from . import views as users_views
urlpatterns=[
    url(r'^$',users_views.users_list),
    url(r'^login/$',users_views.login)
]
