from django.http import JsonResponse
from django.db.models import Value as V
from django.db.models.functions import Concat

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import UserSerializer
from post.models import Post
from post.serializers import PostSerializer


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    users = []
    posts = []

    if query != '':
        users = (((User.objects.annotate(full_name1=Concat('name', V(' '), 'surname')).filter(full_name1__icontains=query)) |
             (User.objects.annotate(full_name2=Concat('surname', V(' '), 'name')).filter(full_name2__icontains=query))))
        posts = Post.objects.filter(body__icontains=query)

    users_serializer = UserSerializer(users, many=True)
    posts_serializer = PostSerializer(posts, many=True)

    return JsonResponse({
        'users': users_serializer.data,
        'posts': posts_serializer.data
    }, safe=False)
