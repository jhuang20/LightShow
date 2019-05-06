import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    a = calculate_ambient(ambient,areflect)
    d = calculate_diffuse(light,dreflect,normal)
    s = calculate_specular(light,sreflect,view,normal)
    #a = [0,0,0]
    #s = [0,0,0]
    #d = [0,0,0]
    color =[(a[p]+d[p]+s[p]) for p in range(3)]
    color=limit_color(color)
    return color
def calculate_ambient(alight, areflect):
    final=[alight[0]*areflect[0], alight[1]*areflect[1], alight[2]*areflect[2]]
    return [c for c in final]
def calculate_diffuse(light, dreflect, normal):
    l,col=light
    normalize(l)
    normalize(normal)
    p=dot_product(normal, l)
    final=[dreflect[i]*p*col[i] for i in range(3)]
    return [c for c in final]
def calculate_specular(light, sreflect, view, normal):
    l,color=light
    normalize(l)
    normalize(normal)
    newNorm=[l[num]-normal[num] for num in range(3)]
    first=[2*a for a in normal]
    b=[first[num]*newNorm[num] for num in range(3)]
    mainVector=[b[obj]-l[obj] for obj in range(3)]
    p=dot_product(view, mainVector)
    final=[((sreflect[0]*p)**SPECULAR_EXP)*color[0],((sreflect[1]*p)**SPECULAR_EXP)*color[1],((sreflect[2]*p)**SPECULAR_EXP)*color[2]]
    return [c for c in final]
def limit_color(color):
    for i in range(len(color)):
        if color[i]>255:
            color[i]=255
    return color



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
