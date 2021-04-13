import discord
import os
from keep_alive import keep_alive
from discord.ext import tasks
from datetime import datetime
from msg import Msg

users_hash_dict={
    '8614': 'dominik',
    '0261': 'maciek',
    '3164': 'swistak',
    '7770': 'gross',
    '4426': 'bartus',
    '2567': 'sebus',
    '6249': 'karol',
    '2010': 'ryba'
}

messages_dict={
    'pogoda':Msg('messages/pogoda_mess.txt'),
    'hania':Msg('messages/hania_mess.txt'),
    'default':Msg('messages/default_mess.txt'),
    'amelka':Msg('messages/amelka_mess.txt'),
    'papiez':Msg('messages/papiez_mess.txt'),
    'hour':Msg('messages/hour_mess.txt'),
    'ryba':Msg('messages/ryba_mess.txt'),
    'swistak':Msg('messages/swistak_mess.txt'),
    'grosik':Msg('messages/grosik_mess.txt'),
    'dominik':Msg('messages/dominik_mess.txt'),
    'karol':Msg('messages/karol_mess.txt'),
    'gra':Msg('messages/gra_mess.txt'),
    'bartus':Msg('messages/bartus_mess.txt'),
    'sebus':Msg('messages/sebus_mess.txt'),
    'maciek':Msg('messages/maciek_mess.txt')
}

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def get_active_members_count():
    members_count=0
    for member in client.get_all_members():
        if str(member.status) == 'online':
            members_count += 1
    return members_count

def get_general_channel():
    channel=""
    for chan in client.get_all_channels():
        if chan.name == "ogólny":
            channel = client.get_channel(chan.id)
    return channel

def get_time_token():
    date= datetime.now()
    if date.hour==21 and date.minute==37:
        return 'papiez'
    if date.minute%1==0:
        return 'hour'

def detect_message(message):
    if "amel" in message:
        return 'amelka'
    elif "hani" in message:
        return 'hania'
    elif "pogod" in message:
        return 'pogoda'
    elif "gra" in message:
        return 'gra'
    return 'default'

def person_detector(author):
    return users_hash_dict[str(author[-4:])] if str(author[-4:]) in users_hash_dict else 'default'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return
    if msg.startswith("$ryba"):
        print(person_detector(str(message.author)))
        return
    if msg.startswith("ryba"):
        if detect_message(msg)!='default':
            msg=messages_dict[detect_message(msg)].choose_message()
            await message.channel.send(msg)
            return
        else:
            msg=messages_dict[person_detector(str(message.author))].choose_message()
            await message.channel.send(msg)


@tasks.loop(seconds=60)
async def mytask():
    members_count=get_active_members_count()
    channel=get_general_channel()
    detector=get_time_token()
    message=messages_dict[detector].choose_message()
    if members_count>2:
        await channel.send(message)

mytask.start()
keep_alive()
client.run(os.getenv('TOKEN'))

