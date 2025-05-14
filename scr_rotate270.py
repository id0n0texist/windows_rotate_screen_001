import rotatescreen
from screeninfo import get_monitors

width_m = get_monitors()[0].width
height_m = get_monitors()[0].height
screen = rotatescreen.get_primary_display()

name = __file__
name = name.split("\\")
name1 = str(name[-1])

if "270" in name1:
	if width_m > height_m:
		screen.rotate_to(270)
	else:
		screen.rotate_to(0)
elif "90" in name1:
	if width_m > height_m:
		screen.rotate_to(90)
	else:
		screen.rotate_to(0)
else:
	screen.rotate_to(0)