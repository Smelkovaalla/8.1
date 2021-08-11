from pprint import pprint
import requests

name = ['Hulk', 'Captain America', 'Thanos']
# print(len(name))

API_BASE_URL = "https://superheroapi.com/api/2619421814940190/"
x = 0
id_list = []
int_dict = {}

while x < len(name):
  print(name[x])
  response = requests.get(API_BASE_URL + "search/" + name[x])

  # pprint(response.json())
  
  id_list.append(response.json()['results'][0]['id'])
  int_dict[name[x]] = (response.json()['results'][0]['powerstats']['intelligence'])
  pprint(response.json()['results'][0]['id'])
  pprint(response.json()['results'][0]['powerstats']['intelligence'])
  x +=1


print(id_list)
print(int_dict)
int_list = list(int_dict.items())
int_list.sort(key=lambda i: i[1])
print(int_list)
print(f'Самый умный супер герой {int_list[0][0]} у него уровень интеллекта {int_list[0][1]}')
