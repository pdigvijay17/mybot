import requests
from constants import base_url,app_access_token
def my_info():
  request_url = (base_url+ 'users/self/?access_token=%s') % (app_access_token)
  print ('GET request url : %s'% (request_url))
  user_info = requests.get(request_url).json()


  if user_info['meta']['code'] == 200:

      if len(user_info['data']):
          print('Username: %s','blue') % (user_info['data']['username'])
          print ('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
          print ('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
          print ('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
      else:
          print ('User does not exist!')

  else:
      print ('Status code other than 200 received!')