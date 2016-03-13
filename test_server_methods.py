import unittest
import requests
import redis
from random import choice

class TestSequenceFunctions(unittest.TestCase):

# Test method GET, gives a list of all candidates
    def test_GET_all_candidates(self):
        response_all, status_code = self.GET_all_candidates()
        self.assertEqual(status_code, 200)
        self.assertGreater(len(response_all['candidates']), 1)

# Test method GET, shows a candidate with id=cand_id
    def test_GET_one_candidate(self):
        cand_id = self.random_id()
        response_one, status_code = self.GET_one_candidate(cand_id)
        self.assertEqual(status_code, 200)
        self.assertEqual(len(response_one['candidate']), 3)
        self.assertEqual(response_one['candidate']['id'], cand_id)

# Test method POST, adds a new candidate
    def test_POST_adds_candidate(self):
        headers = {'Content-Type': 'application/json'}
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        list_name = r.lrange('name', 0, -1)
        name = choice(list_name)
        decoded_name = name.decode('utf8')
        list_position = r.lrange('position', 0, -1)
        position = choice(list_position)
        decoded_position = position.decode('utf8')       
        payload = {'name':decoded_name, 'position':decoded_position}

        response_adds, status_code = self.POST_adds_candidate(payload, headers)
        response_all, status_code_all = self.GET_all_candidates()
        adds_candidate = next((item for item in response_all['candidates'] if item['id'] == response_adds['candidate']['id']))

        self.assertEqual(decoded_name, adds_candidate['name'])
        self.assertEqual(decoded_position, adds_candidate['position'])
        self.assertEqual(status_code, 201)
        self.assertEqual(len(response_adds['candidate']), 3)       

# Test method POST, adds a new candidate, with incorrect_header
    def test_POST_adds_candidate_incorrect_header(self):
        headers = {'Content-Type': ''}
        r = redis.StrictRedis()
        list_name = r.lrange('name', 0, -1)
        name = choice(list_name)
        decoded_name = name.decode('utf8')
        list_position = r.lrange('position', 0, -1)
        position = choice(list_position)
        decoded_position = position.decode('utf8')       
        payload = {'name':decoded_name, 'position':decoded_position}

        response_adds, status_code = self.POST_adds_candidate(payload, headers)
        self.assertEqual(status_code, 400)

# Test method POST, deletes a candidate with id=<cand_id>        
    def test_DELETE_candidate(self):
        cand_id = self.random_id()
        response_del, status_code = self.DELETE_candidate(cand_id)
        self.assertEqual(status_code, 200)
        self.assertNotIn(cand_id, self.all_id())

# Choice random ID from list of all candidates
    def random_id(self):  
        response_all, status_code = self.GET_all_candidates()
        iden = choice([x['id'] for x in response_all['candidates']])        
        return iden

# ID list of all candidates
    def all_id(self):  
        response_all, status_code = self.GET_all_candidates()
        all_iden = [x['id'] for x in response_all['candidates']]        
        return all_iden

# Request GET, gives a list of all candidates
    def GET_all_candidates(self):
        request_all = requests.get('http://qainterview.cogniance.com/candidates')
        return (request_all.json(), request_all.status_code)

# Request GET, shows a candidate with id=cand_id
    def GET_one_candidate(self, cand_id):
        request_one = requests.get('http://qainterview.cogniance.com/candidates/%s' % cand_id)
        return (request_one.json(), request_one.status_code)

# Request POST, adds a new candidate
    def POST_adds_candidate(self, payload, headers):
        request_adds = requests.post('http://qainterview.cogniance.com/candidates',json = payload, headers = headers)
        return (request_adds.json(), request_adds.status_code)

# Request DELETE, deletes a candidate with id=<cand_id>  
    def DELETE_candidate(self, cand_id):
        request_del = requests.delete('http://qainterview.cogniance.com/candidates/%s'%cand_id)
        return (request_del.json(), request_del.status_code)
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
