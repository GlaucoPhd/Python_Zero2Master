from classes.validator import main

username = 'askdja'
validator = validator()
if validator.username_is_valid(username):
    print('username is ok')
else:
    print('Invalid')




# import unittest
# import main
#
#
# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 1.99)
#
#
# unittest.main()
    # def test_do_stuff2(self):
    #     test_param = 'ewrwer'
    #     result = main.do_stuff(test_param)
    #     self.assertIsInstance(isinstance(result, TypeError))
    #
    # def test_do_stuff3(self):
    #     test_param = None
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 'please enter number:')
    #
    # def test_do_stuff4(self):
    #     test_param = ' '
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 'please enter number:')