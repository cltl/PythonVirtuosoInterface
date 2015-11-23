import json
import requests
import urllib
from requests.auth import HTTPDigestAuth

username = ''
password = ''
server = 'http://pvsge014.labs.vu.nl:8890/sparql'

def get_results(query):
	auth = HTTPDigestAuth(username, password)
	q = {'query': query, 'format': 'json'}
	url = server + '?' + urllib.urlencode(q)
	#print url
	r = requests.get(url=url, auth=auth)  
	page = r.content
	return json.loads(page)["results"]["bindings"]

query='SELECT * WHERE { ?a ?b ?c } LIMIT 10'
for result in get_results(query):
	print result["b"]["value"], result["c"]["value"]
