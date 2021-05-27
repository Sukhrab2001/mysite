from django.contrib.auth.models import User
from .serializator import UserSerializer, UserSerializeDetails, CycleSerializer, CycleSerializerDetail, BoostSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MainCycle, Boost
import services


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializeDetails


class CycleList(generics.ListAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleSerializer


class CycleDetail(generics.RetrieveAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleSerializerDetail


class BoostList(generics.ListAPIView):
    queryset = Boost
    serializer_class = BoostSerializer

    def get_queryset(self):
        return Boost.objects.filter(mainCycle=self.kwargs['mainCycle'])


@api_view(['POST'])
def buyBoost(request):
    click_power, coins_count, level, price = services.clicker_services.buy_boost(request)
    return Response({'clickPower': click_power,
                     'coinsCount': coins_count,
                     'level': level,
                     'price': price})


@api_view(['GET'])
def callClick(request):
    data = services.clicker_services.call_click(request)
    return Response(data)
