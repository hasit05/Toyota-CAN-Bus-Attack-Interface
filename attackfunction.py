
from can import Message
import os, binascii

def changespeed_50():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0XB4
    Message.dlc = 8
    Message.data = [0x00, 0x00, 0x00, 0x00, 0x51, 0x12, 0x66, 0xB5]
    return Message



def changespeed_100():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0XB4
    Message.dlc = 8
    Message.data = [0x00, 0x00, 0x00, 0x00, 0x51, 0x25, 0x66, 0xB5]
    return Message

def changespeed_150():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0XB4
    Message.dlc = 8
    Message.data = [0x00, 0x00, 0x00, 0x00, 0x51, 0x37, 0x66, 0xB5]
    return Message


def changespeed_full():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0XB4
    Message.dlc = 8
    Message.data = [0x00, 0x00, 0x00, 0x00, 0x51, 0x65, 0x66, 0xB5]
    return Message


def changespeed_randomtrip():
    return os.system('cansend can1 0B4#$(openssl rand -hex 8)')


def changefuel_full():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X7C0
    Message.dlc = 8
    Message.data = [0x04, 0x30, 0x03, 0x00, 0x40, 0x00, 0x00, 0x00]
    return Message

def changefuel_quarter():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X7C0
    Message.dlc = 8
    Message.data = [0x04, 0x30, 0x03, 0x00, 0x08, 0x00, 0x00, 0x00]
    return Message

def changefuel_half():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X7C0
    Message.dlc = 8
    Message.data = [0x04, 0x30, 0x03, 0x00, 0x10, 0x00, 0x00, 0x00]
    return Message

def changefuel_threequarter():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X7C0
    Message.dlc = 8
    Message.data = [0x04, 0x30, 0x03, 0x00, 0x20, 0x00, 0x00, 0x00]
    return Message


def changefuel_emptybeep():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X7C0
    Message.dlc = 8
    Message.data = [0x04, 0x30, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00]
    return Message


def open_driverdoor():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X620
    Message.dlc = 8
    Message.data = [0x10, 0x80, 0xFF, 0xFF, 0x80, 0x20, 0x00, 0x80]
    return Message


def open_passengerdoor():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X620
    Message.dlc = 8
    Message.data = [0x10, 0x80, 0xFF, 0xFF, 0x80, 0x10, 0x00, 0x80]
    return Message

def close_alldoor():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X620
    Message.dlc = 8
    Message.data = [0x10, 0x80, 0xFF, 0xFF, 0x80, 0x02, 0x00, 0x80]
    return Message

def open_reardoors():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X620
    Message.dlc = 8
    Message.data = [0x10, 0x80, 0xFF, 0xFF, 0x80, 0x0C, 0x00, 0x80]
    return Message

def open_frontdoors():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X620
    Message.dlc = 8
    Message.data = [0x10, 0x80, 0xFF, 0xFF, 0x00, 0x70, 0x00, 0x80]
    return Message


def highbeam():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X622
    Message.dlc = 8
    Message.data = [0x12, 0x80, 0x88, 0x70, 0x00, 0x00, 0x00, 0x00]
    return Message

def headlamp():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X622
    Message.dlc = 8
    Message.data = [0x12, 0x80, 0x88, 0x30, 0x00, 0x00, 0x00, 0x00]
    return Message

def interiorlight():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X622
    Message.dlc = 8
    Message.data = [0x12, 0x80, 0x88, 0x48, 0x00, 0x00, 0x00, 0x00]
    return Message

def lightsoff():
    Message.is_extended_id = False
    Message.is_remote_frame = False
    Message.id_type = 0
    Message.is_error_frame = False
    Message.arbitration_id = 0X622
    Message.dlc = 8
    Message.data = [0x12, 0x80, 0x88, 0x00, 0x00, 0x00, 0x00, 0x00]
    return Message

