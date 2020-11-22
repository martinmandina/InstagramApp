from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

urlpatterns=[
    url(r'^$',views.main,name='home'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^update/',views.edit,name='edit'),
    url(r'^search/',views.results_search,name='search'),


]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)