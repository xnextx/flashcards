from rest_framework import viewsets, permissions, filters
from .models import *
from .serializers import *
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
import datetime


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    model = Group
    serializer_class = GroupSerializer
    permission_classes = (DjangoModelPermissions,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Group.objects.filter(owner=self.request.user)

        return queryset

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    model = Content
    serializer_class = ContentSerializer
    permission_classes = (DjangoModelPermissions,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Content.objects.filter(owner=self.request.user)

        return queryset

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    model = Progress
    serializer_class = ProgressSerializer
    permission_classes = (DjangoModelPermissions,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Progress.objects.filter(owner=self.request.user)

        return queryset
