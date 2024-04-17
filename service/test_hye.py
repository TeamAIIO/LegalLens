from resource.base_models import Answer


def testData(input, db):
    return

def tempData():
    answer_temp: Answer = Answer()
    answer_temp.question = '이것은 고객의 질문입니다ㄹㄹㄹㄹㄹㄹ'
    answer_temp.serialNumber = 123123 # 내부 확인용입니다, 고객 노출 x
    answer_temp.originAnswer = 'DB에서 뽑은 Target 답변입니다'
    answer_temp.shortAnswer = 'GPT가 요약해줄 것입니다'
    answer_temp.caseNumber = '85다카794'
    answer_temp.date = 20240417 #2024-04-17

    print('method', answer_temp)

    return answer_temp