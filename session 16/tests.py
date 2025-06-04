import unittest as ut
from code import ThingThatDoesThings as Thing

class TestThing(ut.TestCase):

    def test_identity(self):
        #Assemble
        thing=Thing("thing 1",1)
        thing.append_datum(1)
        #Act
        result=thing.execute()
        #Assert
        self.assertEqual(1,len(result))
        self.assertEqual(1,result[0])

    def test_multiply(self):
        #Assemble
        thing=Thing("thing 1",10)
        thing.append_datum(1)
        #Act
        result=thing.execute()
        #Assert
        self.assertEqual(1,len(result))
        self.assertEqual(10,result[0])

    def test_many_identity(self):
        #Assemble
        thing=Thing("thing 1",1)
        thing.append_datum(1)
        thing.append_datum(2)
        #Act
        result=thing.execute()
        #Assert
        self.assertEqual(2,len(result))
        self.assertEqual(1,result[0])
        self.assertEqual(2,result[1])

    def test_many_multiply(self):
        #Assemble
        thing=Thing("thing 1",5)
        thing.append_datum(1)
        thing.append_datum(2)
        #Act
        result=thing.execute()
        #Assert
        self.assertEqual(2,len(result))
        self.assertEqual(5,result[0])
        self.assertEqual(10,result[1])

if __name__ == '__main__':
    ut.main()