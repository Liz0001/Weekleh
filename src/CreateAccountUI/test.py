import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
# dirname/dirname/
# same as
# folder/folder
sys.path.append(d)
print(sys.path)

# import login_credentials

# x = login_credentials.check_name("liis")

# x = login_credentials.check_name("Liis1")
# print(x)
