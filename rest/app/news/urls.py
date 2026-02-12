from rest_framework.routers import DefaultRouter
from app.news.views import NewsCategoryViewSet, NewsViewSet

router = DefaultRouter()

router.register(r"news-category", NewsCategoryViewSet, basename="newscategory")
router.register(r"news", NewsViewSet, basename="news")

urlpatterns = router.urls
