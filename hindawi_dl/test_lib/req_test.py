from unittest import TestCase
from requests import get as GET



class TestRequests(TestCase):



    def test_connection(self):
        try:
            r = GET("https://www.hindawi.org/")
            self.assertTrue(r.status_code==200, "main page regect simple request (without headers)")
        except Exception as ex:
            self.fail(f'{ex}')


