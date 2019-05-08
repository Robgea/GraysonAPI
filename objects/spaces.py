

class Spaces(object):

    def __init__(self, client):
        self.client = client


    def get_space_info(self, spaceid):
        space_return = self.client.get_method(branch = 'spaces', info = spaceid, endpoint = '')
        return space_return

    def update_space(self, spaceid, **kwargs):
        space_info = {'format' : 'json'}

        if 'name' in kwargs:
            space_info.update({'name' : kwargs['name']})

        if 'description' in kwargs:
            space_info.update({'description' : kwargs['description']})
            
        if 'image' in kwargs:
            if not kwargs['image'].startswith('http'):
                print('Image file is not a web address. Try again')
                return 'ERROR!'
            else:
                space_info.update({'image' : kwargs['image']})

        if 'capacity' in kwargs:
            space_info.update ({'capacity' : kwargs['capacity']})

        # going to come back to this to add potential categories.

        updated_space = self.client.patch_method(branch = 'spaces', info = spaceid , endpoint = '', params = space_info)
        return updated_space

    def delete_space(self, spaceid):
        pass