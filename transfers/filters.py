import django_filters
from .models import Transfer
from django.db import models
from django import forms

class TransferFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label='Transfer nomi', widget=forms.TextInput(attrs={'class': 'form-control'}), lookup_expr='icontains')

    #location = django_filters.CharFilter(label='davlat qisqartmasi(UZB/GER/USA)', lookup_expr='icontains')
    test_prices = (
        ('0100', '0 - 99 €'),
        ('100200', '100 - 199 €'),
        ('200500', '200 - 499 €'),
        ('5001000', '500 - 999 €'),
        ('10002000', '1000 - 1999 €'),
        ('20005000', '2000 - 4999 €'),
        ('500000000', '5000 € - ...'),
    )

    # test=7500
    # price = django_filters.ModelMultipleChoiceFilter(queryset=Transfer.objects.filter(price=test), widget=forms.CheckboxSelectMultiple)
    CHOICES = (
        ('ascending', 'Ösish tartibida'),
        ('descending', 'Kamayish tartibida')
    )

    CHOICES2 = (
        ('UZB', 'O\'zbekiston'),
        ('GER', 'Germaniya')
    )

    CHOICES3 = (
        ('fasttransfer', 'Echtzeit Überweisung'),
        ('plastik', 'Plastik karta'),
        ('cash', 'Naqd pul'),
        ('paypal', 'Paypal'),
        ('normaltransfer', 'Bank hisob raqamidan (2-3 ish kuni davom etadi)'),
        ('irrelevant', 'farqi yo\'q'),
    )


    # selected_transfer_art = django_filters.MultipleChoiceFilter(label='Transfer turi', choices=CHOICES3, method='filter_transfer_art')

    price = django_filters.ChoiceFilter(label='Transfer miqdori', choices=test_prices, method='filter_by_price')
    ordering_price = django_filters.ChoiceFilter(label='Pul o\'tkazmasi qiymati', choices=CHOICES, method='filter_by_order')
    selected_location = django_filters.ChoiceFilter(label='Pul yuboriladigan davlat', choices=CHOICES2, method='filter_location')
    checkbox_filter = django_filters.MultipleChoiceFilter(label='Transfer turi', choices=CHOICES3, method='filter_location_new')

    # class Meta:
    #     model = Transfer
    #     fields = {
    #         'location': ['icontains'],
    #     }

    def filter_by_price(self, queryset, name, value):
        if value == '0100':
            return queryset.filter(price__gte=0, price__lte=99, status_transfer=True)
        if value == '100200':
            return queryset.filter(price__gte=100, price__lte=199, status_transfer=True)
        if value == '200500':
            return queryset.filter(price__gte=200, price__lte=499, status_transfer=True)
        if value == '5001000':
            return queryset.filter(price__gte=500, price__lte=999, status_transfer=True)
        if value == '10002000':
            return queryset.filter(price__gte=1000, price__lte=1999, status_transfer=True)
        if value == '20005000':
            return queryset.filter(price__gte=2000, price__lte=4999, status_transfer=True)
        if value == '500000000':
            return queryset.filter(price__gte=5000, status_transfer=True)

    def filter_by_order(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.filter(status_transfer=True).order_by(expression)

    def filter_location(self, queryset, name, value):

        if value == 'GER':
            expression_location = 'Germany'
            return queryset.filter(location=expression_location, status_transfer=True)
        if value == 'UZB':
            expression_location = 'Uzbekistan'
            return queryset.filter(location=expression_location, status_transfer=True)

    def filter_location_new(self, queryset, name, value):
        # print('value:', list(queryset[0].transferArt), len(queryset))
        # def test_cds(expression_location):
        #     for i in range(0, len(queryset)):
        #         for transferArt in queryset[i].transferArt:
        #             if expression_location == transferArt:
        #                 return queryset[i]
        # print(test_cds('cash'))
        for i in range(0, len(value)):
            if value[i] == 'fasttransfer':
                expression_location = 'fasttransfer'
                return queryset.filter(transferArt__contains=expression_location, status_transfer=True)
            if value[i] == 'plastik':
                expression_location = 'plastik'
                return queryset.filter(transferArt__contains=expression_location, status_transfer=True)
            if value[i] == 'cash':
                expression_location = 'cash'
                return queryset.filter(transferArt__contains=expression_location, status_transfer=True)
            if value[i] == 'paypal':
                expression_location = 'paypal'
                return queryset.filter(transferArt__contains=expression_location, status_transfer=True)
            if value[i] == 'normaltransfer':
                expression_location = 'normaltransfer'
                return queryset.filter(transferArt__contains=expression_location, status_transfer=True)
            if value[i] == 'irrelevant':
                expression_location = 'irrelevant'
                return queryset.filter(transferArt__contains=expression_location, status_transfer=True)



