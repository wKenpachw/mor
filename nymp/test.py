import dxfgrabber
import numpy as np
import math

dwg  = dxfgrabber.readfile("dxf/t2.dxf", options = {"resolve_text_styles": True})
def line_len(line):
    start_x = line.start[0]
    start_y = line.start[1]
    end_x = line.end[0]
    end_y = line.end[1]
    res = (math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2))
    #print(res)
    return res
"""layer_count = len(dwg.layers)
print(dwg.layers["text"])
all_layer_0_entities = [entity for entity in dwg.entities if entity.layer == 'text']
entities = [e for e in dwg.entities if e.layer=='text']
text_entities = [e for e in entities if e.dxftype=='text']
print(all_layer_0_entities[4].raw_text)
r = MText (all_layer_0_entities[4])
for i in range(len(all_layer_0_entities)):
    print (all_layer_0_entities[i])"""
"""
#Поиск всего mtext
all_mtext = [entity for entity in dwg.entities if entity.dxftype == 'MTEXT']
for text in all_mtext:
    print (text.raw_text)"""
"""
#поиск всего текста
all_mtext = [entity for entity in dwg.entities if entity.dxftype == 'TEXT']
for text in all_mtext:
    print (text.text)"""
#поиск всех линий
all_lines = [entity for entity in dwg.entities if entity.dxftype == 'LINE']
a = np.array([all_lines[0].start, all_lines[0].end])
b = list()
for line in all_lines:
    b.append([line.start, line.end])
    print(line_len(line))
"""    print(line.start)
    print(line.end)
    print("--------")"""
"""#Поиск всех кругов    
all_circle = [entity for entity in dwg.entities if entity.dxftype == 'Circle']
for circle in all_circle:
    print (circle.center)"""
"""print(b[0][0][0])
print(b[0][1][0])
res = (math.sqrt((b[0][1][0] - b[0][0][0])**2 + (b[0][1][1] - b[0][0][1])**2))
#res = (b[0][1][0] - b[0][0][0])**2
print(res)"""
