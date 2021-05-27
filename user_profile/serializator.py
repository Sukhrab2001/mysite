from .models import User, MainCycle, Boost
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserSerializeDetails(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id']


class CycleSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id', 'user', 'coinsCount', 'clickPower', 'boosts']


class BoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boost
        fields = ['level', 'power', 'price']
