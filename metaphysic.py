from PIL import Image, ImageDraw, ImageFont
import sys
import re
from collections import defaultdict

element_map = {
    'metal': [1, 6],
    'water': [2, 7],
    'fire': [3, 8],
    'wood': [4, 9],
    'earth': [5]
}


def single_digit_sum(num1, num2):
    result = num1 + num2
    if result > 9:
        result = sum(map(int, str(result)))
    return result


def get_element_color(number):
    metal = '#2b2d42'
    water = '#0077b6'
    fire = '#f25c54'
    wood = '#57a773'
    earth = '#bc6c25'
    elements = {
        1: metal,
        2: water,
        3: fire,
        4: wood,
        5: earth,
        6: metal,
        7: water,
        8: fire,
        9: wood
    }
    return elements.get(number, "Invalid input")


def get_element_number(name: str):
    name = name.lower()
    array_element = element_map.get(name)
    return array_element[0]


def calculate_number_element(array):
    element_count = {key: 0 for key in element_map.keys()}
    for num in array:
        for element, range_ in element_map.items():
            if num in range_:
                element_count[element] += 1

    return element_count


def sort_number_to_star_array(input_array):
    star_number_array = [0] * 17

    # Sort number into star array
    star_number_array[0] = single_digit_sum(
        int(input_array[0]), int(input_array[1]))
    star_number_array[1] = single_digit_sum(
        int(input_array[2]), int(input_array[3]))
    star_number_array[2] = single_digit_sum(
        int(input_array[4]), int(input_array[5]))
    star_number_array[3] = single_digit_sum(
        int(input_array[6]), int(input_array[7]))
    star_number_array[4] = single_digit_sum(
        star_number_array[1], star_number_array[2])
    star_number_array[5] = single_digit_sum(
        star_number_array[0], star_number_array[1])
    star_number_array[6] = single_digit_sum(
        star_number_array[1], star_number_array[5])
    star_number_array[7] = single_digit_sum(
        star_number_array[0], star_number_array[5])
    star_number_array[8] = single_digit_sum(
        star_number_array[7], star_number_array[6])
    star_number_array[9] = single_digit_sum(
        star_number_array[2], star_number_array[3])
    star_number_array[10] = single_digit_sum(
        star_number_array[2], star_number_array[9])
    star_number_array[11] = single_digit_sum(
        star_number_array[3], star_number_array[9])
    star_number_array[12] = single_digit_sum(
        star_number_array[10], star_number_array[11])
    star_number_array[13] = single_digit_sum(
        star_number_array[5], star_number_array[9])
    star_number_array[14] = single_digit_sum(
        star_number_array[9], star_number_array[13])
    star_number_array[15] = single_digit_sum(
        star_number_array[5], star_number_array[13])
    star_number_array[16] = single_digit_sum(
        star_number_array[14], star_number_array[15])
    return star_number_array


def begin_drawing(input, input_array, isWeb=False):
    star_number_array = [0] * 17

    # Sort number into star array
    star_number_array[0] = single_digit_sum(
        int(input_array[0]), int(input_array[1]))
    star_number_array[1] = single_digit_sum(
        int(input_array[2]), int(input_array[3]))
    star_number_array[2] = single_digit_sum(
        int(input_array[4]), int(input_array[5]))
    star_number_array[3] = single_digit_sum(
        int(input_array[6]), int(input_array[7]))
    star_number_array[4] = single_digit_sum(
        star_number_array[1], star_number_array[2])
    star_number_array[5] = single_digit_sum(
        star_number_array[0], star_number_array[1])
    star_number_array[6] = single_digit_sum(
        star_number_array[1], star_number_array[5])
    star_number_array[7] = single_digit_sum(
        star_number_array[0], star_number_array[5])
    star_number_array[8] = single_digit_sum(
        star_number_array[7], star_number_array[6])
    star_number_array[9] = single_digit_sum(
        star_number_array[2], star_number_array[3])
    star_number_array[10] = single_digit_sum(
        star_number_array[2], star_number_array[9])
    star_number_array[11] = single_digit_sum(
        star_number_array[3], star_number_array[9])
    star_number_array[12] = single_digit_sum(
        star_number_array[10], star_number_array[11])
    star_number_array[13] = single_digit_sum(
        star_number_array[5], star_number_array[9])
    star_number_array[14] = single_digit_sum(
        star_number_array[9], star_number_array[13])
    star_number_array[15] = single_digit_sum(
        star_number_array[5], star_number_array[13])
    star_number_array[16] = single_digit_sum(
        star_number_array[14], star_number_array[15])

    # Open the image
    templateFile = "star_template_web.png" if isWeb else "star_template.png"
    img = Image.open(templateFile)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(img)

    # Define the font and text
    font = ImageFont.truetype("Raleway-Regular.ttf", 36)
    fontElement = ImageFont.truetype("Raleway-Regular.ttf", 20)

    # Draw the number inside star
    draw.text((145, 128), str(star_number_array[0]), font=font,
              fill=get_element_color(star_number_array[0]), anchor="mm")
    draw.text((212, 142), str(star_number_array[1]), font=font,
              fill=get_element_color(star_number_array[1]), anchor="mm")
    draw.text((285, 142), str(star_number_array[2]), font=font,
              fill=get_element_color(star_number_array[2]), anchor="mm")
    draw.text((350, 126), str(star_number_array[3]), font=font,
              fill=get_element_color(star_number_array[3]), anchor="mm")
    draw.text((250, 62),  str(star_number_array[4]), font=font,
              fill=get_element_color(star_number_array[4]), anchor="mm")
    draw.text((210, 220), str(star_number_array[5]), font=font,
              fill=get_element_color(star_number_array[5]), anchor="mm")
    draw.text((145, 245), str(star_number_array[6]), font=font,
              fill=get_element_color(star_number_array[6]), anchor="mm")
    draw.text((101, 210), str(star_number_array[7]), font=font,
              fill=get_element_color(star_number_array[7]), anchor="mm")
    draw.text((101, 165), str(star_number_array[8]), font=font,
              fill=get_element_color(star_number_array[8]), anchor="mm")
    draw.text((285, 220), str(star_number_array[9]), font=font,
              fill=get_element_color(star_number_array[9]), anchor="mm")
    draw.text((350, 245), str(star_number_array[10]), font=font,
              fill=get_element_color(star_number_array[10]), anchor="mm")
    draw.text((395, 210), str(star_number_array[11]), font=font,
              fill=get_element_color(star_number_array[11]), anchor="mm")
    draw.text((395, 165), str(star_number_array[12]), font=font,
              fill=get_element_color(star_number_array[12]), anchor="mm")
    draw.text((250, 305), str(star_number_array[13]), font=font,
              fill=get_element_color(star_number_array[13]), anchor="mm")
    draw.text((195, 353), str(star_number_array[14]), font=font,
              fill=get_element_color(star_number_array[14]), anchor="mm")
    draw.text((305, 354), str(star_number_array[15]), font=font,
              fill=get_element_color(star_number_array[15]), anchor="mm")
    draw.text((250, 406), str(star_number_array[16]), font=font,
              fill=get_element_color(star_number_array[16]), anchor="mm")

    if (not isWeb):
        # Draw total number of element
        counted_element = calculate_number_element(star_number_array)
        draw.text((50, 450), 'Metal x'+str(counted_element['metal']), font=fontElement,
                  fill='black', anchor="mm")
        draw.text((50, 480), 'Water x'+str(counted_element['water']), font=fontElement,
                  fill='black', anchor="mm")
        draw.text((50, 510), 'Fire x'+str(counted_element['fire']), font=fontElement,
                  fill='black', anchor="mm")
        draw.text((50, 540), 'Wood x'+str(counted_element['wood']), font=fontElement,
                  fill='black', anchor="mm")
        draw.text((50, 570), 'Earth x'+str(counted_element['earth']), font=fontElement,
                  fill='black', anchor="mm")

        # Draw type of number
        draw.text((250, 480), 'Spirit: '+str(star_number_array[4]), font=fontElement,
                  fill='black', anchor="mm")
        draw.text((250, 510), 'Physical: '+str(star_number_array[13]), font=fontElement,
                  fill='black', anchor="mm")
        draw.text((250, 540), 'Ending: '+str(star_number_array[16]), font=fontElement,
                  fill='black', anchor="mm")

    # Draw type of number
    draw.text((357, 66), 'Spirit Number', font=fontElement,
              fill='black', anchor="mm")
    draw.text((377, 307), 'Physical Number', font=fontElement,
              fill='black', anchor="mm")
    draw.text((350, 406), 'Ending Number', font=fontElement,
              fill='black', anchor="mm")

    # Save the image
    filename = f'result_{input}.png'
    img.save(filename)
    return filename


def check_input(input_string):
    date_regex = re.compile(
        r'^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[012])(19|20)\d\d$')
    if date_regex.match(input_string):
        return True
    else:
        return False


def get_input(input):
    if len(input) < 3:
        print("Error: Not enough arguments passed.")
        print("Usage: python metaphysic.py ddmmyyyy try something like 31121992")
        sys.exit()

    if check_input(input):
        input_array = list(map(str, input))
        if input[4:8] == "2000":
            input_array[4:8] = list("2005")
        begin_drawing(input, input_array)
    else:
        print("Error: Input is not a valid DOB.")
        print("Usage: python metaphysic.py ddmmyyyy try something like 31121992")


def analysis(input):
    input_array = list(map(str, input))
    if input[4:8] == "2000":
        input_array[4:8] = list("2005")
    sorted_array = sort_number_to_star_array(input_array)

    # Find Physical,Spirit,Ending number
    physical = sorted_array[13]
    spirit = sorted_array[4]
    ending = sorted_array[16]

    # Map with knowledge based
    physical = knowledge_base['Physical'][physical]
    spirit = knowledge_base['Physical'][spirit]
    ending = knowledge_base['Ending'][ending]

    # Find dominant element
    element_counts = defaultdict(int)
    for item in sorted_array:
        for element, element_values in element_map.items():
            if item in element_values:
                element_counts[element] += 1
    dominant_elements = {element: count for element,
                         count in element_counts.items() if count > 4}
    if dominant_elements:
        return [dominant_elements, physical, spirit, ending]
    else:
        dominant_elements = {element: count for element,
                             count in element_counts.items() if count == 4}
        if dominant_elements:
            return [dominant_elements, physical, spirit, ending]
        else:
            return [{}, physical, spirit, ending]


def get_element_analysis(element,count):
    element = element.capitalize()
    if element in knowledge_base:
        return {
            'name': element,
            'count': count,
            'color': get_element_color(get_element_number(element)),
            'personality': knowledge_base[element]['Personality'],
            'strength_and_weakness': knowledge_base[element]['Strength & Weakness'],
            'compatibility': knowledge_base[element]['Compatibility'],
            'relationship': knowledge_base[element]['Relationship'],
            'advice': knowledge_base[element]['Advice'],
        }
    else:
        print("Element not found in the knowledge base.")


# Knowledge Base Section
knowledge_base = {
    'Wood': {
        'Compatibility': 'compatible with Fire and Earth, but can conflict with Metal and Water',
        'Personality': 'optimistic, confident, and energetic',
        'Strength & Weakness': 'Strength: creativity, leadership, and determination. Weakness: impulsiveness, impatience, and inflexibility',
        'Relationship': 'Encourage growth, independence, and exploration. Be supportive and understanding of their need for change.',
        'Advice': 'Emphasize the importance of finding balance between creativity and stability, and encourage them to be patient and considerate in their decisions.'
    },
    'Fire': {
        'Compatibility': 'compatible with Wood and Earth, but can conflict with Metal and Water',
        'Personality': 'passionate, confident, and charismatic',
        'Strength & Weakness': 'Strength: passion, energy, and confidence. Weakness: impulsiveness, hot-headedness, and a tendency to be too dramatic',
        'Relationship': 'Be passionate and energetic, and be open to new experiences. Keep the relationship lively and spontaneous.',
        'Advice': 'Emphasize the importance of finding balance between passion and practicality, and encourage them to think before acting impulsively.'
    },
    'Earth': {
        'Compatibility': 'compatible with Metal and Water, but can conflict with Wood and Fire',
        'Personality': 'practical, reliable, and stable',
        'Strength & Weakness': 'Strength: stability, reliability, and practicality. Weakness: rigidity, inflexibility, and a tendency to be overly attached to material possessions',
        'Relationship': 'Provide stability, security, and practicality. Be reliable and dependable, and show appreciation for their material contributions.',
        'Advice': 'Emphasize the importance of finding balance between stability and change, and encourage them to be open to new experiences.'
    },
    'Metal': {
        'Compatibility': 'compatible with Earth and Water, but can conflict with Wood and Fire',
        'Personality': 'strong-willed, disciplined, and detail-oriented',
        'Strength & Weakness': 'Strength: discipline, strength of will, and focus. Weakness: inflexibility, stubbornness, and a tendency to be overly controlling',
        'Relationship': 'Be disciplined and focused, and appreciate their attention to detail. Be supportive of their goals and aspirations.',
        'Advice': 'Emphasize the importance of finding balance between discipline and flexibility, and encourage them to be more open-minded and considerate of others.'
    },
    'Water': {
        'Compatibility': 'compatible with Metal and Earth, but can conflict with Wood and Fire',
        'Personality': 'intuitive, emotional, and adaptable',
        'Strength & Weakness': 'Strength: adaptability, intuition, and empathy. Weakness: indecisiveness, emotional instability, and a tendency to be overly passive',
        'Relationship': 'Be flexible and adaptable, and provide emotional support. Be understanding and empathetic, and allow for open communication.',
        'Advice': 'Emphasize the importance of finding balance between intuition and rational thinking, and encourage them to be more assertive and confident in their decisions.'
    },
    'Physical': {
        1: 'A wise leader is someone who is good at understanding people, has a lot of good ideas and is very creative.',
        2: 'An honest person is truthful, has high moral standards and is soft-spoken. They listen to others but they dont always follow what they hear.',
        3: 'A person who is charming when young may get things done quickly, but their work is not always perfect. They can be impulsive and sometimes act aggressively. They may not always make strong decisions and their relationships can be unstable.',
        4: 'Someone who is highly skilled and wise doesnt give up easily, but they may have trouble saving money. Their relationships can also be unstable and fall apart easily.',
        5: 'A leader is someone who works very hard, holds a high position, and has a strong determination, even if others disagree.',
        6: 'This person wants to be in control of their finances, enjoys a lavish lifestyle, is self-sufficient, and has a desire to be in charge of situations.',
        7: 'This person is known for starting arguments, being very particular, having many friends and fans, and having the ability to attract people to support them.',
        8: 'This person takes their responsibilities seriously, is quiet but has many friends, is known for being reliable, and always stands up for their friends.',
        9: 'This person is skilled at managing their public image, takes good care of their appearance, is able to impress old generation, but feels lonely at times.'
    },
    'Ending': {
        3: 'The final outcome for this person is either extreme wealth or extreme poverty.',
        6: 'The ultimate result for this person is a higher amount of liquid assets.',
        9: 'The final result for this person is a higher amount of fixed assets.',
    }
}

if __name__ == "__main__":
    get_input(sys.argv[1])
