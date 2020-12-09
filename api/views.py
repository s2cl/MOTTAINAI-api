from rest_framework import generics, permissions
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    """
    post:
    ユーザーを作成する

    """
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    ユーザーの情報と保管場所の一覧を取得する。

    put:
    passwordの更新を伴う変更

    patch:
    登録情報の一部を変更する

    delete:
    ユーザーを削除する
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ItemViewSet(viewsets.ModelViewSet):
    """
    get:
    placeに登録されているItemを取得する

    post:
    placeにItemを登録する

    """

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = self.request.user.items.all()
        place = self.request.GET.get('place')
        if place is not None:
            queryset = queryset.filter(place=place)
        return queryset

class MasterViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MasterItem.objects.all()
    serializer_class = MasterItemSerializer

    def get_queryset(self):
        return self.request.user.masteritems.all()


class ShoppingListViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def get_queryset(self):
        return self.request.user.shoppinglists.all()
    

class ShoppingItemViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

    def get_queryset(self):
        return self.request.user.shoppingitems.all()

