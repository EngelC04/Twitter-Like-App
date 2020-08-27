import random
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404, JsonResponse
from django.utils.http import is_safe_url

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Profile


User = get_user_model()
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# @api_view(['POST'])
# @permission_classes([IsAuthenticated]) #REST API course
# def user_profile_detail_view(request, username, *args, **kwargs):
#     current_user = request
#     to_follow_user = 
#     return Response({}, status = 200)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated]) #REST API course
def user_follow_view(request, username, *args, **kwargs):
    me = request.user
    other_user_qs = User.objects.filter(username=username)
    profile = Profile.objects.filter(user__username=username).first()
    if not other_user_qs.exists():
        return Response({}, status = 400)
    other = other_user_qs.first()
    profile = other.profile
    data = {}
    try:
        data = request.data
    except:
        pass
    print(data)
    action = data.get("action")
    if action == "follow":
        profile.followers.add(me)
    elif action == "unfollow":
        profile.followers.remove(me)
    else:
        pass
    current_followers_qs = profile.followers.all()
    return Response({"count":current_followers_qs.count()}, status = 400)

    if me in profile.followers.all():
        profile.followers.remove(me)
    else:
        profile.followers.add(me)
    return Response({"followers":profile.followers.all()}, status = 400)
