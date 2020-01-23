import dxfgrabber
import numpy as np
import math
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt

#импорт файла
dwg  = dxfgrabber.readfile("dxf/t3.dxf", options = {"grab_blocks": True,"resolve_text_styles": True})
dwg2  = dxfgrabber.readfile("dxf/t2.dxf", options = {"grab_blocks": True,"resolve_text_styles": True})
#находит длинну линии
def line_len(line):
    start_x = line.start[0]
    start_y = line.start[1]
    end_x = line.end[0]
    end_y = line.end[1]
    res = (math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2))
    #print(res)
    return res
def line_len_from_center(coord, center):
    start_x = coord[0]
    start_y = coord[1]
    end_x = center[0]
    end_y = center[1]
    res = (math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2))
    #print(res)
    return res
"""формирует массив с координатами начала и конца всех строк"""
def lines_cords_to_list(all_lines):
    coords_array = np.zeros((len(all_lines), 4))
    for i in range(len(all_lines)):
        coords_array[i] = [all_lines[i].start[0], all_lines[i].start[1], all_lines[i].end[0], all_lines[i].end[1]]
    #print(coords_array)
    return coords_array

def lines_cords_to_list_2(all_lines):
    coords_array = np.zeros((len(all_lines)*2, 2))
    for i in range(len(all_lines)):
        coords_array[i] = [all_lines[i].start[0], all_lines[i].start[1]]
    for i in range(len(all_lines)):
        coords_array[len(all_lines)*2 - i-1] = [ all_lines[i].end[0], all_lines[i].end[1]]
    return coords_array

#поиск всех линий
all_lines = [entity for entity in dwg.entities if entity.dxftype == 'LINE']
print("--------------------")
a = lines_cords_to_list_2(all_lines)

hull = ConvexHull(a, True)
plt.plot(a[:,0], a[:,1], 'o')
coords = np.zeros((hull.simplices.shape[0], 2))
p = 0
"""for simplex in hull.simplices:
    plt.plot(a[simplex, 0], a[simplex, 1], 'k-')
    coords[p] = (a[simplex[1], 0], a[simplex[1], 1])
    p +=1
plt.plot(a[hull.vertices,0], a[hull.vertices,1], 'r--', lw=2)
plt.plot(a[hull.vertices[0],0], a[hull.vertices[0],1], 'ro')
plt.show()
cx = np.mean(hull.points[hull.vertices,0])
cy = np.mean(hull.points[hull.vertices,1])
plt.plot(cx, cy,'*',ms=20)
mass1 = np.zeros((coords.shape[0], 1))
print("растояния от вершин до центра первой фигуры")
for m in range(coords.shape[0]):
    mass1[m] = (line_len_from_center(coords[m], (cx, cy)))
mass1 = np.sort(mass1, axis=0, kind='stable', order=None)
print(mass1)"""
def mass_get(dwg):
	#поиск всех линий
	all_lines = [entity for entity in dwg.entities if entity.dxftype == 'LINE']
	a = lines_cords_to_list_2(all_lines)
	
	hull = ConvexHull(a, True)
	plt.plot(a[:,0], a[:,1], 'o')
	coords = np.zeros((hull.simplices.shape[0], 2))
	p = 0
	for simplex in hull.simplices:
		plt.plot(a[simplex, 0], a[simplex, 1], 'k-')
		coords[p] = (a[simplex[1], 0], a[simplex[1], 1])
		p +=1
	plt.plot(a[hull.vertices,0], a[hull.vertices,1], 'r--', lw=2)
	plt.plot(a[hull.vertices[0],0], a[hull.vertices[0],1], 'ro')
	cx = np.mean(hull.points[hull.vertices,0])
	cy = np.mean(hull.points[hull.vertices,1])
	plt.plot(cx, cy,'*',ms=20)
	mass1 = np.zeros((int(coords.size/2), 1))
	for m in range(int(coords.size/2)):
		mass1[m] = (line_len_from_center(coords[m], (cx, cy)))
	return np.sort(mass1, axis=0, kind='stable', order=None)

x1 = mass_get(dwg)
x2 = mass_get(dwg2)
print(x1)
print(x2)


def equal_fig(x1, x2):
    res = 0
    
    if(np.array_equal(x1, x2)) :
        return True    
    if(x1.size == x2.size):
        print("size is equal")
        if(x1[0] > x2[0]):
            print("X1 >X2")
            for i in range(x1.size):
                if (res != 0):
                    if (res == int(x1[i]/x2[i])): 
                        print("совпадение")
                        res = int(x1[i]/x2[i])
                    else:
                        return False
                else:
                    res = int (x1[i]/x2[i])
        else:
            for i in range(x1.size):
                if (res != 0):
                    if (res == int(x2[i]/x1[i])): 
                        print("совпадение")
                        res = int(x2[i]/x1[i])
                    else:
                        return False
                else:                    
                    res = int(x2[i]/x1[i])
    return True


print(equal_fig(x1, x2))