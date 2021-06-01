import requests
import simplejson
URL = "http://127.0.0.1:8000/stu_create/"
data = {
    'name': 'Shivam Gupta',
    'roll' : 101677,
    'city' : 'Aligarh'
}
data1 = {
    'student' : 'Shivam Gupta',
    'score' : 56 
}
json_data = simplejson.dumps(data, data1)
r = requests.post(url=URL, data=json_data)
