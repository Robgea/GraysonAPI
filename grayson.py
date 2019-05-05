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

    

    # raw user info
    def get_users(self):
        users_output = requests.get(f'{self.url}organizations/{self.org_id}/users', headers = self.header)
        loaded_users = json.loads(users_output.text)
        if loaded_users['meta']['status_code'] == 200:
            return loaded_users['data']

        else:
            print('Hey hey, we have an error!  ')
            print(f'Error code received. \n Code: {loaded_users["meta"]["status_code"]} \n Message:  {loaded_users["meta"]["message"]} ')
    
    #parsed user info
    def get_user_emails(self):
        users_output = requests.get(f'{self.url}organizations/{self.org_id}/users', headers = self.header)
        loaded_users = json.loads(users_output.text)
        if loaded_users['meta']['status_code'] == 200:
            ouput_dict = { user['name'] : user['primary_email']['email'] for user in loaded_users['data']}
            return ouput_dict

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

            return loaded_user_return

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


    def add_location(self, **kwargs):
        location_info = {'name': '', 'description': '', 'image' : '', 'format': 'json'}
        if 'name' not in kwargs:
            print('No name given, invalid input!')
            return "ERROR ERROR ERROR"

        location_info['name'] = kwargs['name']

        if 'description' in kwargs:
            location_info['description'] = kwargs['description']

        if 'address' in kwargs:
            if len(kwargs['address']) < 5:
                print("Address is too short, please write full address.")
                return "Error Error"
            else:
                location_info.update({'address' : kwargs['address']})


        if 'image' in kwargs:
            if not kwargs['image'].startswith('http'):
                print('Image file is not a web address. Try again')
                return 'ERROR!'
            else:
                location_info['image'] = kwargs['image']

        if 'time_zone' in kwargs:
            location_info['time_zone'] = kwargs['time_zone']

        new_location = requests.post(f'{self.url}organizations/{self.org_id}/locations', 
            headers = self.header, data = location_info)

        loaded_new_location_return = json.loads(new_location.text)
        if loaded_new_location_return['meta']['status_code'] == 200:
            return f'Success! New room {location_info["name"]} has been added!'
        else:
            return loaded_new_location_return

    def get_amenities(self):
        amenities_output = requests.get(f'{self.url}organizations/{self.org_id}/amenities', headers = self.header)
        loaded_amenities = json.loads(amenities_output.text)
        if loaded_amenities['meta']['status_code'] == 200:
            return loaded_amenities['data']

        else:
            print('Hey hey, we have an error!  ')
            print(f'Error code received. \n Code: {loaded_locations["meta"]["status_code"]} \n Message:  {loaded_locations["meta"]["message"]} ')
