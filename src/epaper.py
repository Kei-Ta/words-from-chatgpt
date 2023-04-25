#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import openai
openai.organization = "org-i67052IR1mBaY8hVwVLPa912"
openai.api_key = os.getenv("OPENAI_API_KEY")


picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in7b Demo")
    
    epd = epd2in7b.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")
    blackimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    redimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    

    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRedimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126    
    drawblack = ImageDraw.Draw(HBlackimage)
    drawred = ImageDraw.Draw(HRedimage)
    drawblack.text((10, 0), 'ChatGPTからの一言', font = font24, fill = 0)
    drawred.line((0, 30, 264, 30), fill = 0)
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "運勢占いと始業前に仕事のやる気が起きるような一言を100文字以内で一つの文章でください。"}
    ]   
    )
    print(response["choices"][0]["message"]["content"])
    #text = '今日も一歩ずつ成長し、自分を高めるために全力で取り組もう！'
    text = response["choices"][0]["message"]["content"]
    split_len = 14
    q, r = len(text) // split_len, len(text) % split_len
    count = q + 1 if r != 0 else 0
    split_text = [text[x:x+split_len] for x in range(0, len(text), split_len)]
    for i in range(count):
      raw = i * 20 + 40
      drawblack.text((0, raw), split_text[i], font = font18, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
    time.sleep(20)
        
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7b.epdconfig.module_exit()
    exit()
