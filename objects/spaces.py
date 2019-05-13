import datetime

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

        deletion_return = self.client.delete_method(branch = 'spaces', info = spaceid, endpoint = '')
        return deletion_return

    def get_space_events(self, spaceid, before = None, after = None):
        #This has a working syntax now, will make it so that you can specify timing later.

        #replacing this with a default that looks to twenty days before and after now. Then letting people pick the days to look at. Not letting the time be editable.


        if before == None:
            #before = f'{datetime.date.today().isoformat()}T00:01:00Z'
            before = '2019-05-09T11:16:00Z'

        if after == None:
            #after = f'{datetime.date.today().isoformat()}T23:59:00Z'
            after = '2019-01-09T11:16:00Z'

        #before = '2019-05-09T11:16:00Z', after = '2019-01-09T11:16:00Z'

        event_range = {'before' : before , 'after' : after, 'format' : 'json'}
        print(event_range)
        events_return = self.client.get_method(branch = 'spaces', info = spaceid, endpoint = 'events', params = event_range)
        return events_return


    def book_event(self, spaceid, **kwargs):
        #This is still broken. Don't know why.
        booking_info = {
        "title" : "Batmeeting",
        'description' : 'Someone has been eating the bat cookies',
        'start' : {'date_time' : str(datetime.datetime.now().isoformat()),
        'time_zone' : 'America/New_York'},
        'end' : 
        { 'date_time' : str(datetime.datetime(2019, 5, 10, hour = 23, minute = 50, second = 0).isoformat()),
        'time_zone' : 'America/New_York'},
        'invitees' : [{'email' : 'zhouenkissinger@gmail.com'}], 'format' : 'json'}
        print(booking_info)
        events_return = self.client.post_method(branch = 'spaces', info = spaceid, endpoint = 'events', params = booking_info)
        return events_return



    def get_space_amenities(self, spaceid):
        space_return = self.client.get_method(branch = 'spaces', info = spaceid, endpoint = 'amenities')
        return space_return



    def delete_space_amenity(self, spaceid = None, amenityid = None):
        if spaceid == None or amenityid == None:
            print('Need to submit both a "spaceid" and "amenityid".')
            return 'Need to submit both a "spaceid" and "amenityid".'

        deletion_return = self.client.delete_method(branch = 'spaces', info = spaceid, endpoint = f'amenities/{amenityid}')
