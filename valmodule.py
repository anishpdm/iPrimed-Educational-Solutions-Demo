import re
def validate(r):
    val = re.match("\d{2}", r)
    if (val):
        return True
    else:
        return False
