import wolframalpha
client = wolframalpha.client("lilpumsaysnopeeking")

import wikipedia

import PySimpleGUI as sg
sg.theme('Darkpurple')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('ok'), sg.Button('Cancel')]]
window = sg.window('PyDa' , layout)

import pyttsx3
engine = pyttsx3.init()

while True:
	event, values = window.read()
	if event in (None, 'Cancel'):
		break
	try:
		wiki_res = wikipedia.summary(values[0].sentences=2)
		wolfram_res = next(client.query(values[0]).results).text
		engine.say(wolfram_res)
		sg.PopupNonBlocking("wolfram result: "+wolfram_res,"wikipedia Result: "+wiki_res)
	except wikipedia.exception.DisambiguationError:
		wolfram_res = next(client.query(values[0]).results).text
		engine.say(wolfram_res)
		sg.PopupNonBlocking(wolfram_res)

	except wikipedia.exception.PageError:
		wolfram_res = next(client.query(values[0]).results).text
		engine.say(wolfram_res)
		sg.PopupNonBlocking(wolfram_res)

	except:
	    wiki_res = wikipedia.summary(values[0], sentences=2)
	    engine.say(wiki_res)
	    sg.PopupNonBlocking(wiki_res)

	engine.runAndWait()
	print(values[0])

window.close()	    	
	




			
