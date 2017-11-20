# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin
from django.utils.translation import ugettext_lazy

# admin.site.site_title = ugettext_lazy('My site admin')
# admin.site.site_header = ugettext_lazy('My administration')
# admin.site.index_title = ugettext_lazy('Site administration')

urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                       # url(r'^jogo/', include('jogo.urls')),
                       url(r'^api/v1/pergunta', include('pergunta.urls')),
                       url(r'^api/v1/user' , include('user.urls')),
                       url(r'^api/v1/$|^', include('rest_framework_docs.urls')),
                       url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# Add client urls for debug mode
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#  u860844912_show
# This catch all url has to be last
# urlpatterns += url(r'^.*$', 'core.views.home', name='home'),
