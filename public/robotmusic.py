from random import choice
from random import randrange

from pyknon.genmidi import Midi
from pyknon.music import Note
from pyknon.music import NoteSeq

SOP_RANGE = range(6, 8)
ALT_RANGE = range(3, 7)
TEN_RANGE = range(2, 6)
BAS_RANGE = range(1, 5)

SONG_DURATION = 16
RANDOM_PITCHLIST = range(12)
SCALE_PITCHLIST = [0, 2, 4, 5, 7, 9, 11]
BLUES_PITCHLIST = [9, 0, 2, 3, 4, 7]

I_PITCHLIST_AT = [0, 4, 7]
I_PITCHLIST_B = [0]
IV_PITCHLIST_AT = [5, 9, 0]
IV_PITCHLIST_B = [5, 9]
V_PITCHLIST_AT = [7, 11, 2, 5]
V_PITCHLIST_B = [7, 11]
VI_PITCHLIST_AT = [9, 0, 4]
VI_PITCHLIST_B = [9, 0]


def random_notes(pitch_list, octave_list, duration, volume):
    result = NoteSeq()
    number_of_notes = int(1 // duration)
    for x in range(0, number_of_notes, 1):
        pitch = choice(pitch_list)
        octave = choice(octave_list)
        dur = duration
        vol = volume
        result.append(Note(pitch, octave, dur, vol))
    return result


def writesong():
    soprano = NoteSeq()
    alto = NoteSeq()
    tenor = NoteSeq()
    bass = NoteSeq()

    for x in range(0, SONG_DURATION, 1):
        if x == SONG_DURATION:
            soprano += random_notes(I_PITCHLIST_AT, SOP_RANGE, 1, 120)
            alto += random_notes(I_PITCHLIST_AT, ALT_RANGE, 1, 90)
            tenor += random_notes(I_PITCHLIST_AT, TEN_RANGE, 1, 90)
            bass += random_notes(I_PITCHLIST_B, BAS_RANGE, 1, 120)
        elif x % 4 == 0:
            soprano += random_notes(RANDOM_PITCHLIST, SOP_RANGE, 0.0625, 120)
            alto += random_notes(I_PITCHLIST_AT, ALT_RANGE, 0.125, 90)
            tenor += random_notes(I_PITCHLIST_AT, TEN_RANGE, 0.25, 90)
            bass += random_notes(I_PITCHLIST_B, BAS_RANGE, 0.5, 90)
        elif x % 4 == 1:
            soprano += random_notes(RANDOM_PITCHLIST, SOP_RANGE, 0.0625, 120)
            alto += random_notes(IV_PITCHLIST_AT, ALT_RANGE, 0.125, 90)
            tenor += random_notes(IV_PITCHLIST_AT, TEN_RANGE, 0.25, 90)
            bass += random_notes(IV_PITCHLIST_B, BAS_RANGE, 0.5, 90)
        elif x % 4 == 2:
            soprano += random_notes(RANDOM_PITCHLIST, SOP_RANGE, 0.0625, 120)
            alto += random_notes(V_PITCHLIST_AT, ALT_RANGE, 0.125, 90)
            tenor += random_notes(V_PITCHLIST_AT, TEN_RANGE, 0.25, 90)
            bass += random_notes(V_PITCHLIST_B, BAS_RANGE, 0.5, 90)
        elif x % 4 == 3:
            soprano += random_notes(RANDOM_PITCHLIST, SOP_RANGE, 0.0625, 120)
            alto += random_notes(VI_PITCHLIST_AT, ALT_RANGE, 0.125, 90)
            tenor += random_notes(VI_PITCHLIST_AT, TEN_RANGE, 0.25, 90)
            bass += random_notes(VI_PITCHLIST_B, BAS_RANGE, 0.5, 90)

    midi = Midi(4, tempo=150)
    midi.seq_notes(soprano, track=0)
    midi.seq_notes(alto, track=1)
    midi.seq_notes(tenor, track=2)
    midi.seq_notes(bass, track=3)

    return midi


writesong().write("art.mid")
