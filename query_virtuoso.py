import json
import requests
import urllib
from requests.auth import HTTPDigestAuth

username = ''
password = ''
server = 'http://pvsge014.labs.vu.nl:8890/sparql' # Replace this with your SPARQL instance

def get_results(query):
	auth = HTTPDigestAuth(username, password)
	q = {'query': query, 'format': 'json'}
	url = server + '?' + urllib.urlencode(q)
	#print url
	r = requests.get(url=url, auth=auth)  
	page = r.content
	return json.loads(page)["results"]["bindings"]

query='SELECT * WHERE { ?a ?b ?c } LIMIT 10' # Here is your query
for result in get_results(query):
	print result["b"]["value"], result["c"]["value"] # Note that ?b and ?c are coming from the query. 
	#If the variable names change in the query, they should change in this line too.
