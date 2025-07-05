from rest_framework import viewsets, permissions, filters
from .models import NetworkNode, Contact, Product
from .serializers import NetworkNodeSerializer, ContactSerializer, ProductSerializer
from .filters import NetworkNodeFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class IsActiveUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
    filterset_class = NetworkNodeFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'contact__country', 'contact__city']
    ordering_fields = ['created_at', 'debt']

    def perform_update(self, serializer):
        # Запрещаем обновление поля debt через API
        if 'debt' in serializer.validated_data:
            del serializer.validated_data['debt']
        serializer.save()

    @action(detail=True, methods=['post'])
    def clear_debt(self, request, pk=None):
        node = self.get_object()
        node.debt = 0
        node.save()
        return Response({'status': 'debt cleared'})


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
