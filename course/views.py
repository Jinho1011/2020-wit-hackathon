from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.http import QueryDict
from urllib import parse
import urllib.parse
from . import courseList
from . import courseDetail


class CourseListView(View):
    template_name = 'course/course_index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        openSust = request.POST['openSust']
        pobtDiv = request.POST['pobtDiv']
        sbjtId = request.POST['sbjtId']
        sbjtNm = request.POST['sbjtNm']

        courseInfo = {
            'openSust': openSust, 'pobtDiv': pobtDiv, 'sbjtId': sbjtId, 'sbjtNm': parse.quote(sbjtNm)
        }

        object_list = courseList.main(courseInfo)

        return render(request, self.template_name, {
            'object_list': object_list
        })


class CourseDetailView(View):
    template_name = 'course/course_detail.html'

    def get(self, request, *args, **kwargs):
        object_list = courseDetail.main(self.kwargs['number'])

        return render(request, self.template_name, {
            'object_list': object_list
        })
