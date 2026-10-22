from django.contrib.auth.models import User

from rest_framework import serializers

from campus_feedback.models import Feedback

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

        read_only_fields = ["id"]

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:

        model = Feedback

        fields = "__all__"

        read_only_fields = ["id","student","created_at"]

        