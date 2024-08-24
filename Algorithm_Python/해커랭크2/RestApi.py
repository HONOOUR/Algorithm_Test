import requests
import json

team = 'Barcelona'
year = 2011
goals = 0
for team_param in ['team1', 'team2']: 
	url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' +str(year) + '&' + team_param + '=' + team + '&page=1'
	response = requests.request('GET', url, headers={}, data={})
	r = json.loads(response.text.encode('utf8'))
	r_data = r['data']
	for record in r_data:
  		goals += int(record[team_param+'goals'])
print(goals)

response = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=%d&team1=%s&page=1' % (year, team))
data = response.json()["total_page"]
print(data)