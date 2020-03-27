#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

import fluidsynth

if len(sys.argv) < 2:
    sys.exit("Usage: {} <soundfont>".format(sys.argv[0]))

fs = fluidsynth.Synth(samplerate=48000)
fs.start(driver='jack')

sfid = fs.sfload(sys.argv[1])
fs.program_select(0, sfid, 0, 24)

try:
    for i in range(100):
        fs.noteon(0, 60, 30)
        fs.noteon(0, 67, 30)
        fs.noteon(0, 76, 30)

        time.sleep(1.0)

        fs.noteoff(0, 60)
        fs.noteoff(0, 67)
        fs.noteoff(0, 76)

        time.sleep(1.0)
except KeyboardInterrupt:
    fs.all_notes_off(0)
    print('\nAborted.')
finally:
    fs.delete()
