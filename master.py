#!/usr/bin/python3

import sys
import telnetlib
import getpass
import paho.mqtt.publish as publish

# if arguments have been passed, prepare list
args = []
for arg in sys.argv:
    args.append(arg)
n = len(args)

# command was directly executed
if(n == 1):
	mqttBrokerIP = input("MQTT Broker IP: ")
	mqttPort = input("MQTT Port: ")
	mqttTopic = input("MQTT Topic: ")
	mqttUsername = input("MQTT Username: ")
	print("MQTT ", end='')
	sys.stdout.flush()
	mqttPassword = getpass.getpass()

# command was executed with arguments
elif(n == 6):
	mqttBrokerIP = args[1]
	mqttPort = args[2]
	mqttTopic = args[3]
	mqttUsername = args[4]
	mqttPassword = args[5]

# wrong number of arguments
else:
	print("Wrong number of arguments!")
	print("Usage:\npython3 vlcMQTTSync.py\nor\npython3 vlcMQTTSync.py <brokerIP> <port> <topic> <username> <password>")
	print("Exiting...")
	sys.exit()

auther = {'username':mqttUsername, 'password':mqttPassword}

print("Enter 'h' for a list of available functions")
while True:
	x = input("Message: ")
	if(x == 'h'):
		print("| add XYZ  . . . . . . . . . . . . . . . . . . . . add XYZ to playlist")
		print("| enqueue XYZ  . . . . . . . . . . . . . . . . . queue XYZ to playlist")
		print("| delete [X] . . . . . . . . . . . . . . . . delete item X in playlist")
		print("| move [X][Y]  . . . . . . . . . . . . move item X in playlist after Y")
		print("| sort key . . . . . . . . . . . . . . . . . . . . . sort the playlist")
		print("| sd [sd]  . . . . . . . . . . . . . show services discovery or toggle")
		print("| play . . . . . . . . . . . . . . . . . . . . . . . . . . play stream")
		print("| stop . . . . . . . . . . . . . . . . . . . . . . . . . . stop stream")
		print("| next . . . . . . . . . . . . . . . . . . . . . .  next playlist item")
		print("| prev . . . . . . . . . . . . . . . . . . . .  previous playlist item")
		print("| goto, gotoitem . . . . . . . . . . . . . . . . .  goto item at index")
		print("| repeat [on|off]  . . . . . . . . . . . . . .  toggle playlist repeat")
		print("| loop [on|off]  . . . . . . . . . . . . . . . .  toggle playlist loop")
		print("| random [on|off]  . . . . . . . . . . . . . .  toggle playlist random")
		print("| clear  . . . . . . . . . . . . . . . . . . . . .  clear the playlist")
		print("| title [X]  . . . . . . . . . . . . . . set/get title in current item")
		print("| chapter [X]  . . . . . . . . . . . . set/get chapter in current item")
		print("| ")
		print("| seek X . . . . . . . . . . . seek in seconds, for instance `seek 12'")
		print("| pause  . . . . . . . . . . . . . . . . . . . . . . . .  toggle pause")
		print("| fastforward  . . . . . . . . . . . . . . . . . . set to maximum rate")
		print("| rewind . . . . . . . . . . . . . . . . . . . . . set to minimum rate")
		print("| faster . . . . . . . . . . . . . . . . . .  faster playing of stream")
		print("| slower . . . . . . . . . . . . . . . . . .  slower playing of stream")
		print("| normal . . . . . . . . . . . . . . . . . .  normal playing of stream")
		print("| rate [playback rate] . . . . . . . . . .  set playback rate to value")
		print("| frame  . . . . . . . . . . . . . . . . . . . . . play frame by frame")
		print("| fullscreen, f, F [on|off]  . . . . . . . . . . . . toggle fullscreen")
		print("| ")
		print("| volume [X] . . . . . . . . . . . . . . . . . .  set/get audio volume")
		print("| volup [X]  . . . . . . . . . . . . . . .  raise audio volume X steps")
		print("| voldown [X]  . . . . . . . . . . . . . .  lower audio volume X steps")
		print("| achan [X]  . . . . . . . . . . . .  set/get stereo audio output mode")
		print("| atrack [X] . . . . . . . . . . . . . . . . . . . set/get audio track")
		print("| vtrack [X] . . . . . . . . . . . . . . . . . . . set/get video track")
		print("| vratio [X] . . . . . . . . . . . . . . .  set/get video aspect ratio")
		print("| vcrop, crop [X]  . . . . . . . . . . . . . . . .  set/get video crop")
		print("| vzoom, zoom [X]  . . . . . . . . . . . . . . . .  set/get video zoom")
		print("| vdeinterlace [X] . . . . . . . . . . . . . set/get video deinterlace")
		print("| vdeinterlace_mode [X]  . . . . . . .  set/get video deinterlace mode")
		print("| snapshot . . . . . . . . . . . . . . . . . . . . take video snapshot")
		print("| strack [X] . . . . . . . . . . . . . . . . .  set/get subtitle track")
		print("| ")
		print("| vlm  . . . . . . . . . . . . . . . . . . . . . . . . .  load the VLM")
		print("| logout . . . . . . . . . . . . . .  exit (if in a socket connection)")
		print("| quit . . . . . . . .  quit VLC (or logout if in a socket connection)")
		print("| shutdown . . . . . . . . . . . . . . . . . . . . . . .  shutdown VLC")
		print()
	else:
		publish.single(mqttTopic, x, hostname=mqttBrokerIP, auth=auther, port=int(mqttPort))