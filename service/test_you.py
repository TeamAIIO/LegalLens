from resource.models import Precedent, Test1


def testData(input, db):
    print('question', input)
    # list = db.query(Test1).all()
    list = db.query(Precedent).limit(3).all()
    print(list)
    return list