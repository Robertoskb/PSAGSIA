from django.views.generic.edit import FormView
from .forms import SignUpForm
from profiles.models import Profile
from django.urls import reverse_lazy


class SignUpView(FormView):
    template_name = 'profiles/pages/profile_register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('profiles:create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Cadastro de Usuário'

        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['profile'] = '3'

        return initial

    def form_valid(self, form):
        user = form.save()

        profile = form.cleaned_data['profile']
        registration = form.cleaned_data['registration']
        profile = Profile(user=user, profile=profile,
                          registration=registration)
        profile.save()

        return super().form_valid(form)
