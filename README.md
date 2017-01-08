jasper-light
============

Jasper Light Switch Module

## Installation Steps

1. Install wiring pi with [these](http://wiringpi.com/download-and-install/ "WiringPi") instructions
2. Place Light.py in your `jasper_directory/client/modules/` folder
3. Place jlight-helper.sh in `~/bin`
4. Make jlight-helper.sh executable by running `chmod +x ~/bin/jlight-helper.sh`
5. Restart Jasper

## Usage
```
YOU: light (or "right")
JASPER: Okay < toggles pin 0 >
```
[![Jasper Light](http://img.youtube.com/vi/o2Y-x8iqYQQ/0.jpg)](http://www.youtube.com/watch?v=o2Y-x8iqYQQ)

## Problems
- when using PocketSphinx, Jasper will not recognize the word "light" under any circumstances. Instead, it will log the word as "right".

## TODO
- Not use helper.sh
