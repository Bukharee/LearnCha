from rest_framework import permissions


class IsStaffPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if not user.is_staff:
            return False
        return super().has_permission(request, view)
    # def has_permission(self, request, view):
        # user = request.user
        # print(user.get_all_permissions())
        # print(user.is_staff)
        # if user.is_staff:
        #     print("im staff")
        #     print("add", user.has_perm("Api.view_Product"))
        #     if user.has_perm("Api.add_Product"):
        #         return True
        #     if user.has_perm("Api.delete_Product"):
        #         return True
        #     if user.has_perm("Api.change_Product"):
        #         return True
        #     if user.has_perm("Api.view_Product"):
        #         print("zan iya viewing")
        #         return True
        #     return False
        # return False
