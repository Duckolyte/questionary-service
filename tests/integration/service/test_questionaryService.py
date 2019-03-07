from tornado.testing import AsyncHTTPTestCase
from pymodm.errors import DoesNotExist
from bson import ObjectId

from ms_tornado_questionary.ms_questionary import setup_server
from ms_tornado_questionary.controller.questionary import QuestionaryService


class TestQuestionaryService(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_find_questionary(self):
        service = QuestionaryService()
        response = service.find_questionary(
            questionary_id=ObjectId('5c7daf0cdfa3ff0fb496215f')
        )
        self.assertEqual(
            response['_id'],
            ObjectId('5c7daf0cdfa3ff0fb496215f')
        )

    def test_create_questionary(self):
        service = QuestionaryService()
        with self.assertRaises(DoesNotExist):
            response = service.find_questionary(
                questionary_id='-1'
            )
