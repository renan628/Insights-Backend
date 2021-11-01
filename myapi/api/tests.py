from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
import time
from .models import Tag, Card

class CardsEndPointTestCase(APITestCase):
    def setUp(self):
        self.endpoint = '/api/v1/cards/'

    def test_cards_list(self):
        '''
        Testing cards list. Testing tag filters and pagination filter.
        Recording the order is modification timestamp desc
        '''
        tag1 = Tag.objects.create(nome='TesteTagCardGet1')
        tag2 = Tag.objects.create(nome='TesteTagCardGet2')
        tag3 = Tag.objects.create(nome='TesteTagCardGet3')
        card1 = Card.objects.create(texto='TesteCardGet1')
        card1.tags.add(tag1)
        card1.tags.add(tag2)
        card2 = Card.objects.create(texto='TesteCardGet2')
        card2.tags.add(tag2)
        card2.tags.add(tag3)
        time.sleep(0.5)
        card3 = Card.objects.create(texto='TesteCardGet3')

        url = self.endpoint
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        rJson = json.loads(response.content)['results']
        self.assertEqual(3, len(rJson))

        url = self.endpoint + '?tags=TesteTagCardGet1,TesteTagCardGet2'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        rJson = json.loads(response.content)['results']
        self.assertEqual(2, len(rJson))

        url = self.endpoint + '?tags=TesteTagCardGet1'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        rJson = json.loads(response.content)['results']
        self.assertEqual(1, len(rJson))
        self.assertEqual('TesteCardGet1', rJson[0]['texto'])

        url = self.endpoint + '?tags=TesteTagCardGet3'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        rJson = json.loads(response.content)['results']
        self.assertEqual(1, len(rJson))
        self.assertEqual('TesteCardGet2', rJson[0]['texto'])

        url = self.endpoint + '?limit=1&skip=1'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        rJson = json.loads(response.content)['results']
        self.assertEqual(1, len(rJson))
        self.assertEqual('TesteCardGet2', rJson[0]['texto'])

        url = self.endpoint + '?limit=1&skip=2'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        rJson = json.loads(response.content)['results']
        self.assertEqual(1, len(rJson))
        self.assertEqual('TesteCardGet1', rJson[0]['texto'])



    def test_cards_retrive(self):
        card = Card.objects.create(texto='TesteCardGet')
        url = self.endpoint + str(card.id) + '/'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_cards_create(self):
        '''
        Creating card, one tag already exists, the others must be created.
        The existent tag must not be duplicated 
        '''
        Tag.objects.create(nome='TagCardCreate1')
        tag1 = {
            "nome": "TagCardCreate1"
        }
        tag2 = {
            "nome": "TagCardCreate2"
        }
        tag3 = {
            "nome": "TagCardCreate3"
        }
        payload = {
            "texto": "TesteCardCreate",
            "tags": [tag1, tag2, tag3]
        }
        response = self.client.post(self.endpoint, payload, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        rJson = json.loads(response.content)
        self.assertEqual(3, len(rJson['tags']))

        countTag = Tag.objects.filter(nome='TagCardCreate1').count()
        self.assertEqual(1, countTag)

        countTag1 = Tag.objects.filter(nome='TagCardCreate2').count()
        self.assertEqual(1, countTag)

        countTag1 = Tag.objects.filter(nome='TagCardCreate3').count()
        self.assertEqual(1, countTag)


    def test_cards_update(self):
        '''
        Updating card, one tag must be dissociated, the not existent must be created.
        The dissociated tag must continue to exist
        '''
        card = Card.objects.create(texto='TestCardUpdate')
        tag1 = Tag.objects.create(nome='TagCardUpdate1')
        tag2 = Tag.objects.create(nome='TagCardUpdate2')
        card.tags.add(tag1)
        card.tags.add(tag2)

        tag2 = {
            "nome": "TagCardUpdate2"
        }
        tag3 = {
            "nome": "TagCardUpdate3"
        }
        payload = {
            "texto": "TestCardUpdate",
            "tags": [tag2, tag3]
        }

        url = self.endpoint + str(card.id) + '/'
        response = self.client.put(url, payload, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        rJson = json.loads(response.content)
        self.assertEqual(2, len(rJson['tags']))
        self.assertEqual('TagCardUpdate2', rJson['tags'][0]['nome'])
        self.assertEqual('TagCardUpdate3', rJson['tags'][1]['nome'])

        countTag = Tag.objects.filter(nome='TagCardUpdate1').count()
        self.assertEqual(1, countTag)

        countTag1 = Tag.objects.filter(nome='TagCardUpdate2').count()
        self.assertEqual(1, countTag)
        
        countTag1 = Tag.objects.filter(nome='TagCardUpdate3').count()
        self.assertEqual(1, countTag)

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