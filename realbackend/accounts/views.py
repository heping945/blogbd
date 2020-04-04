from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from utils.permission import IsCurUserOrReadOnly
from rest_framework.mixins import UpdateModelMixin

from .validate import validpassword
from .serializers import UserSerializer,UserSimpleSerializer,UserRegSerializer,UserUpdateSerializer,UserAvatarSerializer
from .models import UserProfile


class UserViewset(viewsets.ModelViewSet):
    '''
    处理api/userprofile
    '''
    queryset = UserProfile.objects.all()
    lookup_field = 'urltoken'
    ordering_fields = ('create_time',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserSerializer
        elif self.action == 'list':
            return  UserSimpleSerializer
        elif self.action == 'create':
            return  UserRegSerializer
        return UserUpdateSerializer


class UserPasswordViewset(viewsets.ViewSet):
    permission_classes = (IsCurUserOrReadOnly,)
    lookup_field = 'username'
    def partial_update(self, request,version,username):
        data = {}
        rpwd = request.data.get('password',None)
        npwd = request.data.get('password2',None)
        if all([username,rpwd,npwd]) and rpwd!=npwd:
            user = UserProfile.objects.filter(username=username).first()
            self.check_object_permissions(self.request, user)       # 权限验证
            if user:
                if user.check_password(rpwd):
                    if validpassword(npwd):
                        user.set_password(npwd)
                        user.save(update_fields=["password"])
                        data['msg']='scuusss'
                        data['code']=666
                        return Response(data)
        data['msg']='bad request'
        data['code']=999
        return Response(data)



class UserAvatarViewset(viewsets.GenericViewSet,UpdateModelMixin):
    lookup_field = 'username'
    permission_classes = (IsCurUserOrReadOnly,)
    serializer_class = UserAvatarSerializer
    queryset = UserProfile.objects.all()