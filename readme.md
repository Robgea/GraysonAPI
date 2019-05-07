## Grayson API

This is a python wrapper designed to work with the Robin room management service (find out more at: https://robinpowered.com/ ). 

This is being done as a personal project and without the support of the Robin staff.


# Feature List (so far):

* Logs you into the Robin API (you need a valid API key and your organization name to do this.)

* Get a user list for your organization.

* Get a list of user emails in your organization.

* Add a user to your organization.

* Get a list of locations in your organization.

* Add a location to your organization.

* Get a list of amenities in your organization.

* More coming soon. 

All of this is very rough right now, and will be edited in the coming days (and delegated properly to be more organized.)

# Example of use:

Everything is being delegated to the relevant sub-parts of the API. The outline so far:

### Organizations:

- List users in your organization.
 .organization.get_users()
- Get user emails in your organization.
 .organization.get_user_emails()
- Add a user to your organization.
 .organization.add_user(name = 'relevant name', email = 'relevant email')
- Get a list of locations in your organization. 
.organization.get_locations()
- Add a location to your organization. 
.organization.add_location(name = 'relevant name', address = 'optional', description = 'optional', image = 'optional url')
- Get a list of amenities in your organization. 
.organization.get_amenities()

### Sample Code:

```python

from grayson import GraysonAPI

gray = GraysonAPI(org_name, API_key)

#invite a user

gray.organization.add_user(name = 'Jason Todd', email = 'BoyWonder2@waynecorp.com)

# get a list (really a dict) of user e-mails in the org

user_list = gray.organization.get_user_emails()
print(user_list)

> {'Bruce Wayne' : 'worldsgreatestdetective@waynecorp.com', 'Alfred Pennyworth' : 'stillabutler@waynecorp.com', 
> 'Dick Grayson' : 'AmazingGraysonJr@waynecorp.com', 'Jason Todd' : 'BoyWonder2@waynecorp.com'}

#add a location

gray.organization.add_location(name = 'The Batcave', address = '1007 Mountain Drive, Gotham, NJ', description = 'Home of the world's largest penny.')

#list locations

location_list = gray.organization.get_locations()
print(location_list)




```

## Next up

Adding control over specific room spaces. 
Finding room availability
Reserving rooms
Releasing reservations on rooms.

Eventually proper error handling.


## Bugs?

API doesn't check to see if Locations already exist with same data. Will be adding a check to prevent this from happening.


## Questions
