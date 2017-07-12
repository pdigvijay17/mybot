import requests
from fetch_user_id import fetch_user_id
from constants import base_url,app_access_token
def fetch_user_info(insta_username):
    user_id = fetch_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url + 'users/%s?access_token=%s') % (user_id, app_access_token)

    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:

        if len(user_info['data']):
            print('Username: %s','blue') % (user_info['data']['username'])
            print ('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
            print ('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
            print ('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
        else:
            print ('There is no data for this user!')

    else:
        print 'Status code other than 200 received!'