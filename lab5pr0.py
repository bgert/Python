'''Name: Ben Gertz
    Course: CMPS 1500
    Lab Section: Tuesday 5-6.15 PM
    Assignment: Lab 5 Part 0
    Date: 10/9/2017
    This program has three functions. get_header ((str, str) -> str) outputs a string formatted to be the header of a .ppm file. netherlands ((int, int) -> str) outputs a string with the body of a .ppm file.
    main ((int, int, str) -> str) asks for the dimensions of the image and the output file, then creates the file and outputs the image. nigeria ((int, int) -> str) takes the width and height of the nigerian flag
    and outputs a string for the body of a .ppm file. uae ((int, int) -> str) takes the width and height of the UAE flag and outputs a string for the body of a .ppm image file.
'''

def get_header(width, height):
    '''
    (int, int) -> str
    '''
    return 'P3\n' + str(width) + ' ' + str(height) + '\n' + '255\n'

def netherlands(width, height):
    '''
    (int, int) -> str
    '''
    red = '255 0 0 '
    blue = '0 0 255 '
    white = '255 255 255 '
    rows = height // 3
    out = (red * (width * rows)) + (white * (width * rows)) + (blue * (width * rows))
    return out
def nigeria(width, height):
    '''
    (int, int) -> str
    '''
    white = '255 255 255 '
    green = '0 255 0 '
    columns = width // 3
    out = ((green * columns) + (white * columns) + (green * columns)) * height
    return out
def uae(width, height):
    '''
    (int, int) -> str
    '''
    white = '255 255 255 '
    green = '0 255 0 '
    red = '255 0 0 '
    black = '0 0 0 '
    left = width // 4
    rows = width - left
    thirds = height // 3
    work_green = 0
    work_white = 0
    work_black = 0
    progress = 0
    out = ''
    while progress < height:
        while work_green < thirds:
            out += (red * left) + (green * rows)
            work_green += 1
            progress += 1
            continue
        while work_white < thirds:
            out += (red * left) + (white * rows)
            work_white += 1
            progress += 1
            continue
        while work_black < thirds:
            out += (red * left) + (black * rows)
            work_black += 1
            progress += 1
            continue
        return out
def main():
    '''
    (int, int, str) -> file, str
    '''
    width = int(input('Please, enter width: '))
    height = int(input('Please, enter height: '))
    file_name = input('Please, enter output file name: ')
    f = open(file_name, 'w')
    f.write(get_header(width, height) + '\n' + uae(width, height))
    f.close()
    print('The output has been written to', file_name + '\nView the result in XnView')
