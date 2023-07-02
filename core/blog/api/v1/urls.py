from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views
app_name='api-v1'
router=DefaultRouter()
router.register('post',views.MyApiView,basename='my-api-view')
urlpatterns = router.urls
