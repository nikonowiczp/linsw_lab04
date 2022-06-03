from threading import Thread
from unittest import skip
import time;
import gpiod;
import mpd;

requestedButtons = [1,2,3,4]
requestedButtonsNice = {
    "pause-play" : requestedButtons[0],
    "volume-up" : requestedButtons[1],
    "volume-down" : requestedButtons[2],
    "skip" : requestedButtons[3]
}
requestedLeds = [1,2]
requestedLedsNice = {
    "pause-play" : requestedLeds[0],
    "blinking" : requestedLeds[1],
}



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
    led = leds.get(requestedLedsNice["pause-play"])
    led.set_value(0);
    mpdClient.connect("localhost",6600);
    mpdClient.pause(1);
    mpdClient.disconnect();


def play():
    led = leds.get(requestedLedsNice["pause-play"])
    led.set_value(1);
    mpdClient.connect("localhost",6600);
    mpdClient.pause(0);
    mpdClient.disconnect();

def volumeUp():
    led = leds.get(requestedLedsNice["blinking"])
    led.set_value(1);
    mpdClient.connect("localhost",6600);
    mpdClient.volume(5);
    mpdClient.disconnect();
    time.sleep(0.3);
    led.set_value(0);
    pass

def volumeDown():
    led = leds.get(requestedLedsNice["blinking"])
    led.set_value(1);
    mpdClient.connect("localhost",6600);
    mpdClient.volume(-5);
    mpdClient.disconnect();
    time.sleep(0.3);
    led.set_value(0);
    pass



def skipSong():
    pass

def buttonLoop():
    while True:
        #event_wait only gets lines that had an event
        eventLines = buttons.event_wait(sec=1);
        if eventLines:
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


chip = gpiod.Chip("gpiochip0");
buttons = chip.get_lines(requestedButtons);
leds = chip.get_lines(requestedLeds);


buttons.request(consumer="app", type=gpiod.LINE_REQ_EV_FALLING_EDGE);
leds.request(consumer="app", type=gpiod.LINE_REQ_DIR_OUT);

mpdClient = mpd.MPDClient();
mpdClient.connect("localhost",6600);
mpdClient.add();
mpdClient.disconnect();

btnThread = Thread(target=buttonLoop);
btnThread.start();
