# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.
from datetime import date

from django.shortcuts import get_object_or_404
from django import forms

from .models import Announcement
from categories.models import Category


class EditPostForm(forms.ModelForm):
    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])

    class Meta:
        model = Announcement
        fields = ['title', 'description', 'address', 'country',
                  'city', 'data', 'timePost', 'money', 'category',
                  'image', 'image2', 'image3', 'image4']
        widgets = {'description': forms.Textarea(attrs={'required': 'required',
                                                        })
                   }

        def clean_category(self):
            category = get_object_or_404(Category,
                                         name=self.cleaned_data['category'])
            return category


class CreatePostForm(forms.ModelForm):
    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])

    class Meta:
        model = Announcement
        fields = ['title', 'description', 'address', 'country',
                  'city', 'data', 'timePost', 'money', 'category',
                  'image', 'image2', 'image3', 'image4']
        widgets = {'description': forms.Textarea(attrs={'required': 'required',
                                                        })
                   }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 10:
            raise forms.ValidationError(
                u'Ensure your title has at '
                'least 5 characters')

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 100:
            raise forms.ValidationError(
                u'Ensure your title has at '
                'least 20 characters')

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < date.today():
            raise forms.ValidationError("Date is not valid")

    def clean_money(self):
        money = self.cleaned_data['money']
        if money < 1 or money > 9223372036854775807:
            raise forms.ValidationError('Enter a valid price')
        return money

    def clean_category(self):
        category = get_object_or_404(Category,
                                     name=self.cleaned_data['category'])
        return category
