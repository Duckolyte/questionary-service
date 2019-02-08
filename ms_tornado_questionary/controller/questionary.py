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
            questionary_id=self.get_argument(name="_id")
        ).to_son().to_dict()

        self.write(questionary)

    def post(self, *args, **kwargs):
        questionary_service = QuestionaryService()

        inc_body = self.request.body.decode('utf-8')

        questionary_dict = json.loads(inc_body)

        questionary_service.create_questionary(
            questionary_dict=questionary_dict
        )

        # TODO below is handled by the server default

        '''
        try:
            questionary_service.create_questionary(
                questionary_dict=questionary_dict
            )
        except (ModelDoesNotExist, InvalidModel, MultipleObjectsReturned):
            self.write(
                HTTPResponse(
                    code=500,
                    reason="Internal Server Error. Failed to store questionary."
                )
            )
            return

        self.write(
            HTTPResponse(
                request=self.request,
                code=200,
                reason="OK"
            )
        )
        '''