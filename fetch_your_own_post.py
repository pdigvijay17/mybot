import requests,urllib
from constants import base_url,app_access_token
# 3. Function declaration to get any post of your own account.(range 0-19)

def fetch_your_own_post():
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:

        if len(own_media['data']):

            own_post_number = int(raw_input("Enter the image number you would like to download."))
            image_name = own_media['data'][own_post_number]['id'] + '.jpeg'
            image_url = own_media['data'][own_post_number]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print ('Your image has been downloaded!')
        else:
            print ('Post does not exist!')

    else:
        print ('Status code other than 200 received!')




