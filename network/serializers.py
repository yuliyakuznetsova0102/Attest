from rest_framework import serializers
from .models import NetworkNode, Contact, Product
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)
    hierarchy_level = serializers.IntegerField(read_only=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at')

    def validate(self, data):
        supplier = data.get('supplier')
        node_type = data.get('node_type')

        if supplier and supplier.node_type == 'entrepreneur' and node_type != 'entrepreneur':
            raise serializers.ValidationError(
                "Индивидуальный предприниматель может быть поставщиком только для других ИП"
            )

        if node_type == 'factory' and supplier:
            raise serializers.ValidationError("Завод не может иметь поставщика")

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']
