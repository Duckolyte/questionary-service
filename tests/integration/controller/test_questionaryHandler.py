from json import loads

from tornado.testing import AsyncHTTPTestCase
from pymodm.errors import DoesNotExist

from ms_tornado_questionary.ms_questionary import setup_server


class TestQuestionaryHandler(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_get_response_code(self):
        response = self.fetch('/questionary?_id=5c7daf0cdfa3ff0fb496215f')
        self.assertEqual(response.code, 200)

    def test_get_response_content(self):
        response_body = self.fetch('/questionary?_id=5c7daf0cdfa3ff0fb496215f').body
        json_response = loads(response_body)
        self.assertEqual(json_response['patient_id'], 'test_000321')

    def test_get_bad_code_url_argument(self):
        response = self.fetch('/questionary?_id=-1')
        self.assertEqual(response.code, 500)

    def test_post(self):
        response = self.fetch(
            '/questionary',
            method="POST",
            body='{"patientId": "test_0000", "questionAnswerPairs": "{}"}'
        )
        self.assertEqual(response.code, 200)
