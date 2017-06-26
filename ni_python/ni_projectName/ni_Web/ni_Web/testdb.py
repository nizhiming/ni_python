# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    # 操作码
    integer1 = input('请输入一个操作码[1,4]:')
    donumber = int(integer1)
    integer2 = input('请输入一个id:')
    id_num = int(integer2)
    
    if donumber == 1:
        '''<1> 添加数据：'''
        test0 = Test.objects.filter(id=id_num)
        if bool(test0):
            return HttpResponse("<p>数据已经存在！</p>")
        else:
            test1 = Test(name='runoob',id = id_num)
            test1.save()
            return HttpResponse("<p>数据添加成功！</p>")
        
    elif donumber == 2:
        '''<2> 获取数据: '''
        # 初始化
        response = " "
        response1 = ""
        
        # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT*FROM
        list = Test.objects.all()
        
        # 判断是否是空数据
        if Test.objects.count() < 1:    # 判断数据库中的个数
            return HttpResponse("<p>获取数据库中没有数据！</p>")
        
        # filter相当于SQL中的WHERE，可设置条件过滤结果
        response2 = Test.objects.filter(id=id_num)
        if bool(response2):
            # 获取单个对象
            response3 = Test.objects.get(id=id_num)
            response = response3.name
            
            # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2
            Test.objects.order_by('name')[0:2]
            
            # 数据排序
            Test.objects.order_by("id")
            
            return HttpResponse("<p>获取数据名字：" + response + "</p>")
        else:
            # 上面4步的方法可以连锁使用，上面4不可合成
            Test.objects.filter(name="runoob").order_by("id")
            
            # 输出所有数据
            for var in list:
                response1 += "    " + var.name + "_" + str(var.id) + "<br>"
                # len(l)
            response = response1
        
            return HttpResponse("<p>" + "<b>数据库中不存在id=" + integer2 + "的数据</b><br>" + "数据库中存在的数据：<br>    名字_id<br>" + response + "</p>")
    
    elif donumber == 3:
        ''' <3> 更新数据库 '''
        # 修改数据可以使用 save() 或 update():
        
        # 判断数据库中是否存在id=1的数据
        test0 = Test.objects.filter(id=id_num)
        if bool(test0):
            # 修改其中一个id-1的name字段，再save，相当于SQL中的UPDATE
            test1 = Test.objects.get(id=id_num)
            test1.name = 'xiaominger'
            test1.save()
            
            # 另一种方式
            #Test.objects.filter(id=id_num).uodate(name='xiaominger')
            
            # 修改所有的列
            #Test。objects.all().update(name='xiaominger')
            
            return HttpResponse("<p>修改成功！</p>")
        else:
            return HttpResponse("<p>不存在有且只有一个id=1的数据！</p>")
            
    elif donumber == 4:
        ''' <4>删除数据  '''
        # 删除数据库中的对象只需要调用该对象的delete()方法即可：
        
        # 判断数据库中是否存在id=1的数据
        test0 = Test.objects.filter(id=id_num)
        if bool(test0):
            # 删除id=1的的数据
            test1 = Test.objects.get(id=id_num)
            test1.delete()
            
            # 另一种方式
            #Test.objects.filter(id=1).delete()
            
            return HttpResponse("<p>删除成功！</p>")
        else:
            # 删除所有数据
            #Test.objects.all().delete()    
            return HttpResponse("<p>不存在有且只有一个id=1的数据！</p>")
            
            
    else:
        return HttpResponse("<p>请输入正确的执行码：<br>1:添加数据<br>2:获取数据<br>3:更改数据<br>4:删除数据</p>")