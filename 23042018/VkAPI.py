import requests
import json


class VkAPI:

    def __init__(self):
        pass

    @staticmethod
    def friends_get(id):
        r = requests.get('https://api.vk.com/method/friends.get?user_id='+str(id)+'&v=5')
        req = json.loads(r.text)
        return req['response']['items']

    @staticmethod
    def user_info_by_id(ids):
        for id in ids:
            response = requests.get('https://api.vk.com/method/users.get?user_id='+str(id)+'&v=5')
            pars = json.loads(response.text)
            print(str(pars['response'][0]['id']) + ' ' + str(pars['response'][0]['first_name']) + ' ' +
                  str(pars['response'][0]['last_name']))

    @staticmethod
    def my_frieds_get_mutual(id1, id2):
        first = VkAPI.friends_get(id1)
        second = VkAPI.friends_get(id2)
        print(list(set(first) & set(second)))
        return list(set(first) & set(second))
