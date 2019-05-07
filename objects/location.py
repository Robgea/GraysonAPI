class Location(object):

    def __init__(self, client):
        self.client = client

    # locations start here.

    '''as a principle, the base class can have the location included in it,
     however all of the methods here allow for a location to be specified. The method location info will always overwrite the base info
     so that you can find out about locations that aren't the one the user is in at the moment.'''

    def get_location_spaces(self, location_id = None):
        #might need to create a list version of this function to enable easy searching for other room reservation functions.

        self.location_id = location_id

        #This checks to make sure a Location ID is given, and also lets the base class ID take over in case a location isn't given here.
        if self.location_id == None:
            self.location_id = self.client.loc_id 
            if self.location_id == None:
                return 'Error, need to provide a location ID.'

        spaces_list = self.client.get_method(branch = 'locations', info = self.location_id, endpoint = 'spaces')

        return spaces_list



    def get_location_info(self, location_id = None):
        self.location_id = location_id
        if self.location_id == None:
            self.location_id = self.client.loc_id 
            if self.location_id == None:
                return 'Error, need to provide a location ID.'

        location_info = self.client.get_method(branch = 'locations', info = self.location_id, endpoint = '')
        return location_info

    def get_location_presence(self, location_id = None):
        self.location_id = location_id
        if self.location_id == None:
            self.location_id = self.client.loc_id 
            if self.location_id == None:
                return 'Error, need to provide a location ID.'

        presence_info = self.client.get_method(branch = 'locations', info = self.location_id, endpoint = 'presence')

    def add_location_space(self, location_id = None, **kwargs):
        #Bug found, not working. Will try to figure out what's going on.
        self.location_id = location_id
        if self.location_id == None:
            self.location_id = self.client.loc_id 
            if self.location_id == None:
                return 'Error, need to provide a location ID.'

        space_info = {'name': '', 'description': '', 'image' : '', 'is_accessible' : False, 'format': 'json'}

        if 'name' not in kwargs:
            print('No name given, invalid input!')
            return "ERROR ERROR ERROR"

        space_info['name'] = kwargs['name']

        if 'description' in kwargs:
            space_info['description'] = kwargs['description']

        if 'type' in kwargs:
            space_info.update({'type' : kwargs['type']})

        if 'image' in kwargs:
            if not kwargs['image'].startswith('http'):
                print('Image file is not a web address. Try again')
                return 'ERROR!'
            else:
                space_info['image'] = kwargs['image']

        if 'capacity' in kwargs:
            #Should include a conversion if someone puts it in as a string. 
            if type(kwargs['capacity']) == int:
                space_info.update({'capacity' : kwargs['capacity']})

        new_space = self.client.post_method(branch = 'locations', info = self.location_id, 
            endpoint = 'spaces', params = space_info)
        return new_space



