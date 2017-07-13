import requests
from constants import base_url,app_access_token
from get_post_id import get_post_id
#Working
# 6. Function declarartion to post a like on the user's media.

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/likes') % (media_id)
    payload = {"access_token": app_access_token}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()

    if post_a_like['meta']['code'] == 200:
        print ('Like was successful!')
    else:
        print ('Your like was unsuccessful. Please try again!',)