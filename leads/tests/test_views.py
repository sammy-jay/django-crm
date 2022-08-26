from django.test import TestCase
from django.shortcuts import reverse


class IndexPageTest(TestCase):

    def test_get(self):
        # TODO some test
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_template_name(self):
        # TODO some test
        pass



