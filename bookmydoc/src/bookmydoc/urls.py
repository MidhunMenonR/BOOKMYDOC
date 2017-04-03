from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from docProfile.views import views

urlpatterns = [
    # Examples:
    url(r'^$', 'docProfile.views.home'),
    url(r'^home/', 'docProfile.views.home'),

    url(r'^docprofile/', 'docProfile.views.prof', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login-submit/', 'docProfile.views.loginform'),
    url(r'^search-submit/', 'docProfile.views.searchform'),
    url(r'^search-submitapp/', 'docProfile.views.searchformapp'),

    url(r'^view-docdetails/', 'docProfile.views.docdetails'),
    url(r'^login/', 'docProfile.views.loginPage'),
    url(r'^book-doct/', 'docProfile.views.bookDoc'),
    url(r'^confirm-book/', 'docProfile.views.confirm'),
    url(r'^locdetailentry/', 'docProfile.views.locdetail'),
    url(r'^locapp/', 'docProfile.views.location'),
    url(r'^apphome/', 'docProfile.views.apphome'),
    url(r'^notify/', 'docProfile.views.notification'),
    url(r'^ajaxlocationentry/', 'docProfile.views.ajaxlocationentry'),
    url(r'^doctorresponse/', 'docProfile.views.responsedoc'),
    url(r'^sample/', 'docProfile.views.sample'),
    url(r'^ajaxlocationrem/', 'docProfile.views.ajaxlocationrem'),
    url(r'^regtoken/', 'docProfile.views.regtoken'),
    url(r'^sebin/', 'docProfile.views.sebin'),
    url(r'^about/', 'docProfile.views.about'),

    
    url(r'^admin/', include(admin.site.urls)),


] 

if settings.DEBUG:
	urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)