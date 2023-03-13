from api.views import FundoImobiliarioViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(f'fundos', FundoImobiliarioViewSet)

urlpatterns = router.urls