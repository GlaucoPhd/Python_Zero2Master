# Use to validate data
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Glauco@gmail.com'

pattern2 = re.compile(r"[A-Za-z0-9%$#]{8,}\d")
password = "Ahdhk88989"

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)

