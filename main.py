class Validator:

    def username_is_valid(self, username):

        if len(username) > 10:
            return False

        if ' ' in username:
            return False

        if username.islower():
            return False

        return True











# def do_stuff(num):
#     # try:
#         return num + 5
#     # except TypeError as err:
#     #     return err
#
# #
# # def do_stuff2(num=0):
# #     try:
# #         if num:
# #             return int(num) + 5
# #         else:
# #             return 'please enter number:'
# #     except ValueError as err:
# #         return err
