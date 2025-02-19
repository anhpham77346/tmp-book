from rest_framework import serializers
from .models import Customer, FullName, Address

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'postal_code', 'country']

class CustomerSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = ['username', 'password', 'email', 'phone', 'full_name', 'address']
        extra_kwargs = {
            'password': {'write_only': True},  # Để mật khẩu không hiển thị khi trả về response
        }

    def create(self, validated_data):
        full_name_data = validated_data.pop('full_name', None)
        address_data = validated_data.pop('address', None)
        password = validated_data.pop('password', None)

        full_name = FullName.objects.create(**full_name_data) if full_name_data else None
        address = Address.objects.create(**address_data) if address_data else None

        customer = Customer(full_name=full_name, address=address, **validated_data)
        if password:
            customer.set_password(password)  # Mã hóa mật khẩu trước khi lưu
        customer.save()
        return customer
