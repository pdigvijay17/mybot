import requests
from constants import base_url,app_access_token
from get_post_id import get_post_id

# Working
# 7. Function declaration to get the comment list from the user's post.

def get_comments_list(insta_username):
    media_id = get_post_id(insta_username)
    if media_id is None:
        print ("There is no media")
    else:
        request_url = base_url + "media/%s/comments/?access_token=%s" % (media_id, app_access_token)
        print "Get request url:%s" % request_url
        comment_list = requests.get(request_url).json()

    # check the status code, if comes 200 then show the list of comments
    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            print "The comments on the post :"
            for x in range(len(comment_list['data'])):
                comment_text = comment_list['data'][x]['text']
                print "comment: %s" % (comment_text)

        else:
            print ("No comments on this post")
    else:
        print ("Status code other than 200")