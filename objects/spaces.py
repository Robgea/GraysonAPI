

class Spaces(object):

    def __init__(self, client):
        self.client = client


    def get_space_info(self, spaceid):
        space_info = self.client.get_method(branch = 'spaces', info = spaceid, endpoint = '')
        return space_info

    def update_space(self, spaceid):
        pass

    def delete_space(self, spaceid):
        pass