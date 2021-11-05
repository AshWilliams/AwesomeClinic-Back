import unittest
from backend import app

class BasicTestCase(unittest.TestCase):
    def test_profile_200(self):
            tester = app.test_client(self)
            response = tester.get('/profile/', content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_profile_name(self):
            tester = app.test_client(self)
            response = tester.get('/profile/', content_type='application/json')
            self.assertIn('Robert Rozas Navarro', response.data)

    def test_appointments_200(self):
            tester = app.test_client(self)
            response = tester.get('/appointments/', content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_appointments_count(self):
            tester = app.test_client(self)
            response = tester.get('/appointments/', content_type='application/json')
            jdata = response.get_json()
            self.assertEqual(len(jdata), 4)

            
if __name__ == '__main__':
    unittest.main()