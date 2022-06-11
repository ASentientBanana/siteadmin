from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Project
from .helpers.email import send_mail

import os,json

ips_map = {}
ip_limit = 5

def get_ip(request):
    project_list = Project.objects.all().values()
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def register_ip(ip):
    if ip in ips_map:
        ips_map[ip] += 1
    else:
        ips_map[ip] = 1


def check_for_ip_limit(ip):
    if ip in ips_map:
        if ips_map[ip] < ip_limit:
            return False
    return True

def contact_handler(request):
    ip = get_ip(request)
    if check_for_ip_limit(ip):
        return False
    register_ip(ip)
    print(ips_map)
    return True

def index(request):
    project_list = Project.objects.all().values()
    return JsonResponse({'projects':list(project_list)})

@csrf_exempt
def contactMe(request):
    if request.method == 'POST':
        print("CONTACTING")
        if contact_handler(request):
            return JsonResponse({'msg':'Too many messages in one day.'})
        data = json.loads(request.body)
        send_mail(data['email'],data['message'])
        # send_mail('Portfolio Contact from '+ data['email'], data['message'],os.environ['EMAIL'],[os.environ['TARGET_EMAIL']])
        return HttpResponse(300)
    return JsonResponse({})
