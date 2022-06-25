from rest_framework import serializers
from .models import User, LinkDetails, UserLinks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LinkDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkDetails
        fields = ('id', 'title', 'icon_url')


class UserLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLinks
        fields = ('id', 'user_id', 'link_id', 'link_url')
        extra_kwargs = {'link_id': {'required': True}, 'link_url': {'required': True},
                        'user_id': {'required': False}}
