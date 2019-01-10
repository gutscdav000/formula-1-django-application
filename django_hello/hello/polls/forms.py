from django import forms




class TableForm(forms.Form):
    #your_name = forms.CharField(label='choice', max_length=100)
    options = [(1, 'circuits') , (2, 'constructor results'), (3, 'constructor standings'),
               (4, 'constructors'), (5, 'driver standings'), (6, 'drivers'), (7, 'lap times'),
               (8, 'pit stops'), (9, 'qualifying'), (10, 'races'), (11, 'results'),
               (12, 'status'), (13, 'seasons'),
     ]

    choice = forms.ChoiceField(label = 'choice', choices = options)
