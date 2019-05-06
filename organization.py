

class Organization(object):

    def __init__(self, client):
      self.client = client
        
    def get_users(self):
        users_output = self.client.get_method(branch = 'organizations', endpoint = 'users')
        return users_output

    #gets parsed user info, used to check that an invite hasn't already been sent.
    def get_user_emails(self):
        users_output = self.client.get_method(branch = 'organizations', endpoint = 'users')
        output_dict = { user['name'] : user['primary_email']['email'] for user in users_output}
        return output_dict
        
    def get_locations(self):
        locations_output = self.client.get_method(branch = 'organizations', endpoint = 'locations')
        return locations_output

    def get_amenities(self):
        amenities_output = self.client.get_method(branch = 'organizations', endpoint = 'amenities')
        return amenities_output