import datetime
import platform
import sys

from PIL import Image, ImageDraw, ImageFont

import kindle_gui
from fahrplan import Timetable

font_path = '/home/finn/Programmieren/Kindle/fahrplan_kindle/fonts'

screen_height = 800
screen_width = 600

BLACK = (0, 0, 0, 255)
GRAY1 = ((16*2-1), (16*2-1), (16*2-1), 255)
GRAY2 = ((16*3-1), (16*3-1), (16*3-1), 255)
GRAY3 = ((16*4-1), (16*4-1), (16*4-1), 255)
GRAY4 = ((16*5-1), (16*5-1), (16*5-1), 255)
GRAY5 = ((16*6-1), (16*6-1), (16*6-1), 255)
GRAY6 = ((16*7-1), (16*7-1), (16*7-1), 255)
GRAY7 = ((16*8-1), (16*8-1), (16*8-1), 255)
GRAY8 = ((16*9-1), (16*9-1), (16*9-1), 255)
GRAY9 = ((16*10-1), (16*10-1), (16*10-1), 255)
GRAYA = ((16*11-1), (16*11-1), (16*11-1), 255)
GRAYB = ((16*12-1), (16*12-1), (16*12-1), 255)
GRAYC = ((16*13-1), (16*13-1), (16*13-1), 255)
GRAYD = ((16*14-1), (16*14-1), (16*14-1), 255)
GRAYE = ((16*15-1), (16*15-1), (16*15-1), 255)
WHITE = ((16*16-1), (16*16-1), (16*16-1), 255)


def testing():
    kindle_gui.gui()


if __name__ == "__main__":
    if platform.release() != '5.19.0-76051900-generic':
        testing()
        sys.exit()

    # Create timetable objects for the two destinations and have them load the connections
    timetable_frankfurt = Timetable('29fcbcce-2851-4ce3-8c9c-b2a39645cff2', 'Frankfurt West')
    timetable_frankfurt.refresh()
    timetable_giessen = Timetable('29fcbcce-2851-4ce3-8c9c-b2a39645cff2', 'Gießen')
    timetable_giessen.refresh()

    fnt_small = ImageFont.truetype(f'{font_path}/Caecilia_LT_65_Medium.ttf', 40)
    fnt_big = ImageFont.truetype(f'{font_path}/Caecilia_LT_65_Medium.ttf', 100)

    # Create image
    im = Image.new("RGBA", (screen_width, screen_height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)

    # Direction 1 Header
    draw.rectangle((0, 0, screen_width, 60), fill=GRAY1, width=1)
    draw.text((50, 60), f'{timetable_frankfurt.connections[0].departure.strftime("%H:%M")}', font=fnt_big, fill=BLACK)
    draw.text((400, 60), f'+{timetable_frankfurt.connections[0].delay}', font=fnt_big, fill=BLACK)

    draw.text((50, 60+1*100+50), f'{timetable_frankfurt.connections[1].departure.strftime("%H:%M")}', font=fnt_big, fill=BLACK)
    draw.text((400, 60+1*100+50), f'+{timetable_frankfurt.connections[1].delay}', font=fnt_big, fill=BLACK)


    draw.text((10, 0), "Richtung Frankfurt", font=fnt_small, fill=WHITE)

    # Directon 2 Header
    draw.rectangle((0, screen_height/2, screen_width, screen_height/2 + 60), fill=GRAY1, width=1)
    draw.text((10, screen_height/2), "Richtung Gießen", font=fnt_small, fill=WHITE)

    draw.text((50, screen_height/2 + 60), f'{timetable_frankfurt.connections[0].departure.strftime("%H:%M")}', font=fnt_big, fill=BLACK)
    draw.text((400, screen_height/2 + 60), f'+{timetable_frankfurt.connections[0].delay}', font=fnt_big, fill=BLACK)
    draw.text((310, screen_height / 2 + 60 + 20), f'{timetable_giessen.connections[0].train_type}', font=fnt_small, fill=BLACK)

    draw.text((50, screen_height/2 + 60 + 1 * 100 + 50), f'{timetable_frankfurt.connections[1].departure.strftime("%H:%M")}', font=fnt_big, fill=BLACK)
    draw.text((400, screen_height/2 + 60 + 1 * 100 + 50), f'+{timetable_frankfurt.connections[1].delay}', font=fnt_big, fill=BLACK)
    draw.text((310, screen_height / 2 + 60 + 1 * 100 + 50 + 20), f'{timetable_giessen.connections[0].train_type}', font=fnt_small,fill=BLACK)

    # Clock
    fnt_clock = ImageFont.truetype(f'{font_path}/Caecilia_LT_65_Medium.ttf', 50)
    draw.text((450, 730), datetime.datetime.now().strftime("%H:%M"), font=fnt_clock, fill=BLACK)

    im.show()
