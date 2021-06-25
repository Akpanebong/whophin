from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .views import layout, indexs,it, con


urlpatterns = [
    path('ad/', admin.site.urls),
    path('', include('wholphin.urls')),
    path('products/', include('products.urls')),
    path('in/', indexs, name='in'),
    path('it/', it, name='it'),
    path('con/', con, name='con'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Wholphinplus Venture'
admin.site.index_title = 'welcome to who'
admin.site.site_title='wholphin'