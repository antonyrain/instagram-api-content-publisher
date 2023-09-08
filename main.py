import requests
import hashtags
import datetime
import time

print("start")

ig_user_id = " "
access_token = " "
api_graph = "https://graph.facebook.com/v17.0/"

file = open("./images.txt", "r")
for line in file:
    capt = "Available for purchase: Link in Bio! " + hashtags.random_tags()

    def create_container(api, id, token):
        url = api + id + '/media'
        payload = {
            'image_url': line,
            'caption': capt,
            'access_token': token
        }
        r = requests.post(url, params=payload)
        response = r.json()
        return response

    def publish_container(api, id, creation_id, token):
        url = api + id + "/media_publish"
        payload = {
            'creation_id': creation_id,
            'access_token': token
        }
        r = requests.post(url, params=payload)
        response = r.json()
        return response

    res = create_container(api_graph, ig_user_id, access_token)
    creation_id = res["id"]
    
    time.sleep(2)
    publish_container(api_graph, ig_user_id, creation_id, access_token)

    x = datetime.datetime.now()
    print(x)

    time.sleep(1800)

print("finish")