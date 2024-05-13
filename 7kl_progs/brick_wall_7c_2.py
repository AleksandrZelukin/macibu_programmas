import simple_draw as sd
shift = 50
for y in range(0, 600, 50):
    length_x = 95
    length_y = 45
    shift = 50 - shift
    for x in range(0 - shift, 600, 100):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + length_x, y + length_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)
        left_bottom = sd.get_point(x+1, y+1)
        right_top = sd.get_point(x + length_x - 1, y + length_y - 1)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.random_color(), width=0)
sd.pause()