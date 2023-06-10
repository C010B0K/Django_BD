
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings


from server.views import TextList, PhotoList, PriceList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/text', TextList.as_view()),
    path('api/photo', PhotoList.as_view()),
    path('api/price', PriceList.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)