import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Thread,ChatMessage



class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected")
        # getting keyword from url
        other_user = self.scope['url_route']['kwargs']['username']   # other user to whome i am chatting
        me = self.scope['user']  # requested user

        thread_obj = await self.get_thread(me,other_user)
        self.thread = thread_obj
        print(thread_obj,me)
        chat_room = f"thread_{thread_obj.id}"
        self.chat_room = chat_room
        

        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )

        await self.send({
            "type":"websocket.accept"
        })

        
        


      
    
    async def websocket_receive(self,event):
        print("receiver",event)
        #{'type': 'websocket.receive', 'text': '{"message":"again sending"}'}
        text_feild = event.get('text',None)
        if text_feild:
            data = json.loads(text_feild)
            msg = data.get('message')
            print(msg)

            user = self.scope['user'] 
            await self.create_chat_message(msg,user)


            send_data = {
                'username':user.username,
                'message':msg
            }
        # broadcasts the msg to chat_msssage
        await self.channel_layer.group_send(
            self.chat_room,
            {
                "type": "chat.message",
                "text": json.dumps(send_data),
            }
        )


            
           
            
# sends the actual msg
    async def chat_message(self, event):
        await self.send({
            "type":"websocket.send",
            "text":event['text'],
        })

    
    async def websocket_disconnect(self,event):
        print("disconnect",event)
    
    @database_sync_to_async   # to avoid memory leaks 
    def get_thread(self,user,other_username):
        return Thread.objects.get_or_new(user,other_username)[0]

    
    @database_sync_to_async
    def create_chat_message(self,msg,me):
        thread_obj = self.thread
        ChatMessage.objects.create(thread=thread_obj,user=me,message=msg)
