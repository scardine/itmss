from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from conteudo.views import Home, PortifolioList
import object_tools

admin.autodiscover()
object_tools.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'^portifolio/$', PortifolioList.as_view(), name='portifolio'),
    # url(r'^blog/', include('blog.urls')),
    (r'^object-tools/', include(object_tools.tools.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
