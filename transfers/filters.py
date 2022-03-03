import django_filters
from .models import Transfer

class TransferFilter(django_filters.FilterSet):

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

    ordering_price = django_filters.ChoiceFilter(label='Pul o\'tkazmasi qiymati', choices=CHOICES, method='filter_by_order')
    selected_location = django_filters.ChoiceFilter(label='Pul yuboriladigan davlat', choices=CHOICES2, method='filter_location')

    class Meta:
        model = Transfer
        fields = {
            'title': ['icontains'],
            'location': ['icontains'],
            'price': ['icontains'],
        }
        labels = {
            'title': 'What is your name',
        }

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



