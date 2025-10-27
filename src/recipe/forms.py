from django import forms

class RecipeSearchForm(forms.Form):
    DIFFICULTY_CHOICES = [
        ('', 'Any'),
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard')
    ]

    name = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by recipe name...'
        })
    )

    ingredients = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., chicken, garlic, tomatoes'
        }),
        help_text='Enter ingredients separated by commas'
    )
    
    max_cooking_time = forms.IntegerField(
    required=False,
    min_value=1,
    widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Maximum minutes',
        'min': '1'
    }),
    help_text='Maximum cooking time in minutes'
)

    difficulty = forms.ChoiceField(
        required=False,
        choices=DIFFICULTY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    