from rest_framework import serializers
from .models import Song, Podcast, Audiobook

AUDIO_CHOICES = ['song', 'podcast', 'audiobook']


class AudioSerializer(serializers.Serializer):
    audioFileType = serializers.ChoiceField(AUDIO_CHOICES)
    audioFileMetadata = serializers.JSONField()
    audioFile = serializers.FileField()

    def validate_audioFileType(self, value):
        if value not in AUDIO_CHOICES:
            raise serializers.ValidationError('audioFileType Field value must be one of type (song, podcast, audiobook)')
        return value

    # def validate_audioFileMetadata(self, value):
    #     pass


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ('file_url',)


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'
        read_only_fields = ('file_url',)


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'
        read_only_fields = ('file_url',)

