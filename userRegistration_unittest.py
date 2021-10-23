import unittest
import module_UserRegistration as UR
import json

class test_class(unittest.TestCase):
    file = open('Data.json')
    Data = json.load(file)

    def test_Fname_Pass(self):
        for i in test_class.Data["Fname_Pass"]:
            self.assertTrue(UR.Fname_regex(i))
            
    def test_Fname_Fail(self):
        for i in test_class.Data["Fname_Fail"]:
            self.assertFalse(UR.Fname_regex(i))
            
    def test_Lname_Pass(self):
        for i in test_class.Data["Lname_Pass"]:
            self.assertTrue(UR.Lname_regex(i))
            
    def test_Lname_Fail(self):
        for i in test_class.Data["Lname_Fail"]:
            self.assertFalse(UR.Lname_regex(i))
            
    def test_Email_Pass(self):
        for i in test_class.Data["Email_Pass"]:
            self.assertTrue(UR.Email_regex(i))
            
    def test_Email_Fail(self):
        for i in test_class.Data["Email_Fail"]:
            self.assertFalse(UR.Email_regex(i))
            
    def test_Phone_Pass(self):
        for i in test_class.Data["Phone_Pass"]:
            self.assertTrue(UR.Phone_regex(i))
            
    def test_Phone_Fail(self):
        for i in test_class.Data["Phone_Fail"]:
            self.assertFalse(UR.Phone_regex(i))
            
    def test_Pass1_Pass(self):
        for i in test_class.Data["Pass1_Pass"]:
            self.assertTrue(UR.Password1_regex(i))
            
    def test_Pass1_Fail(self):
        for i in test_class.Data["Pass1_Fail"]:
            self.assertFalse(UR.Password1_regex(i))
            
    def test_Pass2_Pass(self):
        for i in test_class.Data["Pass2_Pass"]:
            self.assertTrue(UR.Password2_regex(i))
            
    def test_Pass2_Fail(self):
        for i in test_class.Data["Pass2_Fail"]:
            self.assertFalse(UR.Password2_regex(i))
            
    def test_Pass3_Pass(self):
        for i in test_class.Data["Pass3_Pass"]:
            self.assertTrue(UR.Password3_regex(i))
            
    def test_Pass3_Fail(self):
        for i in test_class.Data["Pass3_Fail"]:
            self.assertFalse(UR.Password3_regex(i))
            
    def test_Pass4_Pass(self):
        for i in test_class.Data["Pass4_Pass"]:
            self.assertTrue(UR.Password4_regex(i))
            
    def test_Pass4_Fail(self):
        for i in test_class.Data["Pass4_Fail"]:
            self.assertFalse(UR.Password4_regex(i))


if __name__ == '__main__':
    unittest.main()