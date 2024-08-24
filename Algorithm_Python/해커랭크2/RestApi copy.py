import requests
import json

# team = 'Barcelona'
# year = 2011
# goals = 0
# for team_param in ['team1', 'team2']: 
# 	url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' +str(year) + '&' + team_param + '=' + team + '&page=1'
# 	response = requests.request('GET', url, headers={}, data={})
# 	r = json.loads(response.text.encode('utf8'))
# 	r_data = r['data']
# 	for record in r_data:
#   		goals += int(record[team_param+'goals'])
# print(goals)
city = 'Seattle'
cost = 120

response = requests.get('https://jsonmock.hackerrank.com/api/food_outlets?city=%s&page=%d' % (city, 1))
total_pages = json.loads(response.text.encode('utf8'))['total_pages']
restaurant = None
highest_rating = 0
lowest_cost = cost

for page in range(1, int(total_pages)+1):
    response = requests.get('https://jsonmock.hackerrank.com/api/food_outlets?city=%s&page=%d' % (city, page))
    data = json.loads(response.text.encode('utf8'))['data']
    for record in data:
        if record['estimated_cost'] <= cost:
            if highest_rating == record['user_rating']['average_rating'] and record['estimated_cost'] < lowest_cost:
                restaurant = record['name']
                lowest_cost = record['estimated_cost']
            elif highest_rating < record['user_rating']['average_rating']:
                restaurant = record['name']
                highest_rating = record['user_rating']['average_rating']
                lowest_cost = record['estimated_cost']
print(restaurant)


# for answer in answers:
#   if rating < answers[0]['user_rating']['average_rating']:
#     restaurant = answer[0]['name']
#     rating = answers[0]['user_rating']['average_rating']
#   print(answer)
  