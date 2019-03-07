import json

from tornado.web import RequestHandler

from tornado.httpclient import HTTPResponse

from pymodm.errors import \
    DoesNotExist, \
    ModelDoesNotExist, \
    MultipleObjectsReturned, \
    InvalidModel

from ms_tornado_questionary.service.questionary import QuestionaryService
from ms_tornado_questionary.controller.base import BaseHandler

from ms_tornado_questionary.model.questionary import Questionary

from bson import objectid


class QuestionaryHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        questionary_service = QuestionaryService()
        questionary = questionary_service.find_questionary(
            questionary_id=objectid.ObjectId(
                self.get_argument(name="_id")
            )
        )
        self.write(
            json.dumps(
                {
                    "_id": str(questionary['_id']),
                    "patient_id": questionary['patient_id'],
                    "question_answer_pairs": questionary['question_answer_pairs']
                }
            )
        )

    def post(self, *args, **kwargs):
        questionary_service = QuestionaryService()
        inc_body = self.request.body.decode('utf-8')
        questionary_dict = json.loads(inc_body)
        questionary_service.create_questionary(
            questionary_dict=questionary_dict
        )
