from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient

from cakes.models import Cake


class CakesModelViewSetTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.api_client = APIClient()

        self.create_test_cakes()

    def create_test_cakes(self):
        self.cake_1 = baker.make(
            "cakes.Cake", name="cake 1", comment="comment 1", image_url="http://test.url/cake1.img", yum_factor=1
        )
        self.cake_2 = baker.make(
            "cakes.Cake", name="cake 2", comment="comment 2", image_url="http://test.url/cake2.img", yum_factor=1
        )
        self.cake_3 = baker.make(
            "cakes.Cake", name="cake 3", comment="comment 3", image_url="http://test.url/cake3.img", yum_factor=4
        )
        self.cake_4 = baker.make(
            "cakes.Cake", name="cake 4", comment="comment 4", image_url="http://test.url/cake4.img", yum_factor=4
        )

    def test_get_cakes_list(self):
        response = self.api_client.get(reverse("cakes-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 4)
        self.assertEqual(response.data["results"][0]["id"], self.cake_1.id)
        self.assertEqual(response.data["results"][3]["id"], self.cake_4.id)

    def test_get_cake(self):
        kwargs = {"pk": self.cake_2.id}
        response = self.api_client.get(reverse("cakes-detail", kwargs=kwargs))

        response = self.api_client.get(reverse("cakes-detail", kwargs=kwargs))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.cake_2.id)

        kwargs = {"pk": self.cake_3.id}
        response = self.api_client.get(reverse("cakes-detail", kwargs=kwargs))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.cake_3.id)

        kwargs = {"pk": "fake_id"}
        response = self.api_client.get(reverse("cakes-detail", kwargs=kwargs))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"], "Not found.")

    def test_create_cake(self):
        response = self.api_client.post(reverse("cakes-list"), data={})
        self.assertEqual(response.status_code, 400)
        for field in ("name", "comment", "image_url", "yum_factor"):
            self.assertEqual(response.data[field][0], "This field is required.")

        data = {
            "name": "new_cake",
            "comment": "comment for new cake",
            "image_url": "http://test.url/new_cake.img",
            "yum_factor": 5,
        }

        response = self.api_client.post(reverse("cakes-list"), data=data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["comment"], data["comment"])
        self.assertEqual(response.data["image_url"], data["image_url"])
        self.assertEqual(response.data["yum_factor"], data["yum_factor"])

    def test_delete_cake(self):
        kwargs = {"pk": "fake_id"}
        response = self.api_client.delete(reverse("cakes-detail", kwargs=kwargs))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"], "Not found.")

        self.assertTrue(Cake.objects.filter(id=self.cake_1.id).exists())
        kwargs = {"pk": self.cake_1.id}
        response = self.api_client.delete(reverse("cakes-detail", kwargs=kwargs))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Cake.objects.filter(id=self.cake_1.id).exists())
