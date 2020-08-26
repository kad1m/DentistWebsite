from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.sitemaps import BlogSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('', include('blog.urls')),
    )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
