from rest_framework import serializers
from mony.models import News


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'news_time', 'news_text', 'news_inform']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.news_time = validated_data.get('news_time', instance.news_time)
        instance.news_text = validated_data.get('news_text', instance.news_text)
        instance.news_inform = validated_data.get('news_inform', instance.news_inform)
        
        instance.save()
        return instance