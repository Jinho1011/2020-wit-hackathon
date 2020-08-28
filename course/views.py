from django.shortcuts import render, redirect
from django.views import View


class CourseView(View):
    def get(self, request, *argc, **kwargs):
        return 'asd'
        # context = {
        #     'data': self.data,
        # }
        # return render(request, self.template_name, context)

    def post(self, request, *argc, **kwargs):
        result = request.POST
        print(result)
        # context = {
        #     'data': self.data,
        #     'result': result,
        # }
        # return render(request, self.template_name, context)
