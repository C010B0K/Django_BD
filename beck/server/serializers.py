from rest_framework import serializers

from .models import Text,Photo,Price,Contacts




class TextSerializers(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = "__all__"


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"