import requests
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from constants import base_url,app_access_token
from get_post_id import get_post_id

#Working
# 9. Function declaration to delete negative comments from a user's post.

def delete_negative_comments(insta_username):
  media_id = get_post_id(insta_username)
  request_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, app_access_token)
  print 'GET request url : %s' % (request_url)
  comment_info = requests.get(request_url).json()

  if comment_info['meta']['code'] == 200:

    if len(comment_info['data']):

        for x in range(len(comment_info['data'])):
            comment_id = comment_info['data'][x]['id']
            comment_text = comment_info['data'][x]['text']
            blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())

            if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                print 'Negative comment : %s' % (comment_text)
                delete_url = (base_url + 'media/%s/comments/%s/?access_token=%s') % (
                media_id, comment_id, app_access_token)

                print 'DELETE request url : %s' % (delete_url)
                delete_info = requests.delete(delete_url).json()

                if delete_info['meta']['code'] == 200:
                    print ('Comment successfully deleted!\n')
                else:
                    print ('Unable to delete comment!')

            else:
                print ('Positive comment: %s\n') % (comment_info)

    else:
        print ('There are no comments on this post.')

  else:
      print ('Status code other than 200 received!')