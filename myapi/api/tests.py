from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
from .models import Tag, Card

# Create your tests here.

class CardsEndPointTestCase(APITestCase):
    def setUp(self):
        self.endpoint = '/api/v1/cards/'

    def test_cards_list(self):
        Card.objects.create(texto='TesteCardGet1')
        Card.objects.create(texto='TesteCardGet2')
        url = self.endpoint
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        rJson = json.loads(response.content)
        self.assertEqual(2, len(rJson['results']))

    def test_cards_retrive(self):
        card = Card.objects.create(texto='TesteCardGet')
        url = self.endpoint + str(card.id) + '/'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_cards_create(self):
        tag1 = {
            "nome": "TagCardCreate1"
        }
        tag2 = {
            "nome": "TagCardCreate2"
        }
        payload = {
            "texto": "TesteCardCreate",
            "tags": [tag1, tag2]
        }
        response = self.client.post(self.endpoint, payload, format='json')
        print((response.content))
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def cards_update(self):
        pass

    def test_cards_delete(self):
        card = Card.objects.create(texto='TesteCardDelete')
        url = self.endpoint + str(card.id) + '/'
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)  


class TagsEndPointTestCase(APITestCase):
    def setUp(self):
        self.endpoint = '/api/v1/tags/'

    def test_tags_retrive(self):
        tag = Tag.objects.create(nome='TesteTagGet')
        url = self.endpoint + str(tag.id) + '/'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)  

    def test_tags_create(self):
        payload = {
            "nome": "TesteTagCreate"
        }
        response = self.client.post(self.endpoint, payload)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_tags_update(self):
        tag = Tag.objects.create(nome='TesteTagUpdate')
        payload = {
            "nome": "TesteTagUpdateChanged"
        }
        url = self.endpoint + str(tag.id) + '/'
        response = self.client.put(url, payload)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_tags_delete(self):
        tag = Tag.objects.create(nome='TesteTagDelete')
        url = self.endpoint + str(tag.id) + '/'
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)  