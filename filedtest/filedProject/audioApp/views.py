from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Song, Podcast, Audiobook
from .serializers import AudioSerializer, SongSerializer, PodcastSerializer, AudiobookSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.conf import settings
import os
import json
# Create your views here.


def handle_uploaded_file(f, name):
    des = os.path.join(settings.MEDIA_ROOT, "audio", name)
    with open(des, 'wb+') as fp:
        for chunk in f.chunks():
            fp.write(chunk)
        return True



class CreateViewSet(generics.GenericAPIView):

    def post(self, request):
        # data = JSONParser().parse(request)
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            audioType = serializer.data['audioFileType']
            audioMetadata = serializer.data['audioFileMetadata']
            if audioType == 'song':
                song_serializer = SongSerializer(data=audioMetadata)
                if song_serializer.is_valid():
                    file_name = json.loads(request.data['audioFileMetadata'])['name'].replace(" ", "")
                    uploaded_status = handle_uploaded_file(request.FILES['audioFile'], file_name)
                    if uploaded_status:
                        file_link = request.get_host() + "/media/audio/" + file_name
                        song_serializer.save(file_url=file_link)
                        resp = {
                            'msg': 'success',
                            'uploaded_destination': file_link
                        }
                        return Response(resp, status=status.HTTP_201_CREATED)
                    else:
                        return JsonResponse("File Upload Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if audioType == 'podcast':
                podcast_serializer = PodcastSerializer(data=audioMetadata)

                if podcast_serializer.is_valid():
                    file_name = json.loads(request.data['audioFileMetadata'])['name'].replace(" ", "")
                    uploaded_status = handle_uploaded_file(request.FILES['audioFile'], file_name)
                    if uploaded_status:
                        file_link = request.get_host() + "/media/audio/" + file_name
                        podcast_serializer.save(file_url=file_link)
                        resp = {
                            'msg': 'success',
                            'uploaded_destination': file_link
                        }
                        return Response(resp, status=status.HTTP_201_CREATED)
                    else:
                        return JsonResponse("File Upload Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return JsonResponse(podcast_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if audioType == 'audiobook':
                audiobook_serializer = AudiobookSerializer(data=audioMetadata)
                if audiobook_serializer.is_valid():
                    file_name = json.loads(request.data['audioFileMetadata'])['title'].replace(" ", "")
                    uploaded_status = handle_uploaded_file(request.FILES['audioFile'], file_name)
                    if uploaded_status:
                        file_link = request.get_host() + "/media/audio/" + file_name
                        audiobook_serializer.save(file_url=file_link)
                        resp = {
                            'msg': 'success',
                            'uploaded_destination': file_link
                        }
                        return Response(resp, status=status.HTTP_201_CREATED)
                    else:
                        return JsonResponse("File Upload Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return JsonResponse(audiobook_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response("500 INTERNAL SERVER ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PodcastListView(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class PodcastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class AudiobookListView(generics.ListCreateAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer


class AudiobookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer



