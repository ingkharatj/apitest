import unittest
import requests
import json

response = requests.get("https://flamxby.herokuapp.com/reservation")


class ApiTest(unittest.TestCase):

    url = "https://flamxby.herokuapp.com/reservation"

    data = {
        "name": "ing",
        "surname": "aaa",
        "citizen_id": "1152347583215",
        "birth_date": "2021-10-12",
        "occupation": "doctor",
        "address": "1145 bangkok",
        "password": "password"
    }

    def test_get_all_reservation(self):
        r = requests.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 9)
    
    def test_get_all_reservation_error(self):
        r = requests.get("https://flamxby.herokuapp.com/reservationdsfdsdaf")

        self.assertEqual(r.status_code, 404)
        self.assertEqual(len(r.json()), 1)


    def test_get_post(self):
        r = requests.post(self.url, json=self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_specific_date(self):

        r = requests.get(
            "https://flamxby.herokuapp.com/reservation/2021/10/23")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(response.json()), 9)

    def test_get_specific_date_month_more_than_12(self):
    
        r = requests.get(
            "https://flamxby.herokuapp.com/reservation/2021/13/23")
        self.assertEqual(r.status_code, 500)
        self.assertEqual(len(response.json()), 9)
    
    def test_get_specific_date_minus_year(self):
        
        r = requests.get(
            "https://flamxby.herokuapp.com/reservation/-2021/10/23")
        self.assertEqual(r.status_code, 500)
        self.assertEqual(len(response.json()), 9)
        
        
    def test_get_specific_date_minus_month(self):
    
        r = requests.get(
            "https://flamxby.herokuapp.com/reservation/2021/-10/23")
        self.assertEqual(r.status_code, 500)
        self.assertEqual(len(response.json()), 9)
    
    def test_get_specific_date_minus_day(self):
        
        r = requests.get(
            "https://flamxby.herokuapp.com/reservation/2021/10/-23")
        self.assertEqual(r.status_code, 500)
        self.assertEqual(len(response.json()), 9)
    
    def test_get_specific_date_february(self):
        
        r = requests.get(
            "https://flamxby.herokuapp.com/reservation/2021/02/29")
        self.assertEqual(r.status_code, 500)
        self.assertEqual(len(response.json()), 9)
    
    def test_get_specific_date_day_more_than_31(self):
        
        r = requests.get(
            "https://flamxby.herokuapp.com/reservation/2021/08/35")
        self.assertEqual(r.status_code, 500)
        self.assertEqual(len(response.json()), 9)


    def test_get_user(self):
        r = requests.get("https://flamxby.herokuapp.com/user")
        self.assertEqual(len(response.json()), 9)
        self.assertEqual(r.status_code, 405)

    def test_delete(self):
        r = requests.delete(self.url)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
