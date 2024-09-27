from api.permissions import IsStaffPermission
from rest_framework import permissions


class StaffEditorPermissionMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]
    
class UserQuerySetMixins():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query_data = {self.user_field: self.request.user}
        # sans ** on aura qs.filter({'user': self.request.user})
        # ** signifie que: qs.filter(user=self.request.user)
        return qs.filter(**query_data)