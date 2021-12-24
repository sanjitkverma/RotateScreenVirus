import rotatescreen
import time
screen = rotatescreen.get_primary_display()
i = 1
while i >= 1:
    time.sleep(0.1)
    screen.rotate_to(i * 90 % 360)
    i += 1

