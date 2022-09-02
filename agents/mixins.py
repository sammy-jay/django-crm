from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect, reverse

class CustomLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.user_type != 'O':
            return redirect(reverse('leads:index'))
        return super().dispatch(request, *args, **kwargs)