# Method
# 1 - Stars with a dot '.' dont return any value
# 2 - Only owned by an object
# 3 - What a string can do
# 4 - The method is implicitly used for an object for which it is called.
# 5 - Access the data that is contained within the class.

# Example

# class ClassName:
#    def method_name():
#       #…………..
#       # Method_body
#       #………………


class Pet(object):
  def my_method(self):
    print("I am a Cat")
cat = Pet()
cat.my_method()


basket = [1,2,3,4,5]
basket.extend([100])
new_list = basket.pop(4)
print(new_list)
new_list = basket.clear()