from api.permissions import IsStaffPermission
from rest_framework import permissions


class StaffEditorPermissionMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]