from calendar import c
from threading import Thread
from unittest import skip
import time;
import sys;
import gpiod;
import mpd;

requestedButtons = [25,17,10,18]
requestedButtonsNice = {
    "pause-play" : requestedButtons[0],
    "volume-up" : requestedButtons[1],
    "volume-down" : requestedButtons[2],
    "skip" : requestedButtons[3]
};
requestedLeds = [24,27]
requestedLedsNice = {
    "pause-play" : requestedLeds[0],
    "blinking" : requestedLeds[1],
};


def lightLed(ledNumber):
    pass

def stopLed(ledNumber):
    pass

def pause_play():
    mpdClient.connect("localhost",6600);
    mpdState = mpdClient.status()
    mpdState['state']
    if mpdState['state'] == "play":
        print('Pausing')
        led = leds[1];
        led.set_values([0]);
        mpdClient.pause(1);
    else:
        print('Playing')
        led = leds[1]
        led.set_values([1]);
        mpdClient.pause(0);
        mpdClient.play();
    mpdClient.disconnect()


def volumeUp():
    led = leds[0];
    led.set_values([1]);
    mpdClient.connect("localhost",6600);
    mpdClient.volume(5);
    mpdClient.disconnect();
    time.sleep(0.1);
    led.set_values([0]);

def volumeDown():
    led = leds[0];
    led.set_values([1]);
    mpdClient.connect("localhost",6600);
    mpdClient.volume(-5);
    mpdClient.disconnect();
    time.sleep(0.1);
    led.set_values([0]);




def skipSong():
    mpdClient.connect("localhost",6600);
    mpdClient.next();
    mpdClient.disconnect();

def buttonLoop():
    pass
    while True:
        #event_wait only gets lines that had an event
        eventLines = buttons.event_wait(sec=1);
        try:
            if eventLines:
                if mpdClient.
               for line in eventLines:
                   eventLine = line.event_read();
                   currOffset = eventLine.source.offset();

                   if (currOffset == requestedButtonsNice["pause-play"]):
                       pause_play();
                   elif (currOffset == requestedButtonsNice["volume-up"]):
                       volumeUp();
                   elif (currOffset == requestedButtonsNice["volume-down"]):
                       volumeDown();
                   elif (currOffset == requestedButtonsNice["skip"]):
                       skipSong();
        except Exception as e:
            print(e)

if (len(sys.argv) < 2):
    print('Path to music not found')
    exit();

currVolume = 50;

path_to_music = sys.argv[1]

chip = gpiod.Chip("gpiochip0");
buttons = chip.get_lines(requestedButtons);
leds = []; 
for ledNum in requestedLeds:
    pin = chip.get_lines([ledNum]);
    pin.request(consumer="consumer", type=gpiod.LINE_REQ_DIR_OUT);
    leds.append(pin);

buttons.request(consumer="app", type=gpiod.LINE_REQ_EV_FALLING_EDGE);

mpdClient = mpd.MPDClient();
mpdClient.connect("localhost",6600);
mpdClient.update();
#mpdClient.add("rickroll.mp3");
#mpdClient.play();
mpdClient.disconnect();

btnThread = Thread(target=buttonLoop);
btnThread.start();
