class Location(object):

    def __init__(self, client):
        self.client = client

    # locations start here.

    '''as a principle, the base class can have the location included in it,
     however all of the methods here allow for a location to be specified. The method location info will always overwrite the base info
     so that you can find out about locations that aren't the one the user is in at the moment.'''

    def get_location_spaces(self, location_id = None):
        #might need to create a list version of this function to enable easy searching for other room reservation functions.
        self.location_id = self._location_check(location_id)

        spaces_list = self.client.get_method(branch = 'locations', info = self.location_id, endpoint = 'spaces')

        return spaces_list



    def get_location_info(self, location_id = None):
        self.location_id = self._location_check(location_id)

        location_info = self.client.get_method(branch = 'locations', info = self.location_id, endpoint = '')
        return location_info

    def get_location_presence(self, location_id = None):
        self.location_id = self._location_check(location_id)

        presence_info = self.client.get_method(branch = 'locations', info = self.location_id, endpoint = 'presence')

    def add_location_space(self, location_id = None, **kwargs):
        self.location_id = self._location_check(location_id)

        space_info = {'name': '', 'description': '', 'image' : '', 'behaviors' : ['scheduling'] , 'format': 'json'}

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
        if 'is_accessible' in kwargs:
            space_info.update({'is_accessible' : kwargs['is_accessible']})

        new_space = self.client.post_method(branch = 'locations', info = self.location_id, 
            endpoint = 'spaces', params = space_info)
        return new_space

    def update_location(self, location_id = None, **kwargs):
        # this doesn't return anything if a successful update is made. Which is annoying.

        self.location_id = self._location_check(location_id)

        location_info = {'format': 'json'}

        if 'name' in kwargs:
            location_info.update({'name' : kwargs['name']})

        if 'description' in kwargs:
            location_info.update({'description' : kwargs['description']})
            
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
            location_info.update({'time_zone' : kwargs['time_zone']})
            
        updated_location = self.client.patch_method(branch = 'locations', info = self.location_id, endpoint = '', params = location_info)
        return updated_location


    def _location_check(self, location):
        #This checks to make sure a Location ID is given, and also lets the base class location ID take over in case a location isn't given here.
        if location == None:
            if self.client.loc_id == None:
                #need to make this an actual error. 
                print('No location given.')
                return 'Gotta give a location! Error!'
                
            else:
                return self.client.loc_id

        return location





