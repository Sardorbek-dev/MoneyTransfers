from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

# Create your models here.
class Transfer(models.Model):
    title = models.CharField(max_length=255, verbose_name="Transfer nomi",)
    description = RichTextField(verbose_name="Transfer bo'yicha batafsil ma'lomot")
    os_choice = (
        ('UZB', 'O\'zbekistondan Germaniyaga'),
        ('GER', 'Germaniyadan O\'zbekistonga'),
        ('UZBUSA', 'O\'zbekistondan Amerikaga'),
        ('USAUZB', 'Amerikadan O\'zbekistonga'),
        ('JPYUZB', 'Yaponiyadan O\'zbekistonga'),
        ('UZBJPY', 'O\'zbekistondan Yaponiyaga'),
        ('KORUZB', 'Koreyadan O\'zbekistondan'),
        ('UZBKOR', 'O\'zbekistondan Koreyaga'),
        ('TURUZB', 'Turkiyadan O\'zbekistonga'),
        ('UZBTUR', 'O\'zbekistondan Turkiyaga'),
        ('FRAUZB', 'Fransiyadan O\'zbekistonga'),
        ('UZBFRA', 'O\'zbekistondan Fransiyaga'),
        ('SHWUZB', 'Shvetsariyadan O\'zbekistonga'),
        ('UZBSHW', 'O\'zbekistondan Shvetsariyaga'),
        ('UZBITA', 'O\'zbekistondan Italiyaga'),
        ('POLUZB', 'Polshadan O\'zbekistonga'),
        ('UZBPOL', 'O\'zbekistondan Polshaga'),
        ('CHEXUZB', 'Chexiyadan O\'zbekistonga'),
        ('UZBCHEX', 'O\'zbekistondan Chexiyaga'),
        ('CANUZB', 'Canadadan O\'zbekistonga'),
        ('UZBCAN', 'O\'zbekistondan Canadaga'),
        ('AUSTUZB', 'Australiyadan O\'zbekistonga'),
        ('UZBAUST', 'O\'zbekistondan Australiyaga'),
        ('AUSUZB', 'Avstriyadan O\'zbekistonga'),
        ('UZBAUS', 'O\'zbekistondan Avstriyaga'),
    )
    location = models.CharField(max_length=100, choices=os_choice, verbose_name='Pul yuboriladigan davlatni tanlang')
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
    transferArt = MultiSelectField(choices=os_choice3, default="fasttransfer", verbose_name="Transfer turi")
    os_choice4 = (
        ('toshkent', 'Toshkent'),
        ('tashkent_city', 'Toshkent shahri'),
        ('vodiy', 'Vodiy'),
        ('toshkent_vodiy', 'Toshkent/Vodiy'),
        ('samarqand_toshkent', 'Toshkent/Samarqand'),
        ('namangan', 'Namangan'),
        ('andijan', 'Andijon'),
        ('fergana', 'Farg\'ona'),
        ('guliston', 'Guliston'),
        ('jizzax', 'Jizzax'),
        ('qashqadaryo', 'Qashqadaryo'),
        ('surxondaryo', 'Surxondaryo'),
        ('samarqand', 'Samarqand'),
        ('navoiy', 'Navoiy'),
        ('buxoro', 'Buxoro'),
        ('xorazm', 'Xorazm'),
        ('qaraqalpogiston', 'Qaraqalpog\'iston'),
        ('nordrhein_westfalen', 'Nordrhein Westfalen'),
        ('bayern', 'Bayern'),
        ('baden_weurttemberg', 'Baden Württemberg'),
        ('niedersachsen', 'Niedersachsen'),
        ('hessen', 'Hessen'),
        ('rheinland_pfalz', 'Rheinland Pfalz'),
        ('sachsen', 'Sachsen'),
        ('berlin', 'Berlin'),
        ('schleswig_holstein', 'Schleswig Holstein'),
        ('brandenburg', 'Brandenburg'),
        ('sachsen_anhalt', 'Sachsen-Anhalt'),
        ('thueringen', 'Thüringen'),
        ('hamburg', 'Hamburg'),
        ('mecklenburg_vorpommern', 'Mecklenburg-Vorpommern'),
        ('saarland', 'Saarland'),
        ('bremen', 'Bremen'),
    )
    whichLocation = models.CharField(max_length=50, default='iltimos davlatni tanlang', choices=os_choice4, verbose_name="Qaysi shahar yoki viloyat/Bundesland ga yubormoqchisiz?")
    os_choice5 = (
        ('google', 'Google kurs'),
        ('investing', 'Investing.com kurs')
    )
    exchangeRate = models.CharField(max_length=50, choices=os_choice5, verbose_name="Transfer qaysi kursda amalga oshiriladi?")
    price = models.IntegerField(verbose_name="Transfer qilinadigan pul miqdori")
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(get_user_model(), related_name='transfers_like', blank=True)
    like_count = models.BigIntegerField(default='0')
    reputations = models.ManyToManyField(get_user_model(), related_name='reputations_like', blank=True)
    reputation_count = models.BigIntegerField(default='0')
    views = models.ManyToManyField(get_user_model(), related_name='transfer_views', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

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
