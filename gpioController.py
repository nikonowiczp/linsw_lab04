from calendar import c
from threading import Thread
from unittest import skip
import time;
import sys;
#import gpiod;
import mpd;

requestedButtons = [25,10,17,18]
requestedButtonsNice = {
    "pause-play" : requestedButtons[0],
    "volume-up" : requestedButtons[1],
    "volume-down" : requestedButtons[2],
    "skip" : requestedButtons[3]
};
requestedLeds = [23,27]
requestedLedsNice = {
    "pause-play" : requestedLeds[0],
    "blinking" : requestedLeds[1],
};
currVolume = 50;


isCurrentlyPlaying = False;

def lightLed(ledNumber):
    pass

def stopLed(ledNumber):
    pass

def pause_play():
    if isCurrentlyPlaying:
        pause()
    else:
        play()

def pause():
    #led = leds[1];
    #led.set_value(0);
    mpdClient.connect("localhost",6600);
    mpdClient.pause(1);
    mpdClient.disconnect();


def play():
    #led = leds[1]
    #led.set_value(1);
    mpdClient.connect("localhost",6600);
    mpdClient.pause(0);
    mpdClient.disconnect();

def volumeUp():
    #led = leds[0];
    #led.set_value(1);
    mpdClient.connect("localhost",6600);
    currVolume = min(100, currVolume+5)
    mpdClient.setvol(currVolume);
    mpdClient.disconnect();
    time.sleep(0.3);
    #led.set_value(0);

def volumeDown():
    #led = leds[0];
    #led.set_value(1);
    mpdClient.connect("localhost",6600);
    currVolume = max(0, currVolume-5);
    mpdClient.setvol(currVolume);
    mpdClient.disconnect();
    time.sleep(0.3);
    #led.set_value(0);




def skipSong():
    pass

def buttonLoop():
    pass
    #while True:
        #event_wait only gets lines that had an event
        #eventLines = buttons.event_wait(sec=1);
        #if eventLines:
        #    for line in eventLines:
        #        eventLine = line.event_read();
        #        currOffset = eventLine.source.offset();
#
        #        if (currOffset == requestedButtonsNice["pause-play"]):
        #            pause_play();
        #        elif (currOffset == requestedButtonsNice["volume-up"]):
        #            volumeUp();
        #        elif (currOffset == requestedButtonsNice["volume-down"]):
        #            volumeDown();
        #        elif (currOffset == requestedButtonsNice["skip"]):
        #            skipSong();

if (len(sys.argv) < 2):
    print('Path to music not found')
    exit();

path_to_music = sys.argv[1]

#chip = gpiod.Chip("gpiochip0");
#buttons = chip.get_lines(requestedButtons);
leds = []; 
#for ledNum in requestedLeds:
#    pin = chip.get_lines([ledNum]);
#    pin.request(consumer="consumer", type=gpiod.LINE_REQ_DIR_OUT);
#    leds.append(pin);
#chip.get_lines(requestedLeds);

#buttons.request(consumer="app", type=gpiod.LINE_REQ_EV_FALLING_EDGE);

mpdClient = mpd.MPDClient();
mpdClient.connect("localhost",6600);
mpdClient.add("rickroll.mp3");
mpdClient.play();
mpdClient.disconnect();

#btnThread = Thread(target=buttonLoop);
#btnThread.start();
