from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.http import QueryDict
from urllib import parse
import course.courseList


class CourseView(View):
    template_name = 'course/course_index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        openSust = request.POST['openSust']
        pobtDiv = request.POST['pobtDiv']
        sbjtId = request.POST['sbjtId']
        sbjtNm = request.POST['sbjtNm']

        courseInfo = {
            openSust, pobtDiv, sbjtId, sbjtNm
        }

        return render(request, self.template_name, {
            'object_list': courseInfo
        })
