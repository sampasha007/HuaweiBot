# -*- coding: UTF-8 -*-
import telepot
from emoji import emojize
from pprint import pprint
import sys
import time
import image
import urllib
from yahoo_finance import Share
from PyDictionary import PyDictionary
import re
import pywapi
from mail import * 


dictionary=PyDictionary()
#emoji section

traffic=emojize(":traffic_light:",use_aliases=True)
vtraffic=emojize(":vertical_traffic_light:",use_aliases=True)
car=emojize(":car:",use_aliases=True)
bcar=emojize(":blue_car:",use_aliases=True)
on=emojize(":oncoming_automobile:",use_aliases=True)
rcar=emojize(":red_car:",use_aliases=True)
grin=emojize(":grin:",use_aliases=True)
smile=emojize(":smile:",use_aliases=True)
chart=emojize(":chart_with_upwards_trend:",use_aliases=True)
diamond=emojize(":large_blue_diamond:",use_aliases=True)
book=emojize(":notebook_with_decorative_cover:",use_aliases=True)
book1=emojize(":book:",use_aliases=True)
cloud=emojize(":cloud::cloud::cloud:",use_aliases=True)
sun=emojize(":sunny::sunny::sunny:",use_aliases=True)
fog=emojize(":foggy::foggy::foggy:",use_aliases=True)
part=emojize(":partly_sunny::partly_sunny::partly_sunny:",use_aliases=True)
moneky=emojize(":see_no_evil::see_no_evil::see_no_evil:",use_aliases=True)
degree_sign= u'\N{DEGREE SIGN}'
scream=emojize(":scream::scream::scream::scream:",use_aliases=True)


age=["What is your age?","What's your age?","How old are you?"]
parking=["parking?","Which slot is free?","Where can i park my car?","Parking?",car,rcar,traffic,vtraffic,on,bcar]
sup=["What's up?","Sup?"]
mails=["send an email","mail it","mail","email"]



Token="533211671:AAGIZiSMJoh8XP2IfCeFXZ6Si5-QTp6Sh-o"
id=533211671
bot=telepot.Bot(Token)

def mailing(msg):
	server.sendmail(gmail_user, [TO], BODY)
	return "email sent successfully!!"


def weather(msg):
	try:

	  if msg:

		city = msg
		lookup = pywapi.get_location_ids(city)
		for i in lookup:
			location_id = i
		weather_com_result = pywapi.get_weather_from_weather_com(location_id) 
		cond=weather_com_result['current_conditions']['text'].lower() 
		temp=weather_com_result['current_conditions']['temperature'] 
		if cond=="haze":
			emo=fog
		elif cond=="mostly cloudy":
			emo=cloud	
		elif cond=="fair":
			emo=part
		elif cond=="clear":
			emo=sun
		elif cond=="partly cloudy":
			emo=cloud
		elif cond=="cloudy":
			emo=cloud    
		else:
			emo=moneky
				
			
	  message="Weather Conditions\n=================\n"+msg+"\n"+emo+"\n\nIt is "+cond+" and "+temp+degree_sign+ "C"
	  return message

	except:
	   return "error"  

def meaning(msg):
	try:

	 url1 = "http://dictionary.reference.com/browse/"
	 word =msg
	 url1 = url1 + word
	 data = urllib.urlopen(url1).read()
	 data1 = data.decode("utf-8")
	 m = re.search('meta name="description" content="', data1)
	 start = m.end()
	 end = start + 300
	 newString = data1[start: end]
	 m = re.search("See more.", newString)
	 end = m.start() - 1
	 definition = newString[0:end]
	 return definition

	except:

		return "error"
	 


def stock(msg):
	val=Share(msg)
	val.refresh()
	val=val.get_price()
	message="The value of the requested Stock "+msg+" is "+str(val)
	return message



def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		text=msg['text']
		name=msg['chat']['first_name']
		if text.startswith(("Hey","Hello","Hi","hey","hello","hi")):
			 message=emojize("Hello "+name+" how can i help you?:smile:",use_aliases=True)
			 #bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
			 bot.sendMessage(chat_id,message)
			 #bot.sendVoice(chat_id=chat_id, voice=open('/Users/sameerpasha/Desktop/file.ogg', 'rb'))

		elif text in mails:
			bot.sendChatAction(chat_id,"typing")
			message=mailing(text)
			bot.sendMessage(chat_id,message)



		elif text in sup:
			bot.sendChatAction(chat_id,"typing")
			bot.sendMessage(chat_id,"Nothing Much, What about you?")
			bot.sendMessage(chat_id,"Sorry for generic reply lol, i am a bot afterall xD  or am i?")
			bot.sendMessage(chat_id,scream)	 
		elif text=="/start":
			message="Hello "+name+" how can i help you?"+smile
			bot.sendMessage(chat_id,message)
			message="Instructions\n=========\n\n"+diamond+"For parking use any car emoji or the 2 traffic emoji or any parking keyword\n\n"+diamond+"for stock use Stock follwed by name anything but ending should be name of the stock like GOOG,FB,AAPL(enter one stock duh)\n\n"+diamond+"for meaning type Meaning follwed by anything but ending should be the word you need the meaning for \n\n"+diamond+"for opposites start with Opposite,Opp,Antonymn,Not and end with the word\n\n"+diamond+"Same goes for synonym, Synonym Like just Same Similar, start with any keyword and end with the word.\n\n"+diamond+"For weather use Weather,Forecast,Climate the any sentence but end with for follwed by city like Chennai or you can get specific like (City,Country)!! "+smile
			bot.sendMessage(chat_id,message)

		elif text.startswith(("Weather","Climate for","Forecast for")):
			t=text.rsplit("for", 1)[-1]
			print t
			if t=="Weather":
			    message=weather("chennai")
			    bot.sendChatAction(chat_id,"typing")
			    bot.sendMessage(chat_id,message)

			else:
			    			
			    message=weather(t)
			    if message=="error":
				     bot.sendMessage(chat_id,"Please check the word you have typed again!!! "+smile+smile)
			    else:
				     bot.sendChatAction(chat_id,"typing")
				     bot.sendMessage(chat_id,message)	
		
		elif text.startswith("Meaning"):
			t=text.rsplit(None,1)[-1]
			word=meaning(t)
			if word=="error":
				bot.sendChatAction(chat_id,"typing")
				bot.sendMessage(chat_id,"Please check the word you have typed again!!! "+smile+smile)
			else:
				message="Meaning of the word "+t.upper()+" is \n\n"+word
				bot.sendChatAction(chat_id,"typing")
				bot.sendMessage(chat_id,message)

		elif text=="Who are you?":
			message="I am a bot, i was created for you homo sapiens, to make you life easier, you can ask me anything!!!"
			bot.sendChatAction(chat_id,"typing")
			bot.sendMessage(chat_id,message)
			bot.sendMessage(chat_id,emojize(":smile:",use_aliases=True))

		elif text.startswith(("Similar","Same","Just","Like","Synonym")):
			t=text.rsplit(None, 1)[-1]
			synonym=dictionary.synonym(t)
			x='\n'.join(str(p) for p in synonym)
			message="The synonym of the word "+t.upper()+" is\n\n"+x
			bot.sendChatAction(chat_id,"typing")
			bot.sendMessage(chat_id,message)

		elif text.startswith(("Opposite","Opp","Not","Antonym")):
			t=text.rsplit(None, 1)[-1]
			antonym=dictionary.antonym(t)
			y='\n'.join(str(q) for q in antonym)
			message="The antonym of the word "+t.upper()+" is\n\n"+y
			bot.sendChatAction(chat_id,"typing")
			bot.sendMessage(chat_id,message) 

		elif text.startswith(("I","Want","Need","Stock")):
			text=text.rsplit(None, 1)[-1]
			bot.sendMessage(chat_id,"Sure "+grin)
			message=stock(text)
			bot.sendChatAction(chat_id,"typing")
			bot.sendMessage(chat_id,message)

		elif text=="What can you do?":
			message=diamond+" I can help you find parking space for your "+car+"\n\n"+diamond+" I can help you find Price of stocks "+chart+"\n\n"+diamond+"I can help you find Meanings of words,Their Opposites and Synonyms  "+book+book1+book
			bot.sendChatAction(chat_id,"typing")
			bot.sendMessage(chat_id,message)
				
		
		elif text=="what is your name?":
			 message="my name is Bud, but you can call me whatever you like ^_^"
			 bot.sendChatAction(chat_id,"typing")
			 bot.sendMessage(chat_id,message)	

		else:
			text=text.replace(" ","+")
			text=text.replace("?","%3F")
			text=text.replace("'","%27")
			message="http://lmgtfy.com/?q="+text
			bot.sendChatAction(chat_id,"typing")
			bot.sendMessage(chat_id,message)


			

bot.message_loop(handle)
print ('Listening ...')


while 1:
	time.sleep(5)

