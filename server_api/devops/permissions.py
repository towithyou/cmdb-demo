from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class Permission(DjangoModelPermissions):


    def get_custom_perms(self, view, method):
        print(view, method, '+++++++')
        extra_perm_map = getattr(view, 'extra_perm_map', [])
        return extra_perm_map.get(method, []) if isinstance(extra_perm_map, dict) else []


    def has_permission(self, request, view):

        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
                not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        perms.extend(self.get_custom_perms(view, request.method))
        print(perms, '---------------')
        return request.user.has_perms(perms)