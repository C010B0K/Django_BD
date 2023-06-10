from django.shortcuts import render
from rest_framework import generics

from .models import Text,Photo,Price,Contacts
from .serializers import ContactsSerializers, PhotoSerializers, PriceSerializers, TextSerializers


class TextList(generics.ListAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializers

class PhotoList(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers

class PriceList(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializers

class ContactstList(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers

