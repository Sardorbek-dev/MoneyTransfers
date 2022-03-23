from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

# Create your models here.

uzbekistan = 'Uzbekistan'
germany = 'Germany'

UZ_0 = 'Toshkent shahri'
UZ_1 = 'Toshkent viloyati'
UZ_2 = 'Farg\'ona vodiysi'
UZ_3 = 'Samarqand'
UZ_4 = 'Farg\'ona'
UZ_5 = 'Namangan'
UZ_6 = 'Andijon'
UZ_7 = 'Guliston'
UZ_8 = 'Jizzax'
UZ_9 = 'Qashqadaryo'
UZ_10 = 'Surxondaryo'
UZ_11 = 'Navoiy'
UZ_12 = 'Xorazm'
UZ_13 = 'Buxoro'
UZ_14 = 'Qoraqalpog\'iston'

GER_0 = 'Stadt München'
GER_1 = 'Stadt Berlin'
GER_2 = 'Stadt Hamburg'
GER_3 = 'Stadt Köln'
GER_4 = 'Stadt Frankfurt'
GER_5 = 'Bayern'
GER_6 = 'Baden Württemberg'
GER_7 = 'Bremen'
GER_8 = 'Brandenburg'
GER_9 = 'Hessen'
GER_10 = 'Mecklenburg-Vorpommern'
GER_11 = 'Niedersachsen'
GER_12 = 'Nordrhein Westfalen'
GER_13 = 'Rheinland Pfalz'
GER_14 = 'Sachsen'
GER_15 = 'Sachsen-Anhalt'
GER_16 = 'Saarland'
GER_17 = 'Schleswig Holstein'
GER_18 = 'Thüringen'




LOCATION_CHOICES = [
    (uzbekistan, uzbekistan),
    (germany, germany),
]

CITY_CHOICES = [
    (UZ_1, UZ_1),
    (UZ_2, UZ_2),
    (UZ_3, UZ_3),
    (UZ_4, UZ_4),
    (UZ_5, UZ_5),
    (UZ_6, UZ_6),
    (UZ_7, UZ_7),
    (UZ_8, UZ_8),
    (UZ_9, UZ_9),
    (UZ_10, UZ_10),
    (UZ_11, UZ_11),
    (UZ_12, UZ_12),
    (UZ_13, UZ_13),
    (UZ_14, UZ_14),
    (GER_0, GER_0),
    (GER_1, GER_1),
    (GER_2, GER_2),
    (GER_3, GER_3),
    (GER_4, GER_4),
    (GER_5, GER_5),
    (GER_6, GER_6),
    (GER_7, GER_7),
    (GER_8, GER_8),
    (GER_9, GER_9),
    (GER_10, GER_10),
    (GER_11, GER_11),
    (GER_12, GER_12),
    (GER_13, GER_13),
    (GER_14, GER_14),
    (GER_15, GER_15),
    (GER_16, GER_16),
    (GER_17, GER_17),
    (GER_18, GER_18),
]


def get_uz_strings():
    uz_strings = [
        UZ_1,
        UZ_2,
        UZ_3,
        UZ_4,
        UZ_5,
        UZ_6,
        UZ_7,
        UZ_8,
        UZ_9,
        UZ_10,
        UZ_11,
        UZ_12,
        UZ_13,
        UZ_14,
    ]

    return uz_strings


def get_ger_strings():
    ger_strings = [
        GER_0,
        GER_1,
        GER_2,
        GER_3,
        GER_4,
        GER_5,
        GER_6,
        GER_7,
        GER_8,
        GER_9,
        GER_10,
        GER_11,
        GER_12,
        GER_13,
        GER_14,
        GER_15,
        GER_16,
        GER_17,
        GER_18,
    ]

    return ger_strings


class Transfer(models.Model):
    title = models.CharField(max_length=255, verbose_name="Transfer nomi",)
    description = RichTextField(verbose_name="Transfer bo'yicha batafsil ma'lomot")
    # os_choice = (
    #     ('UZB', 'O\'zbekistondan Germaniyaga'),
    #     ('GER', 'Germaniyadan O\'zbekistonga'),
    #     ('UZBUSA', 'O\'zbekistondan Amerikaga'),
    #     ('USAUZB', 'Amerikadan O\'zbekistonga'),
    #     ('JPYUZB', 'Yaponiyadan O\'zbekistonga'),
    #     ('UZBJPY', 'O\'zbekistondan Yaponiyaga'),
    #     ('KORUZB', 'Koreyadan O\'zbekistondan'),
    #     ('UZBKOR', 'O\'zbekistondan Koreyaga'),
    #     ('TURUZB', 'Turkiyadan O\'zbekistonga'),
    #     ('UZBTUR', 'O\'zbekistondan Turkiyaga'),
    #     ('FRAUZB', 'Fransiyadan O\'zbekistonga'),
    #     ('UZBFRA', 'O\'zbekistondan Fransiyaga'),
    #     ('SHWUZB', 'Shvetsariyadan O\'zbekistonga'),
    #     ('UZBSHW', 'O\'zbekistondan Shvetsariyaga'),
    #     ('UZBITA', 'O\'zbekistondan Italiyaga'),
    #     ('POLUZB', 'Polshadan O\'zbekistonga'),
    #     ('UZBPOL', 'O\'zbekistondan Polshaga'),
    #     ('CHEXUZB', 'Chexiyadan O\'zbekistonga'),
    #     ('UZBCHEX', 'O\'zbekistondan Chexiyaga'),
    #     ('CANUZB', 'Canadadan O\'zbekistonga'),
    #     ('UZBCAN', 'O\'zbekistondan Canadaga'),
    #     ('AUSTUZB', 'Australiyadan O\'zbekistonga'),
    #     ('UZBAUST', 'O\'zbekistondan Australiyaga'),
    #     ('AUSUZB', 'Avstriyadan O\'zbekistonga'),
    #     ('UZBAUS', 'O\'zbekistondan Avstriyaga'),
    # )
    # location = models.CharField(max_length=100, choices=os_choice, verbose_name='Pul yuboriladigan davlatni tanlang')
    os_choice2 = (
        ('dollar', 'faqat dollarda kerak'),
        ('som', 'faqat sömda kerak'),
        ('euro', 'faqat euroda kerak'),
        ('euroordollar', 'euro yoki dollarda kerak'),
        ('euroorsom', 'euro yoki sömda kerak'),
        ('somordollar', 'dollar yoki sömda kerak'),
        ('irrelevant', 'farqi yo\'q'),
    )
    moneyCurrency = models.CharField(max_length=50, choices=os_choice2, verbose_name="Transfer pul birligini tanlang")
    os_choice3 = (
        ('fasttransfer', 'Echtzeit Überweisung'),
        ('plastik', 'Plastik karta'),
        ('cash', 'Naqd pul'),
        ('paypal', 'Paypal'),
        ('normaltransfer', 'Bank hisob raqamidan (2-3 ish kuni davom etadi)'),
        ('irrelevant', 'farqi yo\'q'),
    )
    os_choice5 = (
        ('google', 'Google kurs'),
        ('investing', 'Investing.com kurs')
    )
    transferArt = MultiSelectField(choices=os_choice3, default="fasttransfer", verbose_name="Transfer turi")
    # os_choice4 = (
    #     ('toshkent', 'Toshkent'),
    #     ('tashkent_city', 'Toshkent shahri'),
    #     ('vodiy', 'Vodiy'),
    #     ('toshkent_vodiy', 'Toshkent/Vodiy'),
    #     ('samarqand_toshkent', 'Toshkent/Samarqand'),
    #     ('namangan', 'Namangan'),
    #     ('andijan', 'Andijon'),
    #     ('fergana', 'Farg\'ona'),
    #     ('guliston', 'Guliston'),
    #     ('jizzax', 'Jizzax'),
    #     ('qashqadaryo', 'Qashqadaryo'),
    #     ('surxondaryo', 'Surxondaryo'),
    #     ('samarqand', 'Samarqand'),
    #     ('navoiy', 'Navoiy'),
    #     ('buxoro', 'Buxoro'),
    #     ('xorazm', 'Xorazm'),
    #     ('qaraqalpogiston', 'Qaraqalpog\'iston'),
    #     ('nordrhein_westfalen', 'Nordrhein Westfalen'),
    #     ('bayern', 'Bayern'),
    #     ('baden_weurttemberg', 'Baden Württemberg'),
    #     ('niedersachsen', 'Niedersachsen'),
    #     ('hessen', 'Hessen'),
    #     ('rheinland_pfalz', 'Rheinland Pfalz'),
    #     ('sachsen', 'Sachsen'),
    #     ('berlin', 'Berlin'),
    #     ('schleswig_holstein', 'Schleswig Holstein'),
    #     ('brandenburg', 'Brandenburg'),
    #     ('sachsen_anhalt', 'Sachsen-Anhalt'),
    #     ('thueringen', 'Thüringen'),
    #     ('hamburg', 'Hamburg'),
    #     ('mecklenburg_vorpommern', 'Mecklenburg-Vorpommern'),
    #     ('saarland', 'Saarland'),
    #     ('bremen', 'Bremen'),
    # )
    # whichLocation = models.CharField(max_length=50, default='iltimos davlatni tanlang', choices=os_choice4, verbose_name="Qaysi shahar yoki viloyat/Bundesland ga yubormoqchisiz?")
    exchangeRate = models.CharField(max_length=50, choices=os_choice5, verbose_name="Transfer qaysi kursda amalga oshiriladi?")
    price = models.IntegerField(verbose_name="Transfer qilinadigan pul miqdori")
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(get_user_model(), related_name='transfers_like', blank=True)
    like_count = models.BigIntegerField(default='0')
    reputations = models.ManyToManyField(get_user_model(), related_name='reputations_like', blank=True)
    reputation_count = models.BigIntegerField(default='0')
    views = models.ManyToManyField(get_user_model(), related_name='transfer_views', blank=True, default=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, verbose_name='Pul yuboriladigan davlatni tanlang')
    whichLocation = models.CharField(max_length=50, choices=CITY_CHOICES, verbose_name="Qaysi shahar yoki viloyat/Bundesland ga yubormoqchisiz")

    def get_likes(self):
        return self

    def get_reputations(self):
        return self

    def total_likes(self):
        return self.likes.count() # just count all likes

    def total_reputations(self):
        return self.reputations.count() # just count all reputations

    def total_views(self):
        return self.views.count()  # just count all views

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('transfer_detail', args=[str(self.id)])



class TransferComment(models.Model):
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, related_name='transfer_comments')
    date = models.DateField(auto_now_add=True)
    reply = models.ForeignKey('TransferComment', null=True, default=None, related_name="transfer_replies", on_delete=models.CASCADE)
    transfer_comment = models.TextField(max_length=150, default='',)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '%s - %s' % (self.transfer.title, self.transfer_comment)

    # def get_absolute_url(self):
    #     return reverse('transfer_list', args=[str(self.id)])
    #
