import requests
import logging
import os
import unittest

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'logs_for_api.log')


def configure_logging(name, file=log_file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


main_logger = configure_logging('main')


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = main_logger

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)

            elif request_type == 'POST':
                response = requests.post(url, data=data)
                stop_flag = True
            elif request_type == 'DELETE':
                response = requests.delete(url)
                stop_flag = True
            elif request_type == 'PUT':
                response = requests.put(url, data=data)
                stop_flag = True

            if not expected_error and response.status_code == 200:
                stop_flag = True
                break

        # log part
        self.logger.debug(f'{request_type} example')
        self.logger.debug(response.url)
        self.logger.debug(response.status_code)
        self.logger.debug(response.reason)
        self.logger.debug(response.text)
        self.logger.debug(response.json())
        self.logger.debug('-----------')

        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.status_code

    def post(self, endpoint, body):
        url = f'{self.base_url}/{endpoint}/'
        response = self._request(url, 'POST', data=body)
        return response.status_code

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.status_code

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.status_code


class JsonRequest(BaseRequest):
    def __init__(self):
        super().__init__('http://localhost:3000')

    def get_companies(self, entity_id):
        return self.get('companies', entity_id)

    def put_companies(self, entity_id, data):
        return self.put('companies', entity_id, data)

    def delete_companies(self, entity_id):
        return self.delete('companies', entity_id)

    def get_employees(self, entity_id):
        return self.get('employees', entity_id)

    def put_employees(self, entity_id, data):
        return self.put('employees', entity_id, data)

    def delete_employees(self, entity_id):
        return self.delete('employees', entity_id)

    def get_products(self, entity_id):
        return self.get('products', entity_id)

    def put_products(self, entity_id, data):
        return self.put('products', entity_id, data)

    def delete_products(self, entity_id):
        return self.delete('products', entity_id)

    def get_projects(self, entity_id):
        return self.get('projects', entity_id)

    def put_projects(self, entity_id, data):
        return self.put('projects', entity_id, data)

    def delete_projects(self, entity_id):
        return self.delete('projects', entity_id)

    def get_clients(self, entity_id):
        return self.get('clients', entity_id)

    def put_clients(self, entity_id, data):
        return self.put('clients', entity_id, data)

    def delete_clients(self, entity_id):
        return self.delete('clients', entity_id)


class TestJsonRequests(unittest.TestCase):
    def setUp(self):
        self.json_request = JsonRequest()

    def test_get_companies(self):
        id = 1
        company_data = self.json_request.get_companies(id)
        self.assertEqual(company_data, 200)

    def test_put_companies(self):
        new_company_data = {
            'id': 2,
            'CEO': 'New name',
            'company': 'New Company',
            'address': "New Address"
        }
        result = self.json_request.put_companies(new_company_data['id'], new_company_data)
        self.assertEqual(result, 200)

    def test_delete_companies(self):
        id = 4
        company_data = self.json_request.delete_companies(id)
        self.assertEqual(company_data, 200)

    def test_get_employees(self):
        id = 1
        employees_data = self.json_request.get_employees(id)
        self.assertEqual(employees_data, 200)

    def test_put_employees(self):
        updated_employee_data = {
            'id': 1,
            'name': 'John Doe Jr.',
            'phone_number': '0123456789'
        }
        result = self.json_request.put_employees(updated_employee_data['id'], updated_employee_data)
        self.assertEqual(result, 200)

    def test_delete_employees(self):
        id = 4
        result = self.json_request.delete_employees(id)
        self.assertEqual(result, 200)

    def test_get_products(self):
        id = 1
        products_data = self.json_request.get_products(id)
        self.assertEqual(products_data, 200)

    def test_put_products(self):
        updated_products_data = {
            'id': 1,
            'name': 'product',
            'price': 228,
            'category': 'category'
        }
        result = self.json_request.put_products(updated_products_data['id'], updated_products_data)
        self.assertEqual(result, 200)

    def test_delete_products(self):
        id = 4
        result = self.json_request.delete_products(id)
        self.assertEqual(result, 200)

    def test_get_projects(self):
        id = 1
        projects_data = self.json_request.get_projects(id)
        self.assertEqual(projects_data, 200)

    def test_put_projects(self):
        updated_projects_data = {
            'id': 1,
            'name': 'John Doe Jr.',
            'description': 'Example information personal it. Rule also low visit purp'
        }
        result = self.json_request.put_projects(updated_projects_data['id'], updated_projects_data)
        self.assertEqual(result, 200)

    def test_delete_projects(self):
        id = 4
        result = self.json_request.delete_projects(id)
        self.assertEqual(result, 200)

    def test_get_clients(self):
        id = 1
        clients_data = self.json_request.get_clients(id)
        self.assertEqual(clients_data, 200)

    def test_put_clients(self):
        updated_clients_data = {
            "id": 3,
            "name": "Harris-Mcdaniel",
            "contact_person": "Ashley Kelley",
            "email": "edwardlyons@example.com"
        }
        result = self.json_request.put_clients(updated_clients_data['id'], updated_clients_data)
        self.assertEqual(result, 200)

    def test_delete_clients(self):
        id = 4
        result = self.json_request.delete_clients(id)
        self.assertEqual(result, 200)