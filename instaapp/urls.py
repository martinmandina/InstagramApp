from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

urlpatterns=[
    url(r'^$',views.main,name='home'),

]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)