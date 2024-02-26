from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import jobCategoryViewset,jobCircularViewset,jobApplicationViewset

# write your urls on here
router = DefaultRouter()

router.register('category', jobCategoryViewset)
router.register('circular', jobCircularViewset)
router.register('application', jobApplicationViewset)

urlpatterns = [
    path('', include(router.urls))
]
