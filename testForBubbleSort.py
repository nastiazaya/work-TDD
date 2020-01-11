import bubbleSort
import unittest

class Test(unittest.TestCase):

    def testBubbleReturnValue(self):
        A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        exept = [0, 1, 2, 3, 4, 5,5, 6, 7, 8, 9]
        if(bubbleSort.bubblesort(A) == None):
            self.fail("bubblesort fails")
        else:
            print("true")

    def testBubbleSort(self):
        A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        exept = [0,1,2,3,4,5,5,6,7,8,9]
        bubbleSort.bubblesort(A)
        if self.assertEqual(A,exept):
                self.fail("bubblesort fails")
        else:
            print("true")

    def testBubbleSortLen(self):
        A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        exept = [0, 1, 2, 3, 4, 5 ,5, 6, 7, 8, 9]
        bubbleSort.bubblesort(A)
        if(len(A) != len(exept)):
            self.fail("bubblesort fails")
        else:
            print("true")


if __name__ == '__main__':
    unittest.main()