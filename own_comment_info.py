import requests
from constants import base_url,app_access_token
from fetch_own_post_id import fetch_own_post_id


#Working.
# 11. Function to get information of your own comment

def own_comment_info():

    media_id = fetch_own_post_id()
    request_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code'] == 200:
        if len(comment_info):
            x = 0
            for x in range(len(comment_info["data"])):
                print "%s commented : %s" % (["data"][x]["from"]["username"],["data"][x]["text"])
                x = x + 1

        else:
            print ("No comments have been made.")
    else:
        print ("Status codde other than 200 received.")
