from django.conf.urls import patterns, include, url
from django.contrib import admin
from firstApp.views import provider_function_view, PackageClassView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirstDjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^provider/(?P<provider_id>\d+)/$', provider_function_view, name='provider'),
    url(r'^package/(?P<package_id>\d+)/$', PackageClassView.as_view(), name='package'),
)
