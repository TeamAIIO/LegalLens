from resource.models import Test1


def testData(input, db):
    print('question', input)
    list = db.query(Test1).all()
    print(list)
    return list