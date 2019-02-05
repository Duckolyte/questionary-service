from ms_tornado_questionary.model.questionary import Questionary, Question, Answer
#from ms_tornado_questionary.model.questionary import Question


class QuestionaryService:

    def __init__(self):
        pass

    def find_questionary(self, questionary_id):
        return Questionary.objects.get({'_id': questionary_id})

    def create_questionary(self, questionary_dict):
        Questionary(questionary_dict).save()


class AnswerService:

    def __init__(self):
        pass

    def find_answer(self, answer_id):
        return Answer.objects.get({'_id': answer_id})

