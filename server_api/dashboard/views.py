from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage
# from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView

import math
import logging
# Create your views here.
logger = logging.getLogger('devops')


def dashboard(request: HttpRequest, *args, **kwargs):
    # print(request.META)
    # print(request.scheme)
    # print(request.body)
    # print(request.path)
    # print(request.encoding)
    print(kwargs.get('name'))
    return HttpResponse('hello world')

def articles(request, *args, **kwargs):
    print(args)
    data = {
        'test': 'test result',
        'year': kwargs.get('year'),
        'month': kwargs.get('month'),
        'day': kwargs.get('day'),
        'name': kwargs.get('name', '没有名字')
    }
    return JsonResponse(data)

class UserPage(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        print(request.body, 'body')
        try:
            page = int(request.GET.get('page', 1))
            page = 1 if page <= 0 else page
        except Exception as e:
            print(e)
            page = 1

        size = 10
        print(page, 'page num ~~~~~~~~~~~~')
        user = User.objects.all()
        print(user, 'querySet value ................')
        user_counts = user.count()
        total_page = math.ceil(user_counts / size)
        start = (page - 1) * size
        end = start+size
        users = user[start: end]
        user_msg = list(users.values('id', 'username', 'email'))
        print(user_msg)
        ret = {
            'total_pages': total_page,
            'current_page': page,
            'every_page_size': 10,
            'current_page_users': user_msg
        }

        return JsonResponse(ret)


class UserInfo(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        print(request.body, 'body')
        user_id = int(kwargs.get('user_id'))
        print(user_id)
        try:
            user = User.objects.get(id=user_id)
            print(user, '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            ret = {
                "user": {
                    'id': user_id,
                    'name': user.username,
                    'email': user.email
                }
            }
            return JsonResponse(ret)
        except ObjectDoesNotExist as e:
            print(e)
            return JsonResponse({}, status=404)


class UserTest(View):

    def get(self, request: HttpRequest, *args, **kwargs):

        logger.debug('debug User test')
        try:
            page = int(request.GET.get('page', 1))
            if page <= 0:
                page = 1
        except Exception as e:
            print(e)
            page = 1

        size = 10
        user_obj = User.objects.all()
        pagin = Paginator(user_obj, size)
        total = pagin.count
        total_page = pagin.num_pages
        print(pagin.page_range, 'range..................')
        start_page = 1
        end_page = total_page

        try:
            page = pagin.page(page)
        except EmptyPage as e:
            page = pagin.page(1)

        nextpage =  page.next_page_number() if page.has_next() else None
        prevpage = page.previous_page_number() if page.has_previous() else None

        # print(page.object_list)
        logger.warning('warnging User test {}'.format(nextpage))
        r = []
        for user in page.object_list:
            tmp = {}
            tmp['id'] = user.id
            tmp['name'] = user.username
            tmp['email'] = user.email
            r.append(tmp)

        result = {
            'pre': size,
            'total': total,
            'page': page.number,
            'total_page': total_page,
            'start_page': start_page,
            'end_page': end_page,
            'nextpage': nextpage,
            'prevpage': prevpage,
            'page_info': r,
        }
        return JsonResponse(result)


class Temp(TemplateView):
    template_name = 'temp_test.html'

    def get_context_data(self, **kwargs):
        logger.info('info Template View test')
        context = super(__class__, self).get_context_data(**kwargs)
        context['latest_articlesa'] = User.objects.all()[:5]
        logger.error('error Template View test')
        return context

class UserListView(ListView):
    template_name = 'temp_list.html'
    model = User
    paginate_by = 10