from .models import UserModel,StudentModel,Professor
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=100,required=False)
    dob = serializers.DateField(required=False)
    professor_specilization = serializers.CharField(max_length=100,required=False)


    choices = (
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    )
    std = serializers.CharField(required=False)

    caste_choices = (
        ("OPEN", "OPEN"),
        ("OBC", "OBC"),
        ("OTHER", "OTHER")
    )
    caste = serializers.CharField(required=False)

    city = serializers.CharField(max_length=100)

    spe_choices = (
        ("GENERAL", "GENERAL"),
        ("SCIENCE", "SCIENCE"),
        ("COMMERCE", "COMMERCE"),
        ("ARTS", "ARTS")
    )
    specilization = serializers.CharField(max_length=100,required=False)

    choices = (
        ("STUDENT", "STUDENT"),
        ("PROFESSOR", "PROFESSOR")
    )

    user_type = serializers.CharField()
    email = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    password = serializers.CharField(max_length=100)
    conf_password = serializers.CharField(max_length=100)


    def validate(self, attrs):
        if attrs['password']!=attrs['conf_password']:
            raise serializers.ValidationError("Password Missmatch")
        user_type=attrs['user_type']
        email=attrs['email']
        mobile=attrs['mobile']
        student_aatrs = {"std", "dob", "caste", "specilization", "gender"}
        professor_aatrs={"professor_specilization","city"}
        if user_type == "PROFESSOR" and professor_aatrs.intersection(set(attrs.keys())) != professor_aatrs:
            raise serializers.ValidationError(
                '"professor_specilization","city"" one of this field is missing')
        if user_type == "STUDENT" and student_aatrs.intersection(set(attrs.keys())) != student_aatrs:
            raise serializers.ValidationError(
                '"std","dob","caste","specilization","gender" one of this field is missing')
        if UserModel.objects.filter(user_type=user_type,email=email).exists():
            raise serializers.ValidationError("user_type with same email is already exist")
        if UserModel.objects.filter(user_type=user_type,mobile=mobile).exists():
            raise serializers.ValidationError("user_type with same Mobile is already exist")
        return True
    def create(self, validated_data):
        user = UserModel(
            user_type= validated_data['user_type'],
            mobile= validated_data['mobile'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        if user.user_type == "STUDENT":
            student = StudentModel(
                full_name=validated_data['full_name'],
                gender = validated_data['gender'],
                dob=validated_data['dob'],
                std=validated_data['std'],
                caste=validated_data['caste'],
                specilization=validated_data['specilization'],
                user_id=user
            )
            student.save()
        elif user.user_type == "PROFESSOR":
            professor = Professor(
            full_name = validated_data['full_name'],
            city=validated_data['city'],
            professor_specilization=validated_data['professor_specilization'],
            user_id=user

            )
            professor.save()
        return validated_data


class UserModelSerializer(serializers.ModelSerializer):

    model=UserModel
    fields=('email','mobile')


class LimitedSerializer(serializers.ModelSerializer):
    email=serializers.CharField(source="user_id.email")
    mobile=serializers.IntegerField(source="user_id.mobile")
    user_type=serializers.CharField(source="user_id.user_type")
    class Meta:

        model=StudentModel
        fields=('user_type','email','mobile','full_name','gender','specilization','city','dob','std','caste')

       # state_name = serializers.CharField(source="state_id.state_name")




class ProfessorSerializer(serializers.ModelSerializer):
    email=serializers.CharField(source="user_id.email")
    mobile=serializers.IntegerField(source="user_id.mobile")
    user_type = serializers.CharField(source="user_id.user_type")

    class Meta:
        model=Professor
        fields=('user_type','email','mobile','full_name','city','professor_specilization')

class StudentListSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user_id.email")
    mobile = serializers.IntegerField(source="user_id.mobile")
    class Meta:

        model=StudentModel
        fields=('full_name','city','email','mobile')
class ProfessorListSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user_id.email")
    mobile = serializers.IntegerField(source="user_id.mobile")

    class Meta:
        model = Professor
        fields = ('full_name', 'city', 'email', 'mobile')







