from pymongo.write_concern import WriteConcern

from pymodm import MongoModel, fields


class Questionary(MongoModel):
    '''
    _id is auto generated
    questions = fields.ListField()
    answers = fields.ListField()
    '''
    patient_id = fields.CharField()
    question_answer_pairs = fields.ListField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'


class Question(MongoModel):
    '''
    _id is auto generated
    '''
    code = fields.CharField()
    label = fields.CharField()
    answers = fields.ListField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'


class Answer(MongoModel):
    '''
    _id is auto generated
    '''
    code = fields.CharField()
    label = fields.CharField()
    next = fields.CharField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'