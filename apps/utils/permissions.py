#!/usr/bin/env python
# _*_ coding:utf8 _*_ 
__date__ = '2017/10/26 21:13'
__author__ = 'zhourudong'

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.


    """

    def has_object_permission(self, request, view, obj):
        # 判断这个对象    是否
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user   # 如果没有权限则返回false
