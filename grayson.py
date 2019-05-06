import requests
import json
from organization import Organization


# core API will have API key and org ID
#everything else is a method to call on it

class GraysonAPI:
    def __init__(self, org_id, API_key):
        self.API_key = API_key
        self.org_id = org_id
        self.header = {'Authorization' : f'Access-Token {API_key}'}
        self.url = 'https://api.robinpowered.com/v1.0/'
        self.organization = Organization(self)
        

    # Organizations work

    def get_method(self, **kwargs):
        branch = kwargs['branch']
        endpoint = kwargs['endpoint']
        output = requests.get(f'{self.url}{branch}/{self.org_id}/{endpoint}', headers=self.header)
        parsed_output = self.return_parser(output)
        return parsed_output

    def post_method(self, params = None, **kwargs):

        new_user = requests.post(f'{self.url}{branch}/{self.org_id}/{endpoint}', headers = self.header, data = params)
        pass

    def return_parser(self, response):
        read_output = json.loads(response.text)
        if read_output['meta']['status_code'] == 200:
            return read_output['data']

        else:
            # A real error handler will come here eventually. Right now I'm doing this.
            print('Hey hey, we have an error!  ')
            return f'Error code received. \n Code: {loaded_users["meta"]["status_code"]} \n Message:  {loaded_users["meta"]["message"]} '


    def add_user(self, **kwargs):
        repeat = False
        invite_name = kwargs['name']
        invite_email = kwargs['email']

        # add error catch here
        params = {'name': invite_name, 'email': invite_email, 'format': 'json'}

        if 'repeat' in kwargs:
            if kwargs['repeat'] == True:
                repeat = True

        #This section is used to make sure you're not reinviting someone accidentally. 
        if repeat == False:
            check_list = self.get_user_emails()
            print(check_list)
            if check_list == 'Error!':
                print('Error occured when checking e-mail list. ')
                # Placeholder error return.
                return False
            elif invite_email in check_list.values():

                print('Email already in organization! \n If you want to send this invite set "repeat = true" during function call.')
                return False
            else:
                pass

        print('Sending user creation...')
        new_user = requests.post(f'{self.url}organizations/{self.org_id}/users', headers = self.header, data = params)
        loaded_user_return = json.loads(new_user.text)
        if loaded_user_return['meta']['status_code'] == 200:
            return f"Success, {invite_name} at {invite_email} has been invited into the organization."
        else: 
            return loaded_user_return


        # If it 409s it still sends an invite. Is that deliberate?


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

        #need to add support for other parameters. Openings, etc.

        new_location = requests.post(f'{self.url}organizations/{self.org_id}/locations', 
            headers = self.header, data = location_info)

        loaded_new_location_return = json.loads(new_location.text)
        if loaded_new_location_return['meta']['status_code'] == 200:
            return f'Success! New room {location_info["name"]} has been added!'
        else:
            return loaded_new_location_return


    # locations start here.
    # gotta figure out a way to pass the Location info to this? 

    def get_location_spaces(self, location_id, **kwargs):

        self.location_id = location_id


        spaces_list = requests.get(f'{self.url}locations/{self.location_id}/spaces', headers = self.header)
        loaded_spaces_list = json.loads(spaces_list.text)
        return loaded_spaces_list['data']

    #reserve a space
    '''check to see if the input is an integer, if it is, great, if not then run the string through a search, 
    see if the length of the return is greater than 1, if so return the list. If not, book the room.'''