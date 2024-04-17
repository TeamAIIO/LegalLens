from resource.models import Test1


def testData(input, db):
    list = db.query(Test1).all()
    print(list)
    return list