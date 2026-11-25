from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["firstname", "lastname", "email", "phone", "joined_date"]
        labels = {"firstname": "First name"}
        help_texts = {"email": "We will never share your email."}
        widgets = {
            "joined_date": forms.DateInput(attrs={"type": "date"}),
            "firstname": forms.TextInput(attrs={"class": "input", "placeholder": "Jane"}),
            "lastname": forms.TextInput(attrs={"class": "input", "placeholder": "Doe"}),
            "email": forms.EmailInput(attrs={"class": "input", "placeholder": "jane@example.com"}),
            "phone": forms.TextInput(attrs={"class": "input", "placeholder": "912345678"}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone is None:
            return phone
        digits = str(phone)
        if len(digits) != 9 or not digits.startswith("9"):
            raise forms.ValidationError(
                "Phone must have 9 digits and start with 9."
            )
        return phone
