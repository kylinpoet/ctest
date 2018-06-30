from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50,blank=True)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
    def __str__(self):
        return self.name

class Choices(models.Model):
    OPTI_CHOICE=( ('a','a'),('b','b'),('c','c'),('d','d')  )
    BODY_SELECT=(  ('selected','已选定'),('deselect','未选定')  )
    body = models.TextField(unique=True,verbose_name='题目')
    pic = models.ImageField(upload_to='imgfiles',blank=True,verbose_name='图片')
    rightanswer = models.CharField(max_length=2,choices=OPTI_CHOICE,verbose_name='答案')
    detail = models.TextField(blank=True,verbose_name='解答')
    creattime = models.DateTimeField(auto_now_add=True)
    bodyselect = models.CharField(max_length=8, choices=BODY_SELECT, default='deselect',verbose_name='选定')
    bssort = models.IntegerField(blank=True,default=1,verbose_name='题目次序')
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = '题目'

    def __str__(self):
        return self.body

class Cresult(models.Model):
    question = models.ForeignKey(Choices,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sname = models.CharField(max_length=8,verbose_name='学生姓名')
    answer = models.CharField(max_length=2,verbose_name='学生回答')
    answerdetail = models.CharField(max_length=256,blank=True,verbose_name='理由')
    answerstate = models.NullBooleanField()
    answertime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '答案'
        verbose_name_plural = '答案'


    def __str__(self):
        return self.answer


# Create your models here.
