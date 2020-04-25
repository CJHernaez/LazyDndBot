import discord
import sqlite3
import logging
import os.path
from os import path
import json
from discord.utils import get


from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio

from DND.Roller import Roller

client = commands.Bot(command_prefix = ".")


from DB.DBGenerator import GenerateDB
from DBHelper import DBHelper
from DND.Character import Character
from DND.CharacterHelper import CharacterHelper
from MessageHelper import MessageHelper
from UserHelper import UserHelper

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


try:
    with open('Oirasor.json') as f:
        veila = Character(json.load(f))
    characterHelper.uploadCharacter(veila)


    with open('Amsyl.json') as f:
        veila = Character(json.load(f))
    characterHelper.uploadCharacter(veila)


    with open('Hessai.json') as f:
        veila = Character(json.load(f))
    characterHelper.uploadCharacter(veila)


    with open('Rosario.json') as f:
        veila = Character(json.load(f))
    characterHelper.uploadCharacter(veila)


except sqlite3.IntegrityError:
    print('characters already created')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def setPadding(triggerPhrase):
    characterHelper.setBasePadding(triggerPhrase)
    dbHelper.setBasePadding(triggerPhrase)
    userHelper.setBasePadding(triggerPhrase)

triggerlength = 1
setPadding(triggerlength)


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


roller =  Roller()
roller.setMessageHelper(messageHelper)

@client.command()
async def roll(ctx):
    if ctx.message:
        roll = roller.roll(ctx.message) # this is going to be a message due to the on_message

        await ctx.channel.send(roll)

@client.event
async def on_message(message):
    # if message.author.name == 'Prophecies':
    #     clientMember = [x for x in message.channel.members if 'lazydndbot' in x.name.lower()][0]
    #     await clientMember.edit(nick='LazyDndBot')

    if message.author == client.user:
        return
    tokenizedMessage = message.content.replace(',','').split(' ')
    if messageHelper.checkUserTriggerValues(message):
       # if ([x for x in message.author.roles if x.name == "Dev"]): #dont touch this unless you know what you are doing - CJ 2020
            print (messageHelper.getDiscordTagByMessage(message) + ' is a valid user')
            if 'db' in tokenizedMessage[triggerlength]:
                await  dbHelper.getAllFromTable(message)
            else:
                await characterHelper.Handle(message)

    if ('hello') in message.content:
        await message.channel.send('Hello, {0.author}!'.format(message))

    await client.process_commands(message)

client.run(userFile.read())