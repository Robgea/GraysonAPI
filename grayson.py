import requests
import json


# core API will have API key and org ID
#everything else is a method to call on it

class GraysonAPI:
    def __init__(self, org_id, API_key):
        self.API_key = API_key
        self.org_id = org_id
        self.header = {'Authorization' : f'Access-Token {API_key}'}
        self.url = 'https://api.robinpowered.com/v1.0/'
        

    # Organizations work
    def get_users(self):
        users_output = requests.get(f'{self.url}organizations/{self.org_id}/users', headers = self.header)
        loaded_users = json.loads(users_output.text)
        if loaded_users['meta']['status_code'] == 200:
            return loaded_users['data']

        else:
            print('Hey hey, we have an error!  ')
            print(f'Error code received. \n Code: {loaded_users["meta"]["status_code"]} \n Message:  {loaded_users["meta"]["message"]} ')



    def add_user(self, **kwargs):
        invite_name = kwargs['name']
        invite_email = kwargs['email']
        # add error catch here
        params = {'name': invite_name, 'email': invite_email, 'format': 'json'}
        new_user = requests.post(f'{self.url}organizations/{self.org_id}/users', headers = self.header, data = params)
        loaded_user_return = json.loads(new_user.text)
        if loaded_user_return['meta']['status_code'] == 200:
            return f"Success, {invite_name} at {invite_email} has been invited into the organization."
        else: 

            return new_user.text

        # gotta do error handling
        # If it 409s it still sends an invite. Is that deliberate?


    def get_locations(self):
        locations_output = requests.get(f'{self.url}organizations/{self.org_id}/locations', headers = self.header)
        loaded_locations = json.loads(locations_output.text)
        if loaded_locations['meta']['status_code'] == 200:
            return loaded_locations['data']

        else:
            print('Hey hey, we have an error!  ')
            print(f'Error code received. \n Code: {loaded_locations["meta"]["status_code"]} \n Message:  {loaded_locations["meta"]["message"]} ')


    def get_amenities(self):
        amenities_output = requests.get(f'{self.url}organizations/{self.org_id}/amenities', headers = self.header)
        loaded = json.loads(amenities_output.text)
        return loaded