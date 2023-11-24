from rest_framework.routers import SimpleRouter
from cake_creation.views import CakeView
router = SimpleRouter(trailing_slash=False)

router.register(r"cake_system", CakeView)

urlpatterns = []
urlpatterns+=router.urls
