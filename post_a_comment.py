import requests
from constants import base_url,app_access_token
from get_post_id import get_post_id
#Working
# 8. Function declaration to post a comment on a user's media

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": app_access_token, "text": comment_text}
    request_url = (base_url + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)
    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print ('Successfully added a new comment!')
    else:
        print ('Unable to add comment. Please try again!')
