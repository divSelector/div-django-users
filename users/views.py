from django.views.generic.detail import DetailView


class UserView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user
