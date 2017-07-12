import requests,urllib
from fetch_user_id import fetch_user_id
from constants import base_url,app_access_token
# 4. Function declaration to get the any post of another user(Index range from 0-19)


def fetch_user_post(insta_username):
    user_id = fetch_user_id(insta_username)
    if user_id == None:
        print ('User does not exist!','red')
        exit()

    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:

        if len(user_media['data']):

            post_number = int(raw_input("Enter the post number you would like to download")) #Please Note: if entered '20', index out of range error is shown.
            image_name = user_media['data'][post_number]['id'] + '.jpeg'
            image_url = user_media['data'][post_number]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)

            print ('Your image has been downloaded!',)
        else:
            print ('Post does not exist!')

    else:
        print ('Status code other than 200 received!')