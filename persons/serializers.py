from rest_framework.serializers import ModelSerializer
from persons import models


class PersonSerializer(ModelSerializer):

    class Meta:
        fields = (
            'id',
            'nickname',
            'first_name',
            'last_name',
            'birth_date',
            'creation_date',
            'active',
            'sex'
        )

        model = models.Person


class IntroductionSerializer(ModelSerializer):

    class Meta:
        fields = (
            'id',
            'person',
            'introduction'
        )

        model = models.Introduction


class DescriptionSerializer(ModelSerializer):

    class Meta:
        fields = (
            'id',
            'person',
            'description'
        )

        model = models.Description


class ContactInfoSerializer(ModelSerializer):

    class Meta:
        fields = (
            'id',
            'person'
            'mobile',
            'home',
            'email',
            'facebook',
            'instagram'
        )

        model = models.ContactInfo


class PhotoProfileSerializer(ModelSerializer):

    class Meta:
        fields = (
            'id',
            'person',
            'photo_profile'
        )

        model = models.PhotoProfile


class PhotoSerializer(ModelSerializer):

    class Meta:
        fields = (
            'id',
            'person',
            'photo'
        )

        model = models.Photo


class VideoSerializer(ModelSerializer):

    class Meta:
        fields = (
            'id',
            'person',
            'video'
        )

        model = models.Video
