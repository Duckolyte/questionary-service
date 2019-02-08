from ms_tornado_questionary.model.questionary import Questionary, Question, Answer


class QuestionaryService:

    def __init__(self):
        pass

    def find_questionary(self, questionary_id):
        return Questionary.objects.get({'_id': questionary_id})

    def create_questionary(self, questionary_dict):
        Questionary(
            patient_id=questionary_dict["patientId"],
            question_answer_pairs=questionary_dict["questionAnswerPairs"]
        ).save()


class AnswerService:

    def __init__(self):
        pass

    def find_answer(self, answer_id):
        return Answer.objects.get({'_id': answer_id})

