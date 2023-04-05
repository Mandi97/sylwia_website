from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'


class AboutMe(TemplateView):
    template_name = 'home/about_me.html'


class Contact(TemplateView):
    template_name = 'home/contact.html'
