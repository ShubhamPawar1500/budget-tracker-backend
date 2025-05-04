from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, CategoryViewSet, TransactionViewSet, BudgetViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'budgets', BudgetViewSet, basename='budget')

urlpatterns = [
    path('', include(router.urls)),
]
