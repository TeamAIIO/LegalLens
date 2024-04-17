from resource.base_models import Answer
from resource.models import Precedent


def testData(input, db):
    list = db.query(Precedent).limit(1).all()
    print(list)

    # TODO
    # similarity 체크

    first_data: Precedent = list[0]

    answer: Answer = Answer()
    answer.question = input
    answer.originAnswer = first_data.Summary
    answer.shortAnswer = 'TODO'
    answer.serialNumber = first_data.CaseSerialNumber
    answer.caseNumber = first_data.CaseNumber
    answer.date = first_data.JudgmentDate
    print(answer)

    return answer