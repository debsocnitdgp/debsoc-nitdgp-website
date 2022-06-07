from rest_framework import serializers
from .models import Members, blog as Blogs, Comments, event as Events, Alumni
# access_tokens, Candidates, auditionAnswers, auditionQuestions, auditionRounds


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = ['username', 'firstname', 'lastname', 'email', 'bio', 'year', 'post', 'sno', 'dp', 'facebook_url', 'instagram_url', 'linkedin_url']

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogs
        fields = ['title', 'blog_text', 'image_url', 'created_on', 'active', 'author']

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['post', 'comment_by', 'comment', 'commented_on', 'active']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ['event_name', 'event_description', 'poster', 'event_datetime', 'event_mode', 'event_status', 'active', 'text1', 'url1', 'text2', 'url2', 'text3', 'url3']

class AlumniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumni
        fields = ['firstname', 'lastname', 'email', 'batch', 'sno', 'propic', 'facebook_url', 'instagram_url', 'linkedin_url']
