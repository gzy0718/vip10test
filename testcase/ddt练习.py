import unittest
from ddt import *
test_data = [[1,2],[3,4]]
@ddt
class Mytest(unittest.TestCase):
    @data((1,2))
    @unpack
    def testr_bbt1(self,value1,value2):
        print(value1,value2)
        self.assertEqual(value1,value2)

    @data([1,2],[3,4])
    @unpack
    def testr_bbt2(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value1, value2)

    @data(*test_data)
    @unpack
    def testr_bbt3(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value1, value2)

if __name__=='__main__':

    unittest.main(verbosity=2)##表示不同的详细程度


