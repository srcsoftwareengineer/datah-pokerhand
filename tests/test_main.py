'''
Created on 27 de set de 2021

@author: samurai
'''
import unittest

import main


class Test(unittest.TestCase):

    def testMain(self):
        try:
            objMain = main
            self.assertIsNotNone(objMain)
            return
        except BaseException as excpt:
            raise excpt
        finally:
            NotImplemented


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testMain']
    unittest.main()
