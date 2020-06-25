from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custome User Model """

    GENDER_FEMAIL = "female"
    GENDER_MALE = "male"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_FEMAIL, "female"),
        (GENDER_MALE, "male"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "english"), (LANGUAGE_KOREAN, "korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
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
