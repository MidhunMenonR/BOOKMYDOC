from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from docProfile.views import views

urlpatterns = [
    # Examples:
    url(r'^$', 'docProfile.views.home'),
    url(r'^docprofile/', 'docProfile.views.prof', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login-submit/', 'docProfile.views.loginform'),
    url(r'^search-submit/', 'docProfile.views.searchform'),
    url(r'^login/', 'docProfile.views.loginPage'),
    url(r'^admin/', include(admin.site.urls)),

] 

if settings.DEBUG:
	urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)