

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

    def add_user(self, **kwargs):
        repeat = False
        invite_name = kwargs['name']
        invite_email = kwargs['email']

        # An error catcher should be added here soon.
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

        new_user = self.client.post_method(branch = 'organizations', endpoint = 'users', params = params)
        
        return new_user


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

        #need to add support for other parameters. Open times, etc. Low priority.

        new_location = self.client.post_method(branch = 'organizations', endpoint = 'locations', params = location_info)
        return new_location
