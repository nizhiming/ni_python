from django.db import models

# Create your models here.
 
class Test(models.Model):
    name = models.CharField(max_length=20)
    
class Contact(models.Model):
    name  = models.CharField(max_length=200)
    age   = models.IntegerField(default=0)
    email = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)  # 原教程写成：
                                                                    #   contact = models.ForeignKey(Contact)
                                                                    # 但是这样总是报错：
                                                                    #   TypeError: __init__() missing 1 required positional argument: 'on_delete'
                                                                    # 感觉是缺少一个参数，也不知道缺少啥，就随便加一个参数：
                                                                    #   contact = models.ForeignKey(Contact，0)
                                                                    # 这样可以不报错，能运行，但一旦运行到Tag里面界面就会报错：
                                                                    #   TypeError: 'int' object is not callable
                                                                    # 报错信息指向deletion.py 222,应该是删除操作时出了问题，且调用第二各参数时，因为写的是0而无法调用
                                                                    # 搜索了半天也没见谁对这个问题解答过，最后看人家解决其他问题时，写ForeignKey时写成了：
                                                                    #   user=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='info')
                                                                    # 所以在ForeignKey中就添加了参数on_delete=models.CASCADE，写成：
                                                                    #   contact = models.ForeignKey(Contact，on_delete=models.CASCADE)
                                                                    # 测试通过。
                                                                    # 虽然教程中没有让添on_delete参数，我也还没有明白为什么，但确实添加了on_delete=models.CASCADE解决了此问题！
                                                                    # 20170627
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

