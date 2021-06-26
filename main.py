from vk_api.utils import get_random_id
import vk_api
import script

TOKEN = '4814719fffe9a305824e2bdb60cdadee8d9c8529a8c2e62244d0b71613f73036501a74c070bf9f07f072e'
vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()

bot_run = True

while bot_run:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        id_user = messages["items"][0]["last_message"]["from_id"]
        if messages['count'] >= 1:
            if messages['items'][0]['last_message']['attachments'] is not None:
                script.downloadImage(
                    url_img=messages['items'][0]['last_message']['attachments'][0]['photo']['sizes'][-1]['url'],
                    path_to_image='before')
                script.distortImage(img_before='before',
                                    img_after='after')
                upload = vk_api.VkUpload(vk)
                photo = upload.photo_messages('after.jpg')
                owner_id = photo[0]['owner_id']
                photo_id = photo[0]['id']
                access_key = photo[0]['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                vk.method("messages.send", {"peer_id": id_user,
                                            "attachment": attachment,
                                            "random_id": get_random_id()})

    except Exception as error:
        print(error)
