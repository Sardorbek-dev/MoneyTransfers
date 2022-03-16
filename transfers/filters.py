import django_filters
from .models import Transfer
from django.db import models
from django import forms

class TransferFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label='Transfer nomi', widget=forms.TextInput(attrs={'class': 'form-control'}), lookup_expr='icontains')

    #location = django_filters.CharFilter(label='davlat qisqartmasi(UZB/GER/USA)', lookup_expr='icontains')
    test_prices = (
        ('0100', '0 - 100'),
        ('100200', '100 - 200'),
        ('200500', '200 - 500'),
        ('5001000', '500 - 1000'),
        ('10002000', '1000 - 2000'),
        ('20005000', '2000 - 5000'),
        ('500000000', '5000 - ...'),
    )

    # test=7500
    # price = django_filters.ModelMultipleChoiceFilter(queryset=Transfer.objects.filter(price=test), widget=forms.CheckboxSelectMultiple)
    CHOICES = (
        ('ascending', 'Ösish tartibida'),
        ('descending', 'Kamayish tartibida')
    )

    CHOICES2 = (
        ('GER', 'O\'zbekiston'),
        ('UZB', 'Germaniya')
    )

    # CHOICES3 = (
    #     ('fasttransfer', 'Echtzeit Überweisung'),
    #     ('plastik', 'Plastik karta'),
    #     ('cash', 'Naqd pul'),
    #     ('paypal', 'Paypal'),
    #     ('normaltransfer', 'Bank hisob raqamidan (2-3 ish kuni davom etadi)'),
    #     ('irrelevant', 'farqi yo\'q'),
    # )
    #

    # selected_transfer_art = django_filters.MultipleChoiceFilter(label='Transfer turi', choices=CHOICES3, method='filter_transfer_art')

    price = django_filters.ChoiceFilter(label='Transfer miqdori', choices=test_prices, method='filter_by_price')
    ordering_price = django_filters.ChoiceFilter(label='Pul o\'tkazmasi qiymati', choices=CHOICES, method='filter_by_order')
    selected_location = django_filters.ChoiceFilter(label='Pul yuboriladigan davlat', choices=CHOICES2, method='filter_location')

    # class Meta:
    #     model = Transfer
    #     fields = {
    #         'location': ['icontains'],
    #     }

    def filter_by_price(self, queryset, name, value):
        if value == '0100':
            return queryset.filter(price__gt=0, price__lt=100)
        if value == '100200':
            return queryset.filter(price__gt=100, price__lt=200)
        if value == '200500':
            return queryset.filter(price__gt=200, price__lt=500)
        if value == '5001000':
            return queryset.filter(price__gt=500, price__lt=1000)
        if value == '10002000':
            return queryset.filter(price__gt=1000, price__lt=2000)
        if value == '20005000':
            return queryset.filter(price__gt=2000, price__lt=5000)
        if value == '500000000':
            return queryset.filter(price__gt=5000)

    def filter_by_order(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)

    def filter_location(self, queryset, name, value):
        if value == 'GER':
            expression_location = 'GER'
            return queryset.filter(location=expression_location)
        else:
            expression_location = 'UZB'
            return queryset.filter(location=expression_location)

    # def filter_transfer_art(self, queryset, name, value):
    #
    #     if value == 'fasttransfer':
    #         filter_transfer = 'fasttransfer'
    #         print(value)
    #         return queryset.filter(transfer_turi=filter_transfer)
    #     else:
    #         filter_transfer = 'plastik'
    #         return queryset.filter(transfer_turi=filter_transfer)



