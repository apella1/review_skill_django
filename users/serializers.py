from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import User


class UserSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "avatar",
            "edit_url",
        ]

    def get_edit_url(self, obj):
        """Getting the url of a user's update page"""
        request = self.context.get("request")
        return (
            None
            if request is None
            else reverse("user-edit", kwargs={"pk": obj.pk}, request=request)
        )
