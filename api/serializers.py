from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    places = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'places')
        read_only_fields = ['places']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['user']

class MasterItemSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/validators/#advanced-field-defaults
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MasterItem
        fields = '__all__'
        read_only_fields = ['user']

class ShoppingListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ShoppingList
        fields = '__all__'
        read_only_fields = ['user']

class ShoppingItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ShoppingItem
        fields = '__all__'
        read_only_fields = ['user']

class PlaceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = ['user']
