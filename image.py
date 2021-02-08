import random
import os
from PIL import Image, ImageDraw, ImageFont


class MemeCreator:
	@staticmethod
	def draw_meme_with_text(output_file_name, text, font_size=40, x=0, y=0, center_x=False, center_y=False,color_text='white'):
		image = Image.open(f'pictures/{random.choice([file for file in os.walk("pictures")][0][2])}')
		draw = ImageDraw.Draw(image)
		width_image, height_image = image.size
		if center_x:
			x = int((width_image - font_size * len(text) / 1.9) / 2)
		if center_y:
			y = (height_image - font_size) / 2

		font = ImageFont.truetype("font.ttf", size=font_size)
		draw.text((x,y),text, font=font,fill=color_text)
		image.save(f'static/{output_file_name}.jpg')


