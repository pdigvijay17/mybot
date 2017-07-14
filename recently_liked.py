import requests,urllib
from constants import base_url,app_access_token


# Function to get the recent media liked by the user.

def recently_liked():

    request_url = (base_url + 'users/self/media/liked?access_token=%s') % (app_access_token)
    print 'GET request url : %s' % (request_url)
    recent_liked_media = requests.get(request_url).json()

    if recent_liked_media['meta']['code'] == 200 :
        if len(recent_liked_media):
            image_name = recent_liked_media['data'][0]['id'] + '.jpeg'
            image_url = recent_liked_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print ('Your image has been downloaded')
        else:
            print ('No media found.')
    else:
        print ('Status code other than 200 received.')
