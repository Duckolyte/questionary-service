import json

from tornado.web import RequestHandler

from tornado.httpclient import HTTPResponse

from pymodm.errors import \
    DoesNotExist, \
    ModelDoesNotExist, \
    MultipleObjectsReturned, \
    InvalidModel

from ms_tornado_questionary.service.questionary import QuestionaryService

from ms_tornado_questionary.model.questionary import Questionary

from bson import objectid


class QuestionaryHandler(RequestHandler):

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

        questions = self.get_body_argument(
            name="questions",
        )

        answers = self.get_body_argument(
            name="answers",
        )

        try:
            questionary_service.create_questionary(
                questionary_dict={
                    "questions": questions,
                    "answers": answers
                }
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
                code=200,
                reason="OK"
            )
        )
