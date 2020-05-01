import json
import requests

with open('donuts.json', 'r') as file:
    data = json.load(file)
condensed_dict = {}
for donut in data:

    # print('For {} donuts, can have toppings:'.format(donut['name']))
    toppings = [topping_data['type'] for topping_data in
                donut['topping']]
    # for topping in toppings:
    #     print('\t{}'.format(topping))

    condensed_dict[donut['name']] = toppings

with open('donuts_condensed.json', 'w') as file:
    json.dump(condensed_dict, file)

# Using requests
result = requests.get('https://tools.learningcontainer.com/sample-json.json')
user_data = result.json()
pass