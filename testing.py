import numpy as np
from handwriting_synthesis import Hand

def FormatDataToSVG(data):
    result = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>" # Very dirty way of getting the correct xml document from the tree structure returned
    for child in data:
        if child.tag == "defs":
            pass
        elif child.tag == "rect":
            child.attrib.get("width")
            result += "<svg baseProfile=\"full\" height=\"100%\" version=\"1.1\" viewBox=\"0,0," + str(child.attrib["width"]) + "," + str(child.attrib["height"]) + "\" width=\"100%\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:ev=\"http://www.w3.org/2001/xml-events\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"><defs />"
        else:
            result += "<" + str(child.tag) + " " + stringifyDictionary(child.attrib) + "/>"
    result += "</svg>"
    return result


def stringifyDictionary(dictionaryInput = dict[str,str]):
    """"Formats the dictionary to be the correct input for the svg format"""
    result = ""
    for k, v in dictionaryInput.items():
        result += k + "=\"" + v + "\" "
    return result


if __name__ == '__main__':
    hand = Hand()

    lines = """Anton was here
    What will happen to this line.
    Maybe a something weird who knows
    MVH. Anton Harneby"""


    lines = """"Anton was here
    This is another line of text"""
    lines = lines.split("\n")
    biases = [.75 for i in lines]
    styles = [12 for i in lines]

    hand.write(
        filename='img/test temp.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )
    xml = hand.getXML(lines = lines, biases = biases, styles = styles)
    result = FormatDataToSVG(xml)
    print(result)

