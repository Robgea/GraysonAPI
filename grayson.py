import requests
import json
from objects.organization import Organization
from objects.location import Location
from objects.spaces import Spaces


# core API will have API key and org ID
#everything else is a method to call on it

class GraysonAPI:
    def __init__(self, org_id, API_key, loc_id = None):
        self.API_key = API_key
        self.org_id = org_id
        self.loc_id = loc_id
        self.header = {'Authorization' : f'Access-Token {API_key}'}
        self.url = 'https://api.robinpowered.com/v1.0'
        self.organization = Organization(self)
        self.location = Location(self)
        self.spaces = Spaces(self)

    # Organizations work

    def get_method(self, params = None, **kwargs):
        if params == None:
            params = {'format' : 'json'}
        branch = kwargs['branch']
        endpoint = kwargs['endpoint']
        info = kwargs['info']
        output = requests.get(f'{self.url}/{branch}/{info}/{endpoint}', headers=self.header, params = params)
        parsed_output = self.return_parser(output)

        return parsed_output

    def post_method(self, params = None, **kwargs):
        if params == None:
            params = {'format' : 'json'}

        branch = kwargs['branch']
        endpoint = kwargs['endpoint']
        info = kwargs['info']

        output = requests.post(f'{self.url}/{branch}/{info}/{endpoint}', headers = self.header, data = params)
        parsed_output = self.return_parser(output)
        return parsed_output

    def patch_method(self, params = None, **kwargs):
        if params == None:
            params = {'format' : 'json'}

        branch = kwargs['branch']
        endpoint = kwargs['endpoint']
        info = kwargs['info']

        output = requests.patch(f'{self.url}/{branch}/{info}/{endpoint}', headers = self.header, data = params)
        parsed_output = self.return_parser(output)
        return parsed_output

    def delete_method(self, **kwargs):
        branch = kwargs['branch']
        endpoint = kwargs['endpoint']
        info = kwargs['info']
        output = requests.delete(f'{self.url}/{branch}/{info}/{endpoint}', headers=self.header)
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



