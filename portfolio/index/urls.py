from rest_framework.routers import DefaultRouter
from .views import HistoryViewSet,StudystateViewSet,StrongViewSet

router = DefaultRouter()
router.register(r'history',HistoryViewSet,basename="history")
router.register(r'studystate',StudystateViewSet,basename="studystate")
router.register(r'strong',StrongViewSet,basename="strong")