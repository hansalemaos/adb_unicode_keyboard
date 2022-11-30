import base64
import os
import subprocess
import tempfile
from functools import partial
from random import uniform
from time import sleep
import psutil
import regex
import requests
import keyboard as keyboard__
from flexible_partial import FlexiblePartial

keyeventdict = {
    1: {
        "key_name": "KEYCODE_SOFT_LEFT",
        "key_longpress": "input keyevent --longpress 1",
        "key_press": "input keyevent 1",
    },
    2: {
        "key_name": "KEYCODE_SOFT_RIGHT",
        "key_longpress": "input keyevent --longpress 2",
        "key_press": "input keyevent 2",
    },
    3: {
        "key_name": "KEYCODE_HOME",
        "key_longpress": "input keyevent --longpress 3",
        "key_press": "input keyevent 3",
    },
    4: {
        "key_name": "KEYCODE_BACK",
        "key_longpress": "input keyevent --longpress 4",
        "key_press": "input keyevent 4",
    },
    5: {
        "key_name": "KEYCODE_CALL",
        "key_longpress": "input keyevent --longpress 5",
        "key_press": "input keyevent 5",
    },
    6: {
        "key_name": "KEYCODE_ENDCALL",
        "key_longpress": "input keyevent --longpress 6",
        "key_press": "input keyevent 6",
    },
    7: {
        "key_name": "KEYCODE_0",
        "key_longpress": "input keyevent --longpress 7",
        "key_press": "input keyevent 7",
    },
    8: {
        "key_name": "KEYCODE_1",
        "key_longpress": "input keyevent --longpress 8",
        "key_press": "input keyevent 8",
    },
    9: {
        "key_name": "KEYCODE_2",
        "key_longpress": "input keyevent --longpress 9",
        "key_press": "input keyevent 9",
    },
    10: {
        "key_name": "KEYCODE_3",
        "key_longpress": "input keyevent --longpress 10",
        "key_press": "input keyevent 10",
    },
    11: {
        "key_name": "KEYCODE_4",
        "key_longpress": "input keyevent --longpress 11",
        "key_press": "input keyevent 11",
    },
    12: {
        "key_name": "KEYCODE_5",
        "key_longpress": "input keyevent --longpress 12",
        "key_press": "input keyevent 12",
    },
    13: {
        "key_name": "KEYCODE_6",
        "key_longpress": "input keyevent --longpress 13",
        "key_press": "input keyevent 13",
    },
    14: {
        "key_name": "KEYCODE_7",
        "key_longpress": "input keyevent --longpress 14",
        "key_press": "input keyevent 14",
    },
    15: {
        "key_name": "KEYCODE_8",
        "key_longpress": "input keyevent --longpress 15",
        "key_press": "input keyevent 15",
    },
    16: {
        "key_name": "KEYCODE_9",
        "key_longpress": "input keyevent --longpress 16",
        "key_press": "input keyevent 16",
    },
    17: {
        "key_name": "KEYCODE_STAR",
        "key_longpress": "input keyevent --longpress 17",
        "key_press": "input keyevent 17",
    },
    18: {
        "key_name": "KEYCODE_POUND",
        "key_longpress": "input keyevent --longpress 18",
        "key_press": "input keyevent 18",
    },
    19: {
        "key_name": "KEYCODE_DPAD_UP",
        "key_longpress": "input keyevent --longpress 19",
        "key_press": "input keyevent 19",
    },
    20: {
        "key_name": "KEYCODE_DPAD_DOWN",
        "key_longpress": "input keyevent --longpress 20",
        "key_press": "input keyevent 20",
    },
    21: {
        "key_name": "KEYCODE_DPAD_LEFT",
        "key_longpress": "input keyevent --longpress 21",
        "key_press": "input keyevent 21",
    },
    22: {
        "key_name": "KEYCODE_DPAD_RIGHT",
        "key_longpress": "input keyevent --longpress 22",
        "key_press": "input keyevent 22",
    },
    23: {
        "key_name": "KEYCODE_DPAD_CENTER",
        "key_longpress": "input keyevent --longpress 23",
        "key_press": "input keyevent 23",
    },
    24: {
        "key_name": "KEYCODE_VOLUME_UP",
        "key_longpress": "input keyevent --longpress 24",
        "key_press": "input keyevent 24",
    },
    25: {
        "key_name": "KEYCODE_VOLUME_DOWN",
        "key_longpress": "input keyevent --longpress 25",
        "key_press": "input keyevent 25",
    },
    26: {
        "key_name": "KEYCODE_POWER",
        "key_longpress": "input keyevent --longpress 26",
        "key_press": "input keyevent 26",
    },
    27: {
        "key_name": "KEYCODE_CAMERA",
        "key_longpress": "input keyevent --longpress 27",
        "key_press": "input keyevent 27",
    },
    28: {
        "key_name": "KEYCODE_CLEAR",
        "key_longpress": "input keyevent --longpress 28",
        "key_press": "input keyevent 28",
    },
    29: {
        "key_name": "KEYCODE_A",
        "key_longpress": "input keyevent --longpress 29",
        "key_press": "input keyevent 29",
    },
    30: {
        "key_name": "KEYCODE_B",
        "key_longpress": "input keyevent --longpress 30",
        "key_press": "input keyevent 30",
    },
    31: {
        "key_name": "KEYCODE_C",
        "key_longpress": "input keyevent --longpress 31",
        "key_press": "input keyevent 31",
    },
    32: {
        "key_name": "KEYCODE_D",
        "key_longpress": "input keyevent --longpress 32",
        "key_press": "input keyevent 32",
    },
    33: {
        "key_name": "KEYCODE_E",
        "key_longpress": "input keyevent --longpress 33",
        "key_press": "input keyevent 33",
    },
    34: {
        "key_name": "KEYCODE_F",
        "key_longpress": "input keyevent --longpress 34",
        "key_press": "input keyevent 34",
    },
    35: {
        "key_name": "KEYCODE_G",
        "key_longpress": "input keyevent --longpress 35",
        "key_press": "input keyevent 35",
    },
    36: {
        "key_name": "KEYCODE_H",
        "key_longpress": "input keyevent --longpress 36",
        "key_press": "input keyevent 36",
    },
    37: {
        "key_name": "KEYCODE_I",
        "key_longpress": "input keyevent --longpress 37",
        "key_press": "input keyevent 37",
    },
    38: {
        "key_name": "KEYCODE_J",
        "key_longpress": "input keyevent --longpress 38",
        "key_press": "input keyevent 38",
    },
    39: {
        "key_name": "KEYCODE_K",
        "key_longpress": "input keyevent --longpress 39",
        "key_press": "input keyevent 39",
    },
    40: {
        "key_name": "KEYCODE_L",
        "key_longpress": "input keyevent --longpress 40",
        "key_press": "input keyevent 40",
    },
    41: {
        "key_name": "KEYCODE_M",
        "key_longpress": "input keyevent --longpress 41",
        "key_press": "input keyevent 41",
    },
    42: {
        "key_name": "KEYCODE_N",
        "key_longpress": "input keyevent --longpress 42",
        "key_press": "input keyevent 42",
    },
    43: {
        "key_name": "KEYCODE_O",
        "key_longpress": "input keyevent --longpress 43",
        "key_press": "input keyevent 43",
    },
    44: {
        "key_name": "KEYCODE_P",
        "key_longpress": "input keyevent --longpress 44",
        "key_press": "input keyevent 44",
    },
    45: {
        "key_name": "KEYCODE_Q",
        "key_longpress": "input keyevent --longpress 45",
        "key_press": "input keyevent 45",
    },
    46: {
        "key_name": "KEYCODE_R",
        "key_longpress": "input keyevent --longpress 46",
        "key_press": "input keyevent 46",
    },
    47: {
        "key_name": "KEYCODE_S",
        "key_longpress": "input keyevent --longpress 47",
        "key_press": "input keyevent 47",
    },
    48: {
        "key_name": "KEYCODE_T",
        "key_longpress": "input keyevent --longpress 48",
        "key_press": "input keyevent 48",
    },
    49: {
        "key_name": "KEYCODE_U",
        "key_longpress": "input keyevent --longpress 49",
        "key_press": "input keyevent 49",
    },
    50: {
        "key_name": "KEYCODE_V",
        "key_longpress": "input keyevent --longpress 50",
        "key_press": "input keyevent 50",
    },
    51: {
        "key_name": "KEYCODE_W",
        "key_longpress": "input keyevent --longpress 51",
        "key_press": "input keyevent 51",
    },
    52: {
        "key_name": "KEYCODE_X",
        "key_longpress": "input keyevent --longpress 52",
        "key_press": "input keyevent 52",
    },
    53: {
        "key_name": "KEYCODE_Y",
        "key_longpress": "input keyevent --longpress 53",
        "key_press": "input keyevent 53",
    },
    54: {
        "key_name": "KEYCODE_Z",
        "key_longpress": "input keyevent --longpress 54",
        "key_press": "input keyevent 54",
    },
    55: {
        "key_name": "KEYCODE_COMMA",
        "key_longpress": "input keyevent --longpress 55",
        "key_press": "input keyevent 55",
    },
    56: {
        "key_name": "KEYCODE_PERIOD",
        "key_longpress": "input keyevent --longpress 56",
        "key_press": "input keyevent 56",
    },
    57: {
        "key_name": "KEYCODE_ALT_LEFT",
        "key_longpress": "input keyevent --longpress 57",
        "key_press": "input keyevent 57",
    },
    58: {
        "key_name": "KEYCODE_ALT_RIGHT",
        "key_longpress": "input keyevent --longpress 58",
        "key_press": "input keyevent 58",
    },
    59: {
        "key_name": "KEYCODE_SHIFT_LEFT",
        "key_longpress": "input keyevent --longpress 59",
        "key_press": "input keyevent 59",
    },
    60: {
        "key_name": "KEYCODE_SHIFT_RIGHT",
        "key_longpress": "input keyevent --longpress 60",
        "key_press": "input keyevent 60",
    },
    61: {
        "key_name": "KEYCODE_TAB",
        "key_longpress": "input keyevent --longpress 61",
        "key_press": "input keyevent 61",
    },
    62: {
        "key_name": "KEYCODE_SPACE",
        "key_longpress": "input keyevent --longpress 62",
        "key_press": "input keyevent 62",
    },
    63: {
        "key_name": "KEYCODE_SYM",
        "key_longpress": "input keyevent --longpress 63",
        "key_press": "input keyevent 63",
    },
    64: {
        "key_name": "KEYCODE_EXPLORER",
        "key_longpress": "input keyevent --longpress 64",
        "key_press": "input keyevent 64",
    },
    65: {
        "key_name": "KEYCODE_ENVELOPE",
        "key_longpress": "input keyevent --longpress 65",
        "key_press": "input keyevent 65",
    },
    66: {
        "key_name": "KEYCODE_ENTER",
        "key_longpress": "input keyevent --longpress 66",
        "key_press": "input keyevent 66",
    },
    67: {
        "key_name": "KEYCODE_DEL",
        "key_longpress": "input keyevent --longpress 67",
        "key_press": "input keyevent 67",
    },
    68: {
        "key_name": "KEYCODE_GRAVE",
        "key_longpress": "input keyevent --longpress 68",
        "key_press": "input keyevent 68",
    },
    69: {
        "key_name": "KEYCODE_MINUS",
        "key_longpress": "input keyevent --longpress 69",
        "key_press": "input keyevent 69",
    },
    70: {
        "key_name": "KEYCODE_EQUALS",
        "key_longpress": "input keyevent --longpress 70",
        "key_press": "input keyevent 70",
    },
    71: {
        "key_name": "KEYCODE_LEFT_BRACKET",
        "key_longpress": "input keyevent --longpress 71",
        "key_press": "input keyevent 71",
    },
    72: {
        "key_name": "KEYCODE_RIGHT_BRACKET",
        "key_longpress": "input keyevent --longpress 72",
        "key_press": "input keyevent 72",
    },
    73: {
        "key_name": "KEYCODE_BACKSLASH",
        "key_longpress": "input keyevent --longpress 73",
        "key_press": "input keyevent 73",
    },
    74: {
        "key_name": "KEYCODE_SEMICOLON",
        "key_longpress": "input keyevent --longpress 74",
        "key_press": "input keyevent 74",
    },
    75: {
        "key_name": "KEYCODE_APOSTROPHE",
        "key_longpress": "input keyevent --longpress 75",
        "key_press": "input keyevent 75",
    },
    76: {
        "key_name": "KEYCODE_SLASH",
        "key_longpress": "input keyevent --longpress 76",
        "key_press": "input keyevent 76",
    },
    77: {
        "key_name": "KEYCODE_AT",
        "key_longpress": "input keyevent --longpress 77",
        "key_press": "input keyevent 77",
    },
    78: {
        "key_name": "KEYCODE_NUM",
        "key_longpress": "input keyevent --longpress 78",
        "key_press": "input keyevent 78",
    },
    79: {
        "key_name": "KEYCODE_HEADSETHOOK",
        "key_longpress": "input keyevent --longpress 79",
        "key_press": "input keyevent 79",
    },
    80: {
        "key_name": "KEYCODE_FOCUS",
        "key_longpress": "input keyevent --longpress 80",
        "key_press": "input keyevent 80",
    },
    81: {
        "key_name": "KEYCODE_PLUS",
        "key_longpress": "input keyevent --longpress 81",
        "key_press": "input keyevent 81",
    },
    82: {
        "key_name": "KEYCODE_MENU",
        "key_longpress": "input keyevent --longpress 82",
        "key_press": "input keyevent 82",
    },
    83: {
        "key_name": "KEYCODE_NOTIFICATION",
        "key_longpress": "input keyevent --longpress 83",
        "key_press": "input keyevent 83",
    },
    84: {
        "key_name": "KEYCODE_SEARCH",
        "key_longpress": "input keyevent --longpress 84",
        "key_press": "input keyevent 84",
    },
    85: {
        "key_name": "KEYCODE_MEDIA_PLAY_PAUSE",
        "key_longpress": "input keyevent --longpress 85",
        "key_press": "input keyevent 85",
    },
    86: {
        "key_name": "KEYCODE_MEDIA_STOP",
        "key_longpress": "input keyevent --longpress 86",
        "key_press": "input keyevent 86",
    },
    87: {
        "key_name": "KEYCODE_MEDIA_NEXT",
        "key_longpress": "input keyevent --longpress 87",
        "key_press": "input keyevent 87",
    },
    88: {
        "key_name": "KEYCODE_MEDIA_PREVIOUS",
        "key_longpress": "input keyevent --longpress 88",
        "key_press": "input keyevent 88",
    },
    89: {
        "key_name": "KEYCODE_MEDIA_REWIND",
        "key_longpress": "input keyevent --longpress 89",
        "key_press": "input keyevent 89",
    },
    90: {
        "key_name": "KEYCODE_MEDIA_FAST_FORWARD",
        "key_longpress": "input keyevent --longpress 90",
        "key_press": "input keyevent 90",
    },
    91: {
        "key_name": "KEYCODE_MUTE",
        "key_longpress": "input keyevent --longpress 91",
        "key_press": "input keyevent 91",
    },
    92: {
        "key_name": "KEYCODE_PAGE_UP",
        "key_longpress": "input keyevent --longpress 92",
        "key_press": "input keyevent 92",
    },
    93: {
        "key_name": "KEYCODE_PAGE_DOWN",
        "key_longpress": "input keyevent --longpress 93",
        "key_press": "input keyevent 93",
    },
    94: {
        "key_name": "KEYCODE_PICTSYMBOLS",
        "key_longpress": "input keyevent --longpress 94",
        "key_press": "input keyevent 94",
    },
    95: {
        "key_name": "KEYCODE_SWITCH_CHARSET",
        "key_longpress": "input keyevent --longpress 95",
        "key_press": "input keyevent 95",
    },
    96: {
        "key_name": "KEYCODE_BUTTON_A",
        "key_longpress": "input keyevent --longpress 96",
        "key_press": "input keyevent 96",
    },
    97: {
        "key_name": "KEYCODE_BUTTON_B",
        "key_longpress": "input keyevent --longpress 97",
        "key_press": "input keyevent 97",
    },
    98: {
        "key_name": "KEYCODE_BUTTON_C",
        "key_longpress": "input keyevent --longpress 98",
        "key_press": "input keyevent 98",
    },
    99: {
        "key_name": "KEYCODE_BUTTON_X",
        "key_longpress": "input keyevent --longpress 99",
        "key_press": "input keyevent 99",
    },
    100: {
        "key_name": "KEYCODE_BUTTON_Y",
        "key_longpress": "input keyevent --longpress 100",
        "key_press": "input keyevent 100",
    },
    101: {
        "key_name": "KEYCODE_BUTTON_Z",
        "key_longpress": "input keyevent --longpress 101",
        "key_press": "input keyevent 101",
    },
    102: {
        "key_name": "KEYCODE_BUTTON_L1",
        "key_longpress": "input keyevent --longpress 102",
        "key_press": "input keyevent 102",
    },
    103: {
        "key_name": "KEYCODE_BUTTON_R1",
        "key_longpress": "input keyevent --longpress 103",
        "key_press": "input keyevent 103",
    },
    104: {
        "key_name": "KEYCODE_BUTTON_L2",
        "key_longpress": "input keyevent --longpress 104",
        "key_press": "input keyevent 104",
    },
    105: {
        "key_name": "KEYCODE_BUTTON_R2",
        "key_longpress": "input keyevent --longpress 105",
        "key_press": "input keyevent 105",
    },
    106: {
        "key_name": "KEYCODE_BUTTON_THUMBL",
        "key_longpress": "input keyevent --longpress 106",
        "key_press": "input keyevent 106",
    },
    107: {
        "key_name": "KEYCODE_BUTTON_THUMBR",
        "key_longpress": "input keyevent --longpress 107",
        "key_press": "input keyevent 107",
    },
    108: {
        "key_name": "KEYCODE_BUTTON_START",
        "key_longpress": "input keyevent --longpress 108",
        "key_press": "input keyevent 108",
    },
    109: {
        "key_name": "KEYCODE_BUTTON_SELECT",
        "key_longpress": "input keyevent --longpress 109",
        "key_press": "input keyevent 109",
    },
    110: {
        "key_name": "KEYCODE_BUTTON_MODE",
        "key_longpress": "input keyevent --longpress 110",
        "key_press": "input keyevent 110",
    },
    111: {
        "key_name": "KEYCODE_ESCAPE",
        "key_longpress": "input keyevent --longpress 111",
        "key_press": "input keyevent 111",
    },
    112: {
        "key_name": "KEYCODE_FORWARD_DEL",
        "key_longpress": "input keyevent --longpress 112",
        "key_press": "input keyevent 112",
    },
    113: {
        "key_name": "KEYCODE_CTRL_LEFT",
        "key_longpress": "input keyevent --longpress 113",
        "key_press": "input keyevent 113",
    },
    114: {
        "key_name": "KEYCODE_CTRL_RIGHT",
        "key_longpress": "input keyevent --longpress 114",
        "key_press": "input keyevent 114",
    },
    115: {
        "key_name": "KEYCODE_CAPS_LOCK",
        "key_longpress": "input keyevent --longpress 115",
        "key_press": "input keyevent 115",
    },
    116: {
        "key_name": "KEYCODE_SCROLL_LOCK",
        "key_longpress": "input keyevent --longpress 116",
        "key_press": "input keyevent 116",
    },
    117: {
        "key_name": "KEYCODE_META_LEFT",
        "key_longpress": "input keyevent --longpress 117",
        "key_press": "input keyevent 117",
    },
    118: {
        "key_name": "KEYCODE_META_RIGHT",
        "key_longpress": "input keyevent --longpress 118",
        "key_press": "input keyevent 118",
    },
    119: {
        "key_name": "KEYCODE_FUNCTION",
        "key_longpress": "input keyevent --longpress 119",
        "key_press": "input keyevent 119",
    },
    120: {
        "key_name": "KEYCODE_SYSRQ",
        "key_longpress": "input keyevent --longpress 120",
        "key_press": "input keyevent 120",
    },
    121: {
        "key_name": "KEYCODE_BREAK",
        "key_longpress": "input keyevent --longpress 121",
        "key_press": "input keyevent 121",
    },
    122: {
        "key_name": "KEYCODE_MOVE_HOME",
        "key_longpress": "input keyevent --longpress 122",
        "key_press": "input keyevent 122",
    },
    123: {
        "key_name": "KEYCODE_MOVE_END",
        "key_longpress": "input keyevent --longpress 123",
        "key_press": "input keyevent 123",
    },
    124: {
        "key_name": "KEYCODE_INSERT",
        "key_longpress": "input keyevent --longpress 124",
        "key_press": "input keyevent 124",
    },
    125: {
        "key_name": "KEYCODE_FORWARD",
        "key_longpress": "input keyevent --longpress 125",
        "key_press": "input keyevent 125",
    },
    126: {
        "key_name": "KEYCODE_MEDIA_PLAY",
        "key_longpress": "input keyevent --longpress 126",
        "key_press": "input keyevent 126",
    },
    127: {
        "key_name": "KEYCODE_MEDIA_PAUSE",
        "key_longpress": "input keyevent --longpress 127",
        "key_press": "input keyevent 127",
    },
    128: {
        "key_name": "KEYCODE_MEDIA_CLOSE",
        "key_longpress": "input keyevent --longpress 128",
        "key_press": "input keyevent 128",
    },
    129: {
        "key_name": "KEYCODE_MEDIA_EJECT",
        "key_longpress": "input keyevent --longpress 129",
        "key_press": "input keyevent 129",
    },
    130: {
        "key_name": "KEYCODE_MEDIA_RECORD",
        "key_longpress": "input keyevent --longpress 130",
        "key_press": "input keyevent 130",
    },
    131: {
        "key_name": "KEYCODE_F1",
        "key_longpress": "input keyevent --longpress 131",
        "key_press": "input keyevent 131",
    },
    132: {
        "key_name": "KEYCODE_F2",
        "key_longpress": "input keyevent --longpress 132",
        "key_press": "input keyevent 132",
    },
    133: {
        "key_name": "KEYCODE_F3",
        "key_longpress": "input keyevent --longpress 133",
        "key_press": "input keyevent 133",
    },
    134: {
        "key_name": "KEYCODE_F4",
        "key_longpress": "input keyevent --longpress 134",
        "key_press": "input keyevent 134",
    },
    135: {
        "key_name": "KEYCODE_F5",
        "key_longpress": "input keyevent --longpress 135",
        "key_press": "input keyevent 135",
    },
    136: {
        "key_name": "KEYCODE_F6",
        "key_longpress": "input keyevent --longpress 136",
        "key_press": "input keyevent 136",
    },
    137: {
        "key_name": "KEYCODE_F7",
        "key_longpress": "input keyevent --longpress 137",
        "key_press": "input keyevent 137",
    },
    138: {
        "key_name": "KEYCODE_F8",
        "key_longpress": "input keyevent --longpress 138",
        "key_press": "input keyevent 138",
    },
    139: {
        "key_name": "KEYCODE_F9",
        "key_longpress": "input keyevent --longpress 139",
        "key_press": "input keyevent 139",
    },
    140: {
        "key_name": "KEYCODE_F10",
        "key_longpress": "input keyevent --longpress 140",
        "key_press": "input keyevent 140",
    },
    141: {
        "key_name": "KEYCODE_F11",
        "key_longpress": "input keyevent --longpress 141",
        "key_press": "input keyevent 141",
    },
    142: {
        "key_name": "KEYCODE_F12",
        "key_longpress": "input keyevent --longpress 142",
        "key_press": "input keyevent 142",
    },
    143: {
        "key_name": "KEYCODE_NUM_LOCK",
        "key_longpress": "input keyevent --longpress 143",
        "key_press": "input keyevent 143",
    },
    144: {
        "key_name": "KEYCODE_NUMPAD_0",
        "key_longpress": "input keyevent --longpress 144",
        "key_press": "input keyevent 144",
    },
    145: {
        "key_name": "KEYCODE_NUMPAD_1",
        "key_longpress": "input keyevent --longpress 145",
        "key_press": "input keyevent 145",
    },
    146: {
        "key_name": "KEYCODE_NUMPAD_2",
        "key_longpress": "input keyevent --longpress 146",
        "key_press": "input keyevent 146",
    },
    147: {
        "key_name": "KEYCODE_NUMPAD_3",
        "key_longpress": "input keyevent --longpress 147",
        "key_press": "input keyevent 147",
    },
    148: {
        "key_name": "KEYCODE_NUMPAD_4",
        "key_longpress": "input keyevent --longpress 148",
        "key_press": "input keyevent 148",
    },
    149: {
        "key_name": "KEYCODE_NUMPAD_5",
        "key_longpress": "input keyevent --longpress 149",
        "key_press": "input keyevent 149",
    },
    150: {
        "key_name": "KEYCODE_NUMPAD_6",
        "key_longpress": "input keyevent --longpress 150",
        "key_press": "input keyevent 150",
    },
    151: {
        "key_name": "KEYCODE_NUMPAD_7",
        "key_longpress": "input keyevent --longpress 151",
        "key_press": "input keyevent 151",
    },
    152: {
        "key_name": "KEYCODE_NUMPAD_8",
        "key_longpress": "input keyevent --longpress 152",
        "key_press": "input keyevent 152",
    },
    153: {
        "key_name": "KEYCODE_NUMPAD_9",
        "key_longpress": "input keyevent --longpress 153",
        "key_press": "input keyevent 153",
    },
    154: {
        "key_name": "KEYCODE_NUMPAD_DIVIDE",
        "key_longpress": "input keyevent --longpress 154",
        "key_press": "input keyevent 154",
    },
    155: {
        "key_name": "KEYCODE_NUMPAD_MULTIPLY",
        "key_longpress": "input keyevent --longpress 155",
        "key_press": "input keyevent 155",
    },
    156: {
        "key_name": "KEYCODE_NUMPAD_SUBTRACT",
        "key_longpress": "input keyevent --longpress 156",
        "key_press": "input keyevent 156",
    },
    157: {
        "key_name": "KEYCODE_NUMPAD_ADD",
        "key_longpress": "input keyevent --longpress 157",
        "key_press": "input keyevent 157",
    },
    158: {
        "key_name": "KEYCODE_NUMPAD_DOT",
        "key_longpress": "input keyevent --longpress 158",
        "key_press": "input keyevent 158",
    },
    159: {
        "key_name": "KEYCODE_NUMPAD_COMMA",
        "key_longpress": "input keyevent --longpress 159",
        "key_press": "input keyevent 159",
    },
    160: {
        "key_name": "KEYCODE_NUMPAD_ENTER",
        "key_longpress": "input keyevent --longpress 160",
        "key_press": "input keyevent 160",
    },
    161: {
        "key_name": "KEYCODE_NUMPAD_EQUALS",
        "key_longpress": "input keyevent --longpress 161",
        "key_press": "input keyevent 161",
    },
    162: {
        "key_name": "KEYCODE_NUMPAD_LEFT_PAREN",
        "key_longpress": "input keyevent --longpress 162",
        "key_press": "input keyevent 162",
    },
    163: {
        "key_name": "KEYCODE_NUMPAD_RIGHT_PAREN",
        "key_longpress": "input keyevent --longpress 163",
        "key_press": "input keyevent 163",
    },
    164: {
        "key_name": "KEYCODE_VOLUME_MUTE",
        "key_longpress": "input keyevent --longpress 164",
        "key_press": "input keyevent 164",
    },
    165: {
        "key_name": "KEYCODE_INFO",
        "key_longpress": "input keyevent --longpress 165",
        "key_press": "input keyevent 165",
    },
    166: {
        "key_name": "KEYCODE_CHANNEL_UP",
        "key_longpress": "input keyevent --longpress 166",
        "key_press": "input keyevent 166",
    },
    167: {
        "key_name": "KEYCODE_CHANNEL_DOWN",
        "key_longpress": "input keyevent --longpress 167",
        "key_press": "input keyevent 167",
    },
    168: {
        "key_name": "KEYCODE_ZOOM_IN",
        "key_longpress": "input keyevent --longpress 168",
        "key_press": "input keyevent 168",
    },
    169: {
        "key_name": "KEYCODE_ZOOM_OUT",
        "key_longpress": "input keyevent --longpress 169",
        "key_press": "input keyevent 169",
    },
    170: {
        "key_name": "KEYCODE_TV",
        "key_longpress": "input keyevent --longpress 170",
        "key_press": "input keyevent 170",
    },
    171: {
        "key_name": "KEYCODE_WINDOW",
        "key_longpress": "input keyevent --longpress 171",
        "key_press": "input keyevent 171",
    },
    172: {
        "key_name": "KEYCODE_GUIDE",
        "key_longpress": "input keyevent --longpress 172",
        "key_press": "input keyevent 172",
    },
    173: {
        "key_name": "KEYCODE_DVR",
        "key_longpress": "input keyevent --longpress 173",
        "key_press": "input keyevent 173",
    },
    174: {
        "key_name": "KEYCODE_BOOKMARK",
        "key_longpress": "input keyevent --longpress 174",
        "key_press": "input keyevent 174",
    },
    175: {
        "key_name": "KEYCODE_CAPTIONS",
        "key_longpress": "input keyevent --longpress 175",
        "key_press": "input keyevent 175",
    },
    176: {
        "key_name": "KEYCODE_SETTINGS",
        "key_longpress": "input keyevent --longpress 176",
        "key_press": "input keyevent 176",
    },
    177: {
        "key_name": "KEYCODE_TV_POWER",
        "key_longpress": "input keyevent --longpress 177",
        "key_press": "input keyevent 177",
    },
    178: {
        "key_name": "KEYCODE_TV_INPUT",
        "key_longpress": "input keyevent --longpress 178",
        "key_press": "input keyevent 178",
    },
    179: {
        "key_name": "KEYCODE_STB_POWER",
        "key_longpress": "input keyevent --longpress 179",
        "key_press": "input keyevent 179",
    },
    180: {
        "key_name": "KEYCODE_STB_INPUT",
        "key_longpress": "input keyevent --longpress 180",
        "key_press": "input keyevent 180",
    },
    181: {
        "key_name": "KEYCODE_AVR_POWER",
        "key_longpress": "input keyevent --longpress 181",
        "key_press": "input keyevent 181",
    },
    182: {
        "key_name": "KEYCODE_AVR_INPUT",
        "key_longpress": "input keyevent --longpress 182",
        "key_press": "input keyevent 182",
    },
    183: {
        "key_name": "KEYCODE_PROG_RED",
        "key_longpress": "input keyevent --longpress 183",
        "key_press": "input keyevent 183",
    },
    184: {
        "key_name": "KEYCODE_PROG_GREEN",
        "key_longpress": "input keyevent --longpress 184",
        "key_press": "input keyevent 184",
    },
    185: {
        "key_name": "KEYCODE_PROG_YELLOW",
        "key_longpress": "input keyevent --longpress 185",
        "key_press": "input keyevent 185",
    },
    186: {
        "key_name": "KEYCODE_PROG_BLUE",
        "key_longpress": "input keyevent --longpress 186",
        "key_press": "input keyevent 186",
    },
    187: {
        "key_name": "KEYCODE_APP_SWITCH",
        "key_longpress": "input keyevent --longpress 187",
        "key_press": "input keyevent 187",
    },
    188: {
        "key_name": "KEYCODE_BUTTON_1",
        "key_longpress": "input keyevent --longpress 188",
        "key_press": "input keyevent 188",
    },
    189: {
        "key_name": "KEYCODE_BUTTON_2",
        "key_longpress": "input keyevent --longpress 189",
        "key_press": "input keyevent 189",
    },
    190: {
        "key_name": "KEYCODE_BUTTON_3",
        "key_longpress": "input keyevent --longpress 190",
        "key_press": "input keyevent 190",
    },
    191: {
        "key_name": "KEYCODE_BUTTON_4",
        "key_longpress": "input keyevent --longpress 191",
        "key_press": "input keyevent 191",
    },
    192: {
        "key_name": "KEYCODE_BUTTON_5",
        "key_longpress": "input keyevent --longpress 192",
        "key_press": "input keyevent 192",
    },
    193: {
        "key_name": "KEYCODE_BUTTON_6",
        "key_longpress": "input keyevent --longpress 193",
        "key_press": "input keyevent 193",
    },
    194: {
        "key_name": "KEYCODE_BUTTON_7",
        "key_longpress": "input keyevent --longpress 194",
        "key_press": "input keyevent 194",
    },
    195: {
        "key_name": "KEYCODE_BUTTON_8",
        "key_longpress": "input keyevent --longpress 195",
        "key_press": "input keyevent 195",
    },
    196: {
        "key_name": "KEYCODE_BUTTON_9",
        "key_longpress": "input keyevent --longpress 196",
        "key_press": "input keyevent 196",
    },
    197: {
        "key_name": "KEYCODE_BUTTON_10",
        "key_longpress": "input keyevent --longpress 197",
        "key_press": "input keyevent 197",
    },
    198: {
        "key_name": "KEYCODE_BUTTON_11",
        "key_longpress": "input keyevent --longpress 198",
        "key_press": "input keyevent 198",
    },
    199: {
        "key_name": "KEYCODE_BUTTON_12",
        "key_longpress": "input keyevent --longpress 199",
        "key_press": "input keyevent 199",
    },
    200: {
        "key_name": "KEYCODE_BUTTON_13",
        "key_longpress": "input keyevent --longpress 200",
        "key_press": "input keyevent 200",
    },
    201: {
        "key_name": "KEYCODE_BUTTON_14",
        "key_longpress": "input keyevent --longpress 201",
        "key_press": "input keyevent 201",
    },
    202: {
        "key_name": "KEYCODE_BUTTON_15",
        "key_longpress": "input keyevent --longpress 202",
        "key_press": "input keyevent 202",
    },
    203: {
        "key_name": "KEYCODE_BUTTON_16",
        "key_longpress": "input keyevent --longpress 203",
        "key_press": "input keyevent 203",
    },
    204: {
        "key_name": "KEYCODE_LANGUAGE_SWITCH",
        "key_longpress": "input keyevent --longpress 204",
        "key_press": "input keyevent 204",
    },
    205: {
        "key_name": "KEYCODE_MANNER_MODE",
        "key_longpress": "input keyevent --longpress 205",
        "key_press": "input keyevent 205",
    },
    206: {
        "key_name": "KEYCODE_3D_MODE",
        "key_longpress": "input keyevent --longpress 206",
        "key_press": "input keyevent 206",
    },
    207: {
        "key_name": "KEYCODE_CONTACTS",
        "key_longpress": "input keyevent --longpress 207",
        "key_press": "input keyevent 207",
    },
    208: {
        "key_name": "KEYCODE_CALENDAR",
        "key_longpress": "input keyevent --longpress 208",
        "key_press": "input keyevent 208",
    },
    209: {
        "key_name": "KEYCODE_MUSIC",
        "key_longpress": "input keyevent --longpress 209",
        "key_press": "input keyevent 209",
    },
    210: {
        "key_name": "KEYCODE_CALCULATOR",
        "key_longpress": "input keyevent --longpress 210",
        "key_press": "input keyevent 210",
    },
    211: {
        "key_name": "KEYCODE_ZENKAKU_HANKAKU",
        "key_longpress": "input keyevent --longpress 211",
        "key_press": "input keyevent 211",
    },
    212: {
        "key_name": "KEYCODE_EISU",
        "key_longpress": "input keyevent --longpress 212",
        "key_press": "input keyevent 212",
    },
    213: {
        "key_name": "KEYCODE_MUHENKAN",
        "key_longpress": "input keyevent --longpress 213",
        "key_press": "input keyevent 213",
    },
    214: {
        "key_name": "KEYCODE_HENKAN",
        "key_longpress": "input keyevent --longpress 214",
        "key_press": "input keyevent 214",
    },
    215: {
        "key_name": "KEYCODE_KATAKANA_HIRAGANA",
        "key_longpress": "input keyevent --longpress 215",
        "key_press": "input keyevent 215",
    },
    216: {
        "key_name": "KEYCODE_YEN",
        "key_longpress": "input keyevent --longpress 216",
        "key_press": "input keyevent 216",
    },
    217: {
        "key_name": "KEYCODE_RO",
        "key_longpress": "input keyevent --longpress 217",
        "key_press": "input keyevent 217",
    },
    218: {
        "key_name": "KEYCODE_KANA",
        "key_longpress": "input keyevent --longpress 218",
        "key_press": "input keyevent 218",
    },
    219: {
        "key_name": "KEYCODE_ASSIST",
        "key_longpress": "input keyevent --longpress 219",
        "key_press": "input keyevent 219",
    },
    220: {
        "key_name": "KEYCODE_BRIGHTNESS_DOWN",
        "key_longpress": "input keyevent --longpress 220",
        "key_press": "input keyevent 220",
    },
    221: {
        "key_name": "KEYCODE_BRIGHTNESS_UP",
        "key_longpress": "input keyevent --longpress 221",
        "key_press": "input keyevent 221",
    },
    222: {
        "key_name": "KEYCODE_MEDIA_AUDIO_TRACK",
        "key_longpress": "input keyevent --longpress 222",
        "key_press": "input keyevent 222",
    },
    223: {
        "key_name": "KEYCODE_SLEEP",
        "key_longpress": "input keyevent --longpress 223",
        "key_press": "input keyevent 223",
    },
    224: {
        "key_name": "KEYCODE_WAKEUP",
        "key_longpress": "input keyevent --longpress 224",
        "key_press": "input keyevent 224",
    },
    225: {
        "key_name": "KEYCODE_PAIRING",
        "key_longpress": "input keyevent --longpress 225",
        "key_press": "input keyevent 225",
    },
    226: {
        "key_name": "KEYCODE_MEDIA_TOP_MENU",
        "key_longpress": "input keyevent --longpress 226",
        "key_press": "input keyevent 226",
    },
    227: {
        "key_name": "KEYCODE_11",
        "key_longpress": "input keyevent --longpress 227",
        "key_press": "input keyevent 227",
    },
    228: {
        "key_name": "KEYCODE_12",
        "key_longpress": "input keyevent --longpress 228",
        "key_press": "input keyevent 228",
    },
    229: {
        "key_name": "KEYCODE_LAST_CHANNEL",
        "key_longpress": "input keyevent --longpress 229",
        "key_press": "input keyevent 229",
    },
    230: {
        "key_name": "KEYCODE_TV_DATA_SERVICE",
        "key_longpress": "input keyevent --longpress 230",
        "key_press": "input keyevent 230",
    },
    231: {
        "key_name": "KEYCODE_VOICE_ASSIST",
        "key_longpress": "input keyevent --longpress 231",
        "key_press": "input keyevent 231",
    },
    232: {
        "key_name": "KEYCODE_TV_RADIO_SERVICE",
        "key_longpress": "input keyevent --longpress 232",
        "key_press": "input keyevent 232",
    },
    233: {
        "key_name": "KEYCODE_TV_TELETEXT",
        "key_longpress": "input keyevent --longpress 233",
        "key_press": "input keyevent 233",
    },
    234: {
        "key_name": "KEYCODE_TV_NUMBER_ENTRY",
        "key_longpress": "input keyevent --longpress 234",
        "key_press": "input keyevent 234",
    },
    235: {
        "key_name": "KEYCODE_TV_TERRESTRIAL_ANALOG",
        "key_longpress": "input keyevent --longpress 235",
        "key_press": "input keyevent 235",
    },
    236: {
        "key_name": "KEYCODE_TV_TERRESTRIAL_DIGITAL",
        "key_longpress": "input keyevent --longpress 236",
        "key_press": "input keyevent 236",
    },
    237: {
        "key_name": "KEYCODE_TV_SATELLITE",
        "key_longpress": "input keyevent --longpress 237",
        "key_press": "input keyevent 237",
    },
    238: {
        "key_name": "KEYCODE_TV_SATELLITE_BS",
        "key_longpress": "input keyevent --longpress 238",
        "key_press": "input keyevent 238",
    },
    239: {
        "key_name": "KEYCODE_TV_SATELLITE_CS",
        "key_longpress": "input keyevent --longpress 239",
        "key_press": "input keyevent 239",
    },
    240: {
        "key_name": "KEYCODE_TV_SATELLITE_SERVICE",
        "key_longpress": "input keyevent --longpress 240",
        "key_press": "input keyevent 240",
    },
    241: {
        "key_name": "KEYCODE_TV_NETWORK",
        "key_longpress": "input keyevent --longpress 241",
        "key_press": "input keyevent 241",
    },
    242: {
        "key_name": "KEYCODE_TV_ANTENNA_CABLE",
        "key_longpress": "input keyevent --longpress 242",
        "key_press": "input keyevent 242",
    },
    243: {
        "key_name": "KEYCODE_TV_INPUT_HDMI_1",
        "key_longpress": "input keyevent --longpress 243",
        "key_press": "input keyevent 243",
    },
    244: {
        "key_name": "KEYCODE_TV_INPUT_HDMI_2",
        "key_longpress": "input keyevent --longpress 244",
        "key_press": "input keyevent 244",
    },
    245: {
        "key_name": "KEYCODE_TV_INPUT_HDMI_3",
        "key_longpress": "input keyevent --longpress 245",
        "key_press": "input keyevent 245",
    },
    246: {
        "key_name": "KEYCODE_TV_INPUT_HDMI_4",
        "key_longpress": "input keyevent --longpress 246",
        "key_press": "input keyevent 246",
    },
    247: {
        "key_name": "KEYCODE_TV_INPUT_COMPOSITE_1",
        "key_longpress": "input keyevent --longpress 247",
        "key_press": "input keyevent 247",
    },
    248: {
        "key_name": "KEYCODE_TV_INPUT_COMPOSITE_2",
        "key_longpress": "input keyevent --longpress 248",
        "key_press": "input keyevent 248",
    },
    249: {
        "key_name": "KEYCODE_TV_INPUT_COMPONENT_1",
        "key_longpress": "input keyevent --longpress 249",
        "key_press": "input keyevent 249",
    },
    250: {
        "key_name": "KEYCODE_TV_INPUT_COMPONENT_2",
        "key_longpress": "input keyevent --longpress 250",
        "key_press": "input keyevent 250",
    },
    251: {
        "key_name": "KEYCODE_TV_INPUT_VGA_1",
        "key_longpress": "input keyevent --longpress 251",
        "key_press": "input keyevent 251",
    },
    252: {
        "key_name": "KEYCODE_TV_AUDIO_DESCRIPTION",
        "key_longpress": "input keyevent --longpress 252",
        "key_press": "input keyevent 252",
    },
    253: {
        "key_name": "KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP",
        "key_longpress": "input keyevent --longpress 253",
        "key_press": "input keyevent 253",
    },
    254: {
        "key_name": "KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN",
        "key_longpress": "input keyevent --longpress 254",
        "key_press": "input keyevent 254",
    },
    255: {
        "key_name": "KEYCODE_TV_ZOOM_MODE",
        "key_longpress": "input keyevent --longpress 255",
        "key_press": "input keyevent 255",
    },
    256: {
        "key_name": "KEYCODE_TV_CONTENTS_MENU",
        "key_longpress": "input keyevent --longpress 256",
        "key_press": "input keyevent 256",
    },
    257: {
        "key_name": "KEYCODE_TV_MEDIA_CONTEXT_MENU",
        "key_longpress": "input keyevent --longpress 257",
        "key_press": "input keyevent 257",
    },
    258: {
        "key_name": "KEYCODE_TV_TIMER_PROGRAMMING",
        "key_longpress": "input keyevent --longpress 258",
        "key_press": "input keyevent 258",
    },
    259: {
        "key_name": "KEYCODE_HELP",
        "key_longpress": "input keyevent --longpress 259",
        "key_press": "input keyevent 259",
    },
    260: {
        "key_name": "KEYCODE_NAVIGATE_PREVIOUS",
        "key_longpress": "input keyevent --longpress 260",
        "key_press": "input keyevent 260",
    },
    261: {
        "key_name": "KEYCODE_NAVIGATE_NEXT",
        "key_longpress": "input keyevent --longpress 261",
        "key_press": "input keyevent 261",
    },
    262: {
        "key_name": "KEYCODE_NAVIGATE_IN",
        "key_longpress": "input keyevent --longpress 262",
        "key_press": "input keyevent 262",
    },
    263: {
        "key_name": "KEYCODE_NAVIGATE_OUT",
        "key_longpress": "input keyevent --longpress 263",
        "key_press": "input keyevent 263",
    },
    264: {
        "key_name": "KEYCODE_STEM_PRIMARY",
        "key_longpress": "input keyevent --longpress 264",
        "key_press": "input keyevent 264",
    },
    265: {
        "key_name": "KEYCODE_STEM_1",
        "key_longpress": "input keyevent --longpress 265",
        "key_press": "input keyevent 265",
    },
    266: {
        "key_name": "KEYCODE_STEM_2",
        "key_longpress": "input keyevent --longpress 266",
        "key_press": "input keyevent 266",
    },
    267: {
        "key_name": "KEYCODE_STEM_3",
        "key_longpress": "input keyevent --longpress 267",
        "key_press": "input keyevent 267",
    },
    268: {
        "key_name": "KEYCODE_DPAD_UP_LEFT",
        "key_longpress": "input keyevent --longpress 268",
        "key_press": "input keyevent 268",
    },
    269: {
        "key_name": "KEYCODE_DPAD_DOWN_LEFT",
        "key_longpress": "input keyevent --longpress 269",
        "key_press": "input keyevent 269",
    },
    270: {
        "key_name": "KEYCODE_DPAD_UP_RIGHT",
        "key_longpress": "input keyevent --longpress 270",
        "key_press": "input keyevent 270",
    },
    271: {
        "key_name": "KEYCODE_DPAD_DOWN_RIGHT",
        "key_longpress": "input keyevent --longpress 271",
        "key_press": "input keyevent 271",
    },
    272: {
        "key_name": "KEYCODE_MEDIA_SKIP_FORWARD",
        "key_longpress": "input keyevent --longpress 272",
        "key_press": "input keyevent 272",
    },
    273: {
        "key_name": "KEYCODE_MEDIA_SKIP_BACKWARD",
        "key_longpress": "input keyevent --longpress 273",
        "key_press": "input keyevent 273",
    },
    274: {
        "key_name": "KEYCODE_MEDIA_STEP_FORWARD",
        "key_longpress": "input keyevent --longpress 274",
        "key_press": "input keyevent 274",
    },
    275: {
        "key_name": "KEYCODE_MEDIA_STEP_BACKWARD",
        "key_longpress": "input keyevent --longpress 275",
        "key_press": "input keyevent 275",
    },
    276: {
        "key_name": "KEYCODE_SOFT_SLEEP",
        "key_longpress": "input keyevent --longpress 276",
        "key_press": "input keyevent 276",
    },
    277: {
        "key_name": "KEYCODE_CUT",
        "key_longpress": "input keyevent --longpress 277",
        "key_press": "input keyevent 277",
    },
    278: {
        "key_name": "KEYCODE_COPY",
        "key_longpress": "input keyevent --longpress 278",
        "key_press": "input keyevent 278",
    },
    279: {
        "key_name": "KEYCODE_PASTE",
        "key_longpress": "input keyevent --longpress 279",
        "key_press": "input keyevent 279",
    },
    280: {
        "key_name": "KEYCODE_SYSTEM_NAVIGATION_UP",
        "key_longpress": "input keyevent --longpress 280",
        "key_press": "input keyevent 280",
    },
    281: {
        "key_name": "KEYCODE_SYSTEM_NAVIGATION_DOWN",
        "key_longpress": "input keyevent --longpress 281",
        "key_press": "input keyevent 281",
    },
    282: {
        "key_name": "KEYCODE_SYSTEM_NAVIGATION_LEFT",
        "key_longpress": "input keyevent --longpress 282",
        "key_press": "input keyevent 282",
    },
    283: {
        "key_name": "KEYCODE_SYSTEM_NAVIGATION_RIGHT",
        "key_longpress": "input keyevent --longpress 283",
        "key_press": "input keyevent 283",
    },
    284: {
        "key_name": "KEYCODE_ALL_APPS",
        "key_longpress": "input keyevent --longpress 284",
        "key_press": "input keyevent 284",
    },
    285: {
        "key_name": "KEYCODE_REFRESH",
        "key_longpress": "input keyevent --longpress 285",
        "key_press": "input keyevent 285",
    },
    286: {
        "key_name": "KEYCODE_THUMBS_UP",
        "key_longpress": "input keyevent --longpress 286",
        "key_press": "input keyevent 286",
    },
    287: {
        "key_name": "KEYCODE_THUMBS_DOWN",
        "key_longpress": "input keyevent --longpress 287",
        "key_press": "input keyevent 287",
    },
    288: {
        "key_name": "KEYCODE_PROFILE_SWITCH",
        "key_longpress": "input keyevent --longpress 288",
        "key_press": "input keyevent 288",
    },
    289: {
        "key_name": "KEYCODE_VIDEO_APP_1",
        "key_longpress": "input keyevent --longpress 289",
        "key_press": "input keyevent 289",
    },
    290: {
        "key_name": "KEYCODE_VIDEO_APP_2",
        "key_longpress": "input keyevent --longpress 290",
        "key_press": "input keyevent 290",
    },
    291: {
        "key_name": "KEYCODE_VIDEO_APP_3",
        "key_longpress": "input keyevent --longpress 291",
        "key_press": "input keyevent 291",
    },
    292: {
        "key_name": "KEYCODE_VIDEO_APP_4",
        "key_longpress": "input keyevent --longpress 292",
        "key_press": "input keyevent 292",
    },
    293: {
        "key_name": "KEYCODE_VIDEO_APP_5",
        "key_longpress": "input keyevent --longpress 293",
        "key_press": "input keyevent 293",
    },
    294: {
        "key_name": "KEYCODE_VIDEO_APP_6",
        "key_longpress": "input keyevent --longpress 294",
        "key_press": "input keyevent 294",
    },
    295: {
        "key_name": "KEYCODE_VIDEO_APP_7",
        "key_longpress": "input keyevent --longpress 295",
        "key_press": "input keyevent 295",
    },
    296: {
        "key_name": "KEYCODE_VIDEO_APP_8",
        "key_longpress": "input keyevent --longpress 296",
        "key_press": "input keyevent 296",
    },
    297: {
        "key_name": "KEYCODE_FEATURED_APP_1",
        "key_longpress": "input keyevent --longpress 297",
        "key_press": "input keyevent 297",
    },
    298: {
        "key_name": "KEYCODE_FEATURED_APP_2",
        "key_longpress": "input keyevent --longpress 298",
        "key_press": "input keyevent 298",
    },
    299: {
        "key_name": "KEYCODE_FEATURED_APP_3",
        "key_longpress": "input keyevent --longpress 299",
        "key_press": "input keyevent 299",
    },
    300: {
        "key_name": "KEYCODE_FEATURED_APP_4",
        "key_longpress": "input keyevent --longpress 300",
        "key_press": "input keyevent 300",
    },
    301: {
        "key_name": "KEYCODE_DEMO_APP_1",
        "key_longpress": "input keyevent --longpress 301",
        "key_press": "input keyevent 301",
    },
    302: {
        "key_name": "KEYCODE_DEMO_APP_2",
        "key_longpress": "input keyevent --longpress 302",
        "key_press": "input keyevent 302",
    },
    303: {
        "key_name": "KEYCODE_DEMO_APP_3",
        "key_longpress": "input keyevent --longpress 303",
        "key_press": "input keyevent 303",
    },
    304: {
        "key_name": "KEYCODE_DEMO_APP_4",
        "key_longpress": "input keyevent --longpress 304",
        "key_press": "input keyevent 304",
    },
}


def get_tmpfile(suffix=".txt"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    return filename, partial(os.remove, tfp.name)


def connect_to_adb(adb_path, deviceserial):
    _ = subprocess.run(f"{adb_path} start-server", capture_output=True, shell=False)
    _ = subprocess.run(
        f"{adb_path} connect {deviceserial}", capture_output=True, shell=False
    )


def execute_adb_command(
    cmd: str, subcommands: list, exit_keys: str = "ctrl+x", end_of_printline: str = ""
) -> list:
    if isinstance(subcommands, str):
        subcommands = [subcommands]
    elif isinstance(subcommands, tuple):
        subcommands = list(subcommands)
    popen = None

    def run_subprocess(cmd):
        nonlocal popen

        def kill_process():
            nonlocal popen
            try:
                print("Killing the process")
                p = psutil.Process(popen.pid)
                p.kill()
                try:
                    if exit_keys in keyboard__.__dict__["_hotkeys"]:
                        keyboard__.remove_hotkey(exit_keys)
                except Exception:
                    try:
                        keyboard__.unhook_all_hotkeys()
                    except Exception:
                        pass
            except Exception:
                try:
                    keyboard__.unhook_all_hotkeys()
                except Exception:
                    pass

        if exit_keys not in keyboard__.__dict__["_hotkeys"]:
            keyboard__.add_hotkey(exit_keys, kill_process)

        DEVNULL = open(os.devnull, "wb")
        try:
            popen = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                stderr=DEVNULL,
                shell=False,
            )

            for subcommand in subcommands:
                if isinstance(subcommand, bytes):
                    subcommand = subcommand.rstrip(b"\n") + b"\n"

                    subcommand = subcommand.decode("utf-8", "replace")
                else:
                    subcommand = subcommand.rstrip("\n") + "\n"

                popen.stdin.write(subcommand)

            popen.stdin.close()

            for stdout_line in iter(popen.stdout.readline, ""):
                try:
                    yield stdout_line
                except Exception as Fehler:
                    continue
            popen.stdout.close()
            return_code = popen.wait()
        except Exception as Fehler:
            # print(Fehler)
            try:
                popen.stdout.close()
                return_code = popen.wait()
            except Exception as Fehler:
                yield ""

    proxyresults = []
    try:
        for proxyresult in run_subprocess(cmd):
            proxyresults.append(proxyresult)
            print(proxyresult, end=end_of_printline)
    except KeyboardInterrupt:
        try:
            p = psutil.Process(popen.pid)
            p.kill()
            popen = None
        except Exception as da:
            pass
            # print(da)

    try:
        if popen is not None:
            p = psutil.Process(popen.pid)
            p.kill()
    except Exception as da:
        pass

    try:
        if exit_keys in keyboard__.__dict__["_hotkeys"]:
            keyboard__.remove_hotkey(exit_keys)
    except Exception:
        try:
            keyboard__.unhook_all_hotkeys()
        except Exception:
            pass
    return proxyresults


class AdbUnicodeKeyboard:
    def __init__(self, adb_path, deviceserial, exit_keys="ctrl+x"):
        self.exit_key = exit_keys
        self.adb_path = adb_path
        self.deviceserial = deviceserial

    def connect_to_adb(self):
        connect_to_adb(
            adb_path=self.adb_path, deviceserial=self.deviceserial,
        )
        for key, item in keyeventdict.items():
            generalname = str(item["key_name"]).lower()
            if str(generalname).isidentifier():
                keypress = f"press_{str(key)}_{generalname}".lower()
                keylongpress = f"longpress_{str(key)}_{generalname}".lower()
                setattr(
                    self,
                    keypress,
                    FlexiblePartial(
                        execute_adb_command,
                        True,
                        cmd=f"{self.adb_path} -s {self.deviceserial} shell",
                        subcommands=[item["key_press"] + "\nexit"],
                        exit_keys=self.exit_key,
                        end_of_printline="",
                    ),
                ),
                setattr(
                    self,
                    keylongpress,
                    FlexiblePartial(
                        execute_adb_command,
                        True,
                        cmd=f"{self.adb_path} -s {self.deviceserial} shell",
                        subcommands=[item["key_longpress"] + "\nexit"],
                        exit_keys=self.exit_key,
                        end_of_printline="",
                    ),
                ),

        return self

    def uninstall_adb_keyboard(self):
        execute_adb_command(
            f"{self.adb_path} -s {self.deviceserial} shell",
            ["pm uninstall com.android.adbkeyboard"],
        )
        return self

    def install_adb_keyboard(self):
        keyb = requests.get(
            r"https://github.com/senzhk/ADBKeyBoard/raw/master/ADBKeyboard.apk"
        )
        tmpfile_, removetmpfile = get_tmpfile(".apk")
        with open(tmpfile_, mode="wb") as f:
            f.write(keyb.content)

        subprocess.run(f"{self.adb_path} -s {self.deviceserial} install {tmpfile_}")
        sleep(5)
        removetmpfile()
        return self

    def send_unicode_text_with_delay(self, text, delay_range=(0.05, 0.3)):
        for t in list(text):
            self.send_unicode_text(t)
            sleep((uniform(*delay_range)))
        return self

    def send_unicode_text(self, text):
        charsb64 = str(base64.b64encode(text.encode("utf-8")))[1:]

        execute_adb_command(
            cmd=f"{self.adb_path} -s {self.deviceserial} shell",
            subcommands=[
                f"""am broadcast -a ADB_INPUT_B64 --es msg {charsb64}\nexit"""
            ],
        )
        return self

    def get_all_installed_keyboards(self):
        installedkeyboards = execute_adb_command(
            cmd=f"{self.adb_path} -s {self.deviceserial} shell",
            subcommands=["ime list -a"],
        )
        keyboards = [
            x.strip().strip(":")
            for x in installedkeyboards
            if regex.search(r"^[^\s]", x)
        ]
        keyboards = [x.strip() for x in keyboards]
        return keyboards

    def is_keyboard_shown(self):
        return "mInputShown=true" in subprocess.run(
            f"{self.adb_path} -s {self.deviceserial} shell dumpsys input_method",
            capture_output=True,
        ).stdout.decode("utf-8", "ignore")

    def activate_adb_keyboard(self):
        keyboards = self.get_all_installed_keyboards()
        keyba = [x for x in keyboards if "com.android.adbkeyboard" in x][0]
        execute_adb_command(
            cmd=f"{self.adb_path} -s {self.deviceserial} shell",
            subcommands=[f"ime set {keyba}"],
        )
        return self

    def disable_adb_keyboard(self, new_keyboard_name=None):
        if new_keyboard_name is None:
            keyboards = self.get_all_installed_keyboards()
            try:
                keyba = [x for x in keyboards if "com.android.inputmethod" in x][0]
            except Exception:
                execute_adb_command(
                    cmd=f"{self.adb_path} -s {self.deviceserial} shell",
                    subcommands=["""ime reset"""],
                )
                return self

        else:
            keyba = new_keyboard_name
        execute_adb_command(
            cmd=f"{self.adb_path} -s {self.deviceserial} shell",
            subcommands=[f"ime set {keyba}"],
        )
        return self
