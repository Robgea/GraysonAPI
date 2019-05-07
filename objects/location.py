class Location(object):

    def __init__(self, client):
        self.client = client

    # locations start here.

    '''as a principle, the base class can have the location included in it,
     however all of the methods here allow for a location to be specified. The method location info will always overwrite the base info
     so that you can find out about locations that aren't the one the user is in at the moment.'''

    def get_location_spaces(self, location_id = None):

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




    #reserve a space
    '''check to see if the input is an integer, if it is, great, if not then run the string through a search, 
    see if the length of the return is greater than 1, if so return the list. If not, book the room.'''

    def end_function(self):
        pass