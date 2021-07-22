from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    choices=(
        ("STUDENT","STUDENT"),
        ("PROFESSOR","PROFESSOR")

    )

    user_type=models.CharField(choices=choices,max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
         unique_together=(('user_type','email'),('user_type','mobile'))
class StudentModel(models.Model):
    stu_id=models.AutoField(primary_key=True)
    user_id=models.OneToOneField('UserModel',on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    dob=models.DateField()
    std_choices=(
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),
    )
    std=models.CharField(choices=std_choices,max_length=100)
    caste_choices=(
        ("OPEN","OPEN"),
        ("OBC","OBC"),
        ("OTHER","OTHER"),
     )
    caste=models.CharField(choices=caste_choices,max_length=100)
    city=models.CharField(max_length=100)
    spe_choices=(
        ("GENERAL", "GENERAL"),
        ("SCIENCE", "SCIENCE"),
        ("COMMERCE", "COMMERCE"),
        ("ARTS","ARTS")
         )
    specilization=models.CharField(choices=caste_choices,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Professor(models.Model):
    professor_id=models.AutoField(primary_key=True)
    user_id = models.OneToOneField('UserModel', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    professor_specilization=models.CharField(max_length=100)




