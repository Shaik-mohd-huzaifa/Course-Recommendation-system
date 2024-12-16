from linkedin_api import Linkedin

# Authenticate using any Linkedin user account credentials
api = Linkedin("astrastudiox@gmail.com", "._Pa5r&YB93a.4k")


# GET a profile
# profile = api.get_profile("shaik-mohd-huzaifa-7b0804208")

# GET a profiles contact info
# contact_info = api.get_profile_contact_info("shaik-mohd-huzaifa-7b0804208")

# # GET 1st degree connections of a given profile
# connections = api.get_profile_connections("1234asc12304")

# results = api.search_people(keywords="Data Scientist")
# print(results)

results = api.search_people(keywords="Data Scientist")
print(results)

# print(contact_info, connections)
