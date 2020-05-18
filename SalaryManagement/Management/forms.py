from django import forms


class SalaryMonthYear(forms.Form):
    month = forms.CharField(label='Month', max_length=100)
    year = forms.CharField(label='Year', max_length=100)

class TimeSheetform(forms.Form):
    date = forms.DateField(label='date')
    working = forms.CharField(label='Status',max_length=10)

class CsvForm(forms.Form):
    csv_file = forms.FileField()
