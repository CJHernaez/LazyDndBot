import discord
import sqlite3
import logging
import os.path
from os import path

from DB.DBHelper import GenerateDB
from DBHelper import DBHelper
from DND.CharacterHelper import CharacterHelper
from MessageHelper import MessageHelper
from UserHelper import UserHelper

client = discord.Client()


conn = GenerateDB()


userFile = open("userToken.txt","r")

#Configure User Helper
users = {}
userHelper = UserHelper(users, conn)
users = userHelper.refresh()

#Configure Message Helper
messageHelper = MessageHelper(userHelper)

#Configure DB Helper
dbHelper = DBHelper(conn)
dbHelper.setUserHelper(userHelper)

#Configure CharacterHelper
characters = {}
characterHelper = CharacterHelper(characters, conn)
characters = characterHelper.refresh()
characterHelper.setUserHelper(userHelper)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def setPadding(triggerPhrase):
    characterHelper.setBasePadding(triggerPhrase)
    dbHelper.setBasePadding(triggerPhrase)
    userHelper.setBasePadding(triggerPhrase)

triggerlength = 1
setPadding(triggerlength)

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    tokenizedMessage = message.content.split(' ')
    if messageHelper.checkUserTriggerValues(message):
        if ([x for x in message.author.roles if x.name == "Dev"]): #dont touch this unless you know what you are doing - CJ 2020
            print('User is a dev')
            if 'db' in tokenizedMessage[triggerlength]:
                await  dbHelper.getAllFromTable(message)
            else:
                await characterHelper.Handle(message)

    if ('hello') in message.content:
        await message.channel.send('Hello, {0.author}!'.format(message))


client.run(userFile.read())