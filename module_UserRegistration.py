import re
import PatternError as Error

def Fname_regex(string):
    patt = r'^[A-Z][a-z]{2,30}'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False

def Lname_regex(string):
    patt = r'^[A-Z][a-z]{3,30}'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False

def Email_regex(string):
    patt = r'([A-Za-z0-9_+\-!#$%^&*]{3,})+(\.[A-Za-z0-9]{3,})*(\@[a-zA-Z1-9]{1,}\.)+([a-zA-Z]{2,})+(\.[a-zA-Z]{2,})*'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False

def Phone_regex(string):
    patt = r'([0-9]{2})+(\s[0-9]{10})+'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False

def Password1_regex(string):
    patt = r'(.{8,})+'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False

def Password2_regex(string):
    patt = r'(?=.*[A-Z]).{8,}'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False

def Password3_regex(string):
    patt = r'(?=.*[A-Z])(?=.*[0-9]).{8,}'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False

def Password4_regex(string):
    patt = r'(?=.*[A-Z])(?=.*[0-9])(?=.*[@!#$%^&*_-]).{8,}'
    matches = re.fullmatch(patt,string)
    if matches:
        return True
    else:
        return False
