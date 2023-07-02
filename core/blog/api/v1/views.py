from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework   import viewsets 
from ...models import Post
from .serialzer import ApiSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .permissions import PermissionTest
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import CustomPagination
#useing viewsets to show data instead of ApiView
class MyApiView(viewsets.ModelViewSet):
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    permission_classes=[IsAuthenticatedOrReadOnly]
    pagination_class=CustomPagination
    serializer_class=ApiSerializer
    queryset=Post.objects.all()
    filterset_fields=['title','content']
    search_fields=['title','content']
    ordering_fields=['published_date']

    def delete(self,request,id):
        serializer_value=self.serializer_class(self.queryset,data=request.data)
        serializer_value.delete()
        return Response(serializer_value.data)

  #the upper code with ApiView
"""""
class mytest(APIView):

    permission_classes=[IsAuthenticatedOrReadOnly,PermissionTest]
    serializer_class=serialize
    def post(self,request,id):
        post=Post.objects.all()
        serializer_calsses=serialize(post,data=request.data)
        serializer_calsses.is_valid(raise_exception=True)
        serializer_calsses.save()
        return Response(serializer_calsses.data)
    
    def get(self,request,id):
        queryset=Post.objects.all()
        serializer_calsses=serialize(queryset,many=True)
        return Response(serializer_calsses.data)
    
    def delete(self,request,id):
        post=Post.objects.all()
        serializer_calsses=serialize(post,data=request.data)
        serializer_calsses.delete()
        return Response(serializer_calsses.data)
"""""




