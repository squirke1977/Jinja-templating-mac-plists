import csv
import os
import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from sys import argv
from jinja2 import *

script, file_name = argv

FuzeRooms = open(file_name, "r")
csvReader = csv.reader(FuzeRooms)
header = csvReader.next()

RoomName = header.index("Room")
RoomURL = header.index("URL")

working_directory = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=FileSystemLoader(working_directory))
template = env.get_template('Jinja-Fuzeroom-template')


for row in csvReader:
    isRoomName = row[RoomName].strip()
    isRoomURL = row[RoomURL].strip()
    
    room_config = {"Room_username": isRoomURL, "Username_To_Join": isRoomName}

    filename = isRoomName + ".mobileconfig"

    outputfile = open(filename, 'w')     
    outputfile.write(template.render(room_config))
    outputfile.close

print("All done")
