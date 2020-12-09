from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'master', views.MasterViewSet)
router.register(r'list', views.ShoppingListViewSet)
router.register(r'listitem', views.ShoppingItemViewSet)

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('user/', views.UserView.as_view()),
    path('', include(router.urls)),
]
