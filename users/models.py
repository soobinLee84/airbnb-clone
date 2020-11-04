from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# mgriation 하는법
# python filename.py migrations
# python filename.py migrate

# 데이터베이스에 default 값을 넣어줘야
# Migration 했을때 빈공간없이 default 값으로 채워준다.아니면 null 값으로 채운다.
# 이와같이 하면 column이 설정되기전에 값들이 채워진다.


# 상속의 개념
# AbstractUser안에 있는 모든것을 User로 복붙해준다.admin도 마찬가지
class User(AbstractUser):

    """ Custome User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "english"), (LANGUAGE_KOREAN, "korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # image 데이터를 처리하는 pillow(파이썬 이미지 라이브러리) 필수 설치
    # pipenv install pillow
    # blank는 웹프론트 단의 null 이라생각하면된다
    # null 값을 허용해도 프론트에서는 필수사항이라는 이유가 db에서만 null 허용이기에 blank를 써야 완벽한 null허용이 된다.
    # blank를 설정해야 form에 적용된다.
    # migrations는 항상 적게 유지하는것이 좋다
    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    """
    CharField = 셀렉트 박스
    TextField = 텍스트박스
    ImageField = 파일추가 박스
    BooleanField = 체크박스
    DateField = 데이트 선택 필드박스(달력형태로 ui 구성)
    클래스 BooleanField
    참/거짓필드.
    이 필드에 위젯의 기본 형태는 CheckbocInput, 또는 NullBooleanSelect경우
    null=True의 기본값은 BooleanFiled입니다. None때 Field.default 정의되지 않았습니다.
    check_box = BooelanField를 체크박스라고 생각하면된다.
    체크된거면 True 체크 안된 거면 False 값을 가진다. 

    **configuration : (=set up) 환경설정과 같은것이다.
    """
    superhost = models.BooleanField(default=False)

