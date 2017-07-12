import  requests
from constants import base_url,app_access_token
from fetch_user_id import  fetch_user_id
#Function declaration to get the post id of another user's recent post.

def get_post_id(insta_username):
    user_id = fetch_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (base_url+ 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:

        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print ('There is no recent post of the user!')
            exit()

    else:
        print ('Status code other than 200 received!')
        exit()
