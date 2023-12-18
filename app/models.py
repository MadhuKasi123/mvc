from django.db import models
# Create your models here.
class Dept(models.Model):
    DeptNo=models.IntegerField(max_length=10,primary_key=True)
    Dname=models.CharField(max_length=100,unique=True)
    Loction=models.CharField(max_length=30,null=False)
    
    def __str__(self):
        return str(self.DeptNo)
    
   


class Emp(models.Model):
    
    Ename=models.CharField(max_length=100,null=False)
    Eid=models.IntegerField(max_length=100,primary_key=True)
    DeptNo=models.ForeignKey(Dept,on_delete=models.CASCADE)
    Sal=models.IntegerField(max_length=10,null=False)
    def __str__(self):
        return self.Ename

   

   