from rest_framework import serializers
from .models import Members, blog as Blogs, Comments, event as Events, Alumni
# access_tokens, Candidates, auditionAnswers, auditionQuestions, auditionRounds


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = "__all__"
