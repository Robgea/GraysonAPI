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
        if params == None:
            params = {'format' : 'json'}

        branch = kwargs['branch']
        endpoint = kwargs['endpoint']

        output = requests.post(f'{self.url}{branch}/{self.org_id}/{endpoint}', headers = self.header, data = params)
        parsed_output = self.return_parser(output)
        return parsed_output

    def return_parser(self, response):
        read_output = json.loads(response.text)
        if str(read_output['meta']['status_code']).startswith('20'):
            return read_output['data']

        else:
            # A real error handler will come here eventually. Right now I'm doing this.
            print('Hey hey, we have an error!  ')
            return f'Error code received. \n Code: {read_output["meta"]["status_code"]} \n Message:  {read_output["meta"]["message"]} '



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