# coding:utf-8
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext,loader,Context
from django.shortcuts import render_to_response, get_object_or_404,render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator              ##分页器

#导入数据库类为了方便
from id_sql import *

#导入表单类
from asset.form1 import *
from asset.models import HostList   ##导入所有主机的模型
from omsknight import settings

#主机编辑函数,显示所有主机
@login_required
def host_list(request):
    if request.method == "POST":
        ip1 = request.POST['ip']
        host_groupnew = request.POST['host_group'].encode('utf-8')
        statusnew = request.POST['status'].encode('utf-8')
        if ip1:                                                        #如果有值就执行
            posts = HostList.objects.filter(ip=ip1,host_group=host_groupnew,status=statusnew)
        else:
            posts = HostList.objects.filter(host_group=host_groupnew,status=statusnew)
        postn = posts
        c = Context({'list': postn})
        return render_to_response('host_list.html', c)

##不是post如下:
    page = request.GET.get('page', '')  # 获取key对应的值,也就是page后的变量
    ##try发生异常就执行except语句
    try:
        page_num = int(page)
    except:
        page_num = 0

    posts = HostList.objects.all()
    postn = posts[page_num * 5:(page_num + 1) * 5]     # 5代表一页显示的记录数量

    c = Context({'list':postn})

    return render_to_response('host_list.html',c)



##点击编辑展开详细页面
def detail(request, id):

    listhost = HostList.objects.all()
    h_id = get_object_or_404(HostList, pk=id)

    if request.method == 'GET':
        # listhost = HostList.objects.all()
        # h_id = get_object_or_404(HostList, pk=id)
        return render(request, 'detail.html', {'h_ids': h_id})


    if request.method == 'POST':
        ipnew = request.POST['ip']           #获取表单传过来的值
        hostnamenew = request.POST['hostname']
        applicationnew = request.POST['application']
        remarknew = request.POST['remark']
        host_groupnew = request.POST['host_group'].encode('utf-8')

        # 更新数据表,过了出字段然后update
        #ip=ipnew,  id要设置主键 并且自动递增
        b = HostList.objects.filter(ip=h_id.ip).update(hostname=hostnamenew,application=applicationnew,remark=remarknew,host_group=host_groupnew)

        # return HttpResponse(u"已经通过post方式提交更新数据到数据库中....")
        return HttpResponseRedirect('/list/')

def create_host(request):
    listhost = HostList.objects.all()

    if request.method == 'GET':
        return render(request, 'create_host.html')

#创建对象并保存到数据库中
    if request.method == 'POST':
        sql = "SELECT COUNT(id) from asset_hostlist"
        # 获取所有记录列表
        cursor.execute(sql)
        results = cursor.fetchall()  ##是个元组
        ss = str(results)
       # ss2_1 = int(ss[2])+1


        ##定义表单内容
        ipnew = request.POST['ip']
        hostnamenew = request.POST['hostname']
        productnew = request.POST['product']
        applicationnew = request.POST['application']
        idc_jgnew = request.POST['idc_jg']
        statusnew = request.POST['status']
        remarknew = request.POST['remark']
        host_groupnew = request.POST['host_group'].encode('utf-8')     #中文要encode 要把unicode字符串编码成字符串

        ##表单插入数据
        c = HostList.objects.create(ip=ipnew,hostname=hostnamenew,product=productnew,application=applicationnew,idc_jg=idc_jgnew,status=statusnew,remark=remarknew,host_group=host_groupnew)
        c.save()
        # return HttpResponse(u"你已经成功的通过post表单方式添加到了数据库")
        return HttpResponseRedirect('/list/')


##定义删除主机按钮
def delete_host(request,id):
    #ids eq :  1,2,3,4
    ids = id.split(",")   #处理前台传过来的值
    for i in ids:
        HostList.objects.filter(id=i).delete()  ##删除指定数据
    return HttpResponseRedirect('/list/')


##后台首页
@login_required
def hindex(request):
    if not request.user.is_authenticated():
        return HttpResponse(u"请先登录...")
    return render_to_response('hindex.html')

###########数据中心资产
@login_required
def data_center(request):
    if not request.user.is_authenticated():
        return HttpResponse(u"请先登录...")
    posts = IdcAsset.objects.all()
    c = Context({'list': posts})
    return render_to_response('center.html', c)

#####网络设备资产
@login_required
def netzichan(request):
    if not request.user.is_authenticated():
        return HttpResponse(u"请先登录...")
    posts = NetworkAsset.objects.all()
    c = Context({'list': posts})
    return render_to_response('netzichan.html', c)

##后台首页
@login_required
def hindex(request):
    if request.user.is_authenticated():
        return render_to_response('hindex.html')
##软硬件信息


######使用django的后台session,测试验证而已
@login_required
def list4(request):
    if not request.user.is_authenticated():  ## 如果已经验证成功通过
        return HttpResponse(u"请先登录...")

    return render_to_response('list4.html')



