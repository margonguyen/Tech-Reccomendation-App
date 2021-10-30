import unittest
from app import app
class Test(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
    def test_login(self):
        rv = self.app.get('/api/login')
        self.assertEqual(rv.status, '200 OK')
    def test_signup(self):
        rv = self.app.get('/api/signup')
        self.assertEqual(rv.status, '200 OK')
    def test_users(self):
        rv = self.app.get('/api/users')
        self.assertEqual(rv.status, '200 OK')
    def test_a_user(self):
        rv = self.app.get('/api/abcd')
        self.assertEqual(rv.status, '200 OK')
    def test_searchFilter(self):
        rv = self.app.get('/filter')
        self.assertEqual(rv.status, '200 OK')
if __name__ == '__main__':
    unittest.main()