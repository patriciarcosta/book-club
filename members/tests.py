from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Member


class MembersByMonthTests(TestCase):
    def test_lists_members_joined_in_requested_month(self):
        matching_member = Member.objects.create(
            firstname="Alex", lastname="Reader", joined_date=date(2024, 3, 5)
        )
        Member.objects.create(
            firstname="Sam", lastname="Reader", joined_date=date(2024, 4, 5)
        )
        Member.objects.create(
            firstname="Jo", lastname="Reader", joined_date=date(2023, 3, 5)
        )

        response = self.client.get(
            reverse("members:joined-month", kwargs={"year": 2024, "month": 3})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["members"]), [matching_member])
