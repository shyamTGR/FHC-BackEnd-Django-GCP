from .models import Article, Comment, Live, Lyric, Chord
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author','title','english_title','slug','content','Optional_english_version_content','created_date','editing','article_image']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'comment_author','comment_date']

class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live
        fields = ['video_id', 'title','caption_or_description','created_date']

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['author','telugu_name','english_name','slug','telugu_lyrics','english_lyrics','created_date','language','editing','composer','singer','youTube_video']

class ChordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chord
        fields = ['author','telugu_name','english_name','slug','key','telugu_lyrics','english_lyrics','created_date','language','editing','composer','singer','youTube_video']


