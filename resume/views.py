from django.views.generic import TemplateView


class ResumeView(TemplateView):
    template_name = "resume/index.html"
