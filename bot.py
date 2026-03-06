import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", BAG4lpkAvBuoAo_F915BK3GHuuwrZzZe6oyh5GtO5CUk12h4G_FfK5li22dt46oq4W-f_HSW5JfMrhT1uwDZ1LHjbcCxlmTuknNrC_o72OT10hvg7rgGqAOekLX1LtBMw_NfmF0Vi5bhjxNvo-qTg9SRhn-xGkuzas7sybrsUFldU4yDo5VwR5ssvHSFiLaR61HfVMJLcpe_ouQNK2QD8dDrGX2kYu7MlDaPG8EeNY14bv3pYQ5gAmfkHg21ouhLgdcVL0kCX65tXBC-vlvMbgy73_V0Wwic2A2BS8d58AAr4BjwEp6Y8PG6T3hhzOYxkLhXo8jGQQIVKnBrjI54AoK-ahvX5AAAAAGc40A7AA)        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







