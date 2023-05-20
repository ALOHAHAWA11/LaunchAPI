from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class LaunchAPIView(APIView):

    def get(self, request, id):
        launch = Launch.objects.filter(id=id).values()
        comments = Comment.objects.filter(launch__id=id).values()
        return Response({'launch': launch, 'comments': list(comments)})

    def post(self, request, id):
        if Launch.objects.get(id=id):
            return Response({'msg': f'there is launch with id="{id}"'})
        launch = Launch.objects.create(
            id=id,
            name=request.data['_name'],
            window_start=request.data['_window_start'],
            window_end=request.data['_window_end']
        )
        return Response({'launch': model_to_dict(launch)})


class CommentAPIView(APIView):
    def get(self, request, id):
        comments = Comment.objects.filter(launch__id=id).values()
        print(comments)
        if comments:
            return Response(comments)
        return Response({'msg': 'no comments'})

    def post(self, request, id):
        new_comment = Comment.objects.create(
            content=request.data['content'],
            author=request.data['author_id'],
            launch_id=request.data['launch_id'],
            published_date=request.data['published_date']
        )
        return Response({'comment': model_to_dict(new_comment)})


class ArchiveAPIView(APIView):
    def get(self, request):
        launches = Launch.objects.all().values()
        for launch in launches:
            launch['comments'] = Comment.objects.filter(launch_id=str(launch['id'])).values()
        return Response({'launches': launches})
