from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
# from .serializers import UserSerializer, GroupSerializer

# API Serializers
# class UserViewSet(viewsets.ModelViewSet):
    # """API endpoint that allows users to be viewed or edited."""
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
    # """API endpoint that allows groups to be viewed or edited."""
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer

# Create your views here.
def home(request):
    return render(request,'home/home.html')
