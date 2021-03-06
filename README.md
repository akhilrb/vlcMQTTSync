# VMS

A Python utility to keep multiple devices playing the same video file in sync, using MQTT.

(Originally made for easing out movie-watching for nerdy long-distance-relationships)

The module can be run on a device connected locally to the device hosting the VLC session.  
For example, it is possible to have machine __A__ (with internet access), connected locally to a machine __B__ (with or without internet access) running a VLC session and control the __B__'s playback. This essentially is the typical RC interface provided by videoLAN over a telnet interface.

## Configuration and Requirements

On your host machine, go to  
`VLC > Tools > Preferences > All Settings > Interface > Main Interfaces > Lua`  
and edit these options for Lua Telnet:

```
Host 		: <Find the local IP of the host and insert here>
Port 		: <port>
Password 	: <password>
```

The utility runs on Python3.7. A stale branch for Python3.6 is available. It features no GUI and is not extremely friendly to interface.

Use `pip3 install -r requirements.txt --user` to install necessary modules.

## Usage

1. Run `vms.py` and `master.py`.
2. Wait for all connections to establish.
3. Open same files on different systems connected to the internet.
4. Use the `master.py` script to send commands/messages.

`master.py` can send various commands (most of the ones provided in the VideoLAN interface) to control behaviour on all screens.  
Send `h` for a list of available commands, or `x` to exit.

Due to the VLC Interface responding only to specific commands, the `master.py` interface doubles up as a group chat, where each message is sent to all live users!  
The messages can be sent from the `master` shell and can be received on the `vms` shell.

## Examples

### Public Server

For a quick test, a config file for Mosquitto's public server is already provided with the configuration:

```
MQTT Broker IP/Server: test.mosquitto.org
MQTT Port: 1883
MQTT Topic: vlcMQTTSyncPublic
VLC Host IP: localhost
Host Port: 4212
Host Password: test
```


The configurations can be done manually as well.

Run `python3 vms.py`, choose option 1, and follow-up with:

```
MQTT Broker IP/Server: test.mosquitto.org
MQTT Port: 1883
MQTT Topic: randomTopic
VLC Host IP: localhost
Host Port: 4212
Host Password: ****
```

If the above server doesn't work out for you, consult [this list](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers) of publicly available MQTT servers.

Some public servers allow traffic only on certain ports. The server `test.mosquitto.org` for example, listens on the following ports:
* 1883 : MQTT, unencrypted
* 8883 : MQTT, encrypted
* 8884 : MQTT, encrypted, client certificate required
* 8080 : MQTT over WebSockets, unencrypted
* 8081 : MQTT over WebSockets, encrypted


### Private Servers

Run `python3 vms.py`, choose option 2, and follow-up with:

```
MQTT Broker IP/Server: <server-ip>
MQTT Port: 1883
MQTT Topic: customTopic
MQTT Username: <username>
MQTT Password: *******
VLC Host IP: localhost
Host Port: 1437
Host Password: *******
```

### Using a separate interface

The only change that needs to be made when `vms` and VLC sessions are running on different devices is giving the correct VLC Host IP and port and making sure the VLC host is configured to listen to it.

```
MQTT Broker IP/Server: test.mosquitto.org
MQTT Port: 1883
MQTT Topic: randomTopic
VLC Host IP: 192.168.1.5
Host Port: 4212
Host Password: *******
```

## Saved configurations

All configurations are saved in the `config` folder and are accessible by `vms.py` as well as `master.py`

---

## Update

I'm thinking of refactoring this project to:
* ~~make it more modular in terms of features~~
* ~~send and receive encrypted messages~~
* implement rooms
* eventually support a GUI : possibly a floating widget that can expand into the chat window.

Please feel free to submit a pull request :)


