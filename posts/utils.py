from posts.models import Role, Profile


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
            context['profile'] = Profile.objects.filter(user=self.request.user).first()
        return context
