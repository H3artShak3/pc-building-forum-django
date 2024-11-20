from django import forms

from .models import Profile, User, Postai, PostaiReview, Advertisements, AdvertisementReview


class PostasReviewForm(forms.ModelForm):
    class Meta:
        model = PostaiReview
        fields = ('content', 'postas', 'reviewer', 'ft')
        widgets = {
            'postas': forms.HiddenInput(),
            'reviewer': forms.HiddenInput()
        }


class AdvertisementReviewForm(forms.ModelForm):
    class Meta:
        model = AdvertisementReview
        fields = ('content', 'advert', 'reviewer')
        widgets = {
            'advert': forms.HiddenInput(),
            'reviewer': forms.HiddenInput()
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('f_name', 'l_name', 'picture')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class DateInput(forms.DateInput):
    input_type = 'date'


class UserPostasCreateForm(forms.ModelForm):
    class Meta:
        model = Postai
        fields = ('category', 'theme', 'status',
                  'description', 'ft_1', 'ft_2', 'ft_3', 'ft_4', 'ft_5', 'creator')
        widgets = {
            'creator': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }


class UserAdvertisementCreateForm(forms.ModelForm):
    class Meta:
        model = Advertisements
        fields = ('kaina', 'telefonas', 'tema', 'aprasymas',
                  'cpu_kiekis', 'cpu_modelis', 'gpu_kiekis', 'gpu_modelis', 'ram_kiekis', 'ram_modelis',
                  'ft_1', 'ft_2', 'ft_3', 'ft_4', 'status', 'useris')
        widgets = {
            'useris': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }
