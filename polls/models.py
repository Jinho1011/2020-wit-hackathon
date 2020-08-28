from django.db import models

# Create your models here.
#과목명, 과목코드 제출
class SubjectRegister(models.Model):
    subject_name = models.CharField(max_length=50) # 과목이름
    subject_code = models.CharField(max_length=10) # 과목코드
    #sunject_num = models.IntegerField(default=0) # 최소인원 등록 해야함.?
    #현재인원 등록 해야함.?
    def __str__(self): #이름으로출력.
        return self.subject_name

class SubjectChoice(models.Model):
    #name = models.ForeignKey(SubjectRegister, on_delete=models.CASCADE)
    #name = models.CharField(max_length=50)
    code = models.ForeignKey(SubjectRegister, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name
