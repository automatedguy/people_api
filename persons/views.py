from rest_framework import request
from rest_framework.viewsets import ModelViewSet

from .models import Person, Introduction, Description
from .serializers import PersonSerializer, IntroductionSerializer, DescriptionSerializer


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class IntroductionViewSet(ModelViewSet):
    serializer_class = IntroductionSerializer
    queryset = Introduction.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(person=self.kwargs.get('person_pk'))


class DescriptionViewSet(ModelViewSet):
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(person=self.kwargs.get('person_pk'))