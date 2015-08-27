import sublime, sublime_plugin, os, random, shutil
from xml.dom.minidom import parse

defaultScheme = sublime.packages_path() + "/User/VSDefault.tmTheme"
currentScheme = sublime.packages_path() + "/User/VS.tmTheme"

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)

def change(colors):
    rgb = hex_to_rgb(colors[0].nodeValue)
    scale = 3
    counter = 1000
    while (counter > 0):
        counter -= 1
        two = random.randint(0,2)
        sign = random.choice([1,-1])
        twoChange = sign * (-2) * scale
        oneChange = sign * scale
        if ((twoChange + rgb[two] > 255) or (rgb[two] - twoChange < 0)):
            continue
        if ((oneChange + rgb[(two + 1) % 3] > 255) or (rgb[(two + 1) % 3] - oneChange  < 0)):
            continue
        if ((oneChange + rgb[(two + 2) % 3] > 255) or (rgb[(two + 2) % 3] - oneChange  < 0)):
            continue
        rgb[two] += twoChange
        rgb[(two + 1) % 3] += sign * scale
        rgb[(two + 2) % 3] += sign * scale
        break
    if counter == 0:
        print('warning:#%02x%02x%02x' % tuple(rgb))
    for color in colors:
        color.replaceWholeText(rgb_to_hex(rgb))
    return

class AutoRecolorer(sublime_plugin.TextCommand):
    def run(self, edit):
        path = currentScheme
        dom = parse(path)
        array = dom.childNodes[2].childNodes[1].childNodes[11]
        
        #comment
        change ([array.childNodes[3].childNodes[11].childNodes[7].childNodes[0]]) 
        #keyword
        change ([array.childNodes[7].childNodes[11].childNodes[7].childNodes[0], array.childNodes[19].childNodes[11].childNodes[7].childNodes[0], array.childNodes[21].childNodes[11].childNodes[7].childNodes[0], array.childNodes[39].childNodes[11].childNodes[7].childNodes[0]])
        #numeric
        change ([array.childNodes[15].childNodes[11].childNodes[7].childNodes[0], array.childNodes[53].childNodes[11].childNodes[7].childNodes[0]])
        #user defined constant
        change ([array.childNodes[17].childNodes[11].childNodes[7].childNodes[0]])
        #string
        change ([array.childNodes[23].childNodes[11].childNodes[7].childNodes[0]])
        #string interpolation
        change ([array.childNodes[25].childNodes[11].childNodes[7].childNodes[0]])
        #type
        change ([array.childNodes[33].childNodes[11].childNodes[7].childNodes[0], array.childNodes[35].childNodes[11].childNodes[7].childNodes[0], array.childNodes[37].childNodes[11].childNodes[7].childNodes[0], array.childNodes[41].childNodes[11].childNodes[7].childNodes[0], array.childNodes[51].childNodes[11].childNodes[7].childNodes[0]])
        
        f = open(path, 'w')
        dom.writexml(f)
        f.close()

class AutoRecolorerReset(sublime_plugin.TextCommand):
    def run(self, edit):
        shutil.copyfile(defaultScheme, currentScheme)

class AutoRecolorerNightModeToggle(sublime_plugin.TextCommand):
    def run(self, edit):
        path = currentScheme
        #todo - make a night mode toggle
        #dom = parse(path)
        #array = dom.childNodes[2].childNodes[1].childNodes[11]