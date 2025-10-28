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

class RecipeAddForm(forms.Form):

    name = forms.CharField(
        required= True,
        max_length= 200,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter recipe name'
        })
    )   

    ingredients = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., chicken, garlic, tomatoes'
        }),
        help_text='Enter ingredients separated by commas'
    )

    cooking_time = forms.IntegerField(
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Value in minutes',
            'min': '1'
        }),
        help_text='Cooking time in minutes'
    )

    method = forms.CharField(
        required= False,
        max_length= 500,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'How to prepare this meal'
        })
    )       

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput()
    )

    def clean_ingredients(self):
        raw = self.cleaned_data['ingredients']
        # Replace common separators (; and .) with commas
        raw = raw.replace(';', ',').replace('.', ',')
        # Split and clean each word
        ingredients = [i.strip() for i in raw.split(',') if i.strip()]
        # Optionally ensure only letters/spaces allowed
        cleaned = []
        for ing in ingredients:
            cleaned.append(''.join(ch for ch in ing if ch.isalnum() or ch.isspace()))
        return cleaned