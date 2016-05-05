# coding:utf8
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext,loader,Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

#导入表单类
from asset.form1 import *

from asset.models import HostList   ##导入所有主机的模型

from omsknight import settings




def host_list(request):
    """
    显示所有主机
    """
    # user = request.user

    #获取所有的主机对象
    listhost = HostList.objects.all()
    aa = {'name':'knight','sex':'man'}

    # bb = {'pp':posts}
    t = loader.get_template("host_list1.html")
    c = Context({'list':listhost})

    #使用内置的分页类
    # paginator = Paginator(all_host,10)
    # return HttpResponse(posts)
    #return HttpResponse(t.render(c))
    return HttpResponse(t.render(c))





    # try:
    #     page = int(request.GET.get('page','1'))
    # except ValueError:
    #     page = 1
    #
    # try:
    #     all_host = paginator.page(page)
    # except :
    #     all_host = paginator.page(paginator.num_pages)

    # return render_to_response('host_list.html', {'all_host_list': all_host, 'page': page, 'paginator':paginator})
