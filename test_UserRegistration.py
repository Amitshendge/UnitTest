import pytest
import module_UserRegistration as UR
import json

file = open('Data.json')
Data = json.load(file)

def test_Fname_Pass():
    for i in Data["Fname_Pass"]:
        assert UR.Fname_regex(i) == True
            
def test_Fname_Fail():
    for i in Data["Fname_Fail"]:
        assert UR.Fname_regex(i) == False
            
def test_Lname_Pass():
    for i in Data["Lname_Pass"]:
        assert UR.Lname_regex(i) == True
            
def test_Lname_Fail():
    for i in Data["Lname_Fail"]:
        assert UR.Lname_regex(i) == False
            
def test_Email_Pass():
    for i in Data["Email_Pass"]:
        assert UR.Email_regex(i) == True
            
def test_Email_Fail():
    for i in Data["Email_Fail"]:
        assert UR.Email_regex(i) == False
        
def test_Phone_Pass():
    for i in Data["Phone_Pass"]:
        assert UR.Phone_regex(i) == True
        
def test_Phone_Fail():
    for i in Data["Phone_Fail"]:
        assert UR.Phone_regex(i) == False
        
def test_Pass1_Pass():
    for i in Data["Pass1_Pass"]:
        assert UR.Password1_regex(i) == True
        
def test_Pass1_Fail():
    for i in Data["Pass1_Fail"]:
        assert UR.Password1_regex(i) == False
        
def test_Pass2_Pass():
    for i in Data["Pass2_Pass"]:
        assert UR.Password2_regex(i) == True
        
def test_Pass2_Fail():
    for i in Data["Pass2_Fail"]:
        assert UR.Password2_regex(i) == False
        
def test_Pass3_Pass():
    for i in Data["Pass3_Pass"]:
        assert UR.Password3_regex(i) == True
        
def test_Pass3_Fail():
    for i in Data["Pass3_Fail"]:
        assert UR.Password3_regex(i) == False
        
def test_Pass4_Pass():
    for i in Data["Pass4_Pass"]:
        assert UR.Password4_regex(i) == True
        
def test_Pass4_Fail():
    for i in Data["Pass4_Fail"]:
        assert UR.Password4_regex(i) == False


if __name__ == '__main__':
    pytest.main()