from django.test import TestCase

# Create your tests here.
from .models import Lead

class LeadModelTest(TestCase):
    def test_check_age_of_lead_not_negative(self):
        lead = Lead(age=-10)
        self.assertGreater(lead.age, 0)
