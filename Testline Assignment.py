import os
from google.cloud import vision
import io
import cv2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "path/to/your/service_account_key.json"
client = vision.ImageAnnotatorClient()


def analyze_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    return texts


def segment_visual_elements(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    visual_elements = []

    image_dir = 'visual_elements'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        visual_element = image[y:y+h, x:x+w]
        img_path = os.path.join(image_dir, f'visual_element_{i}.png')
        cv2.imwrite(img_path, visual_element)
        visual_elements.append((x, y, w, h, img_path))

    return visual_elements


def create_html(texts, visual_elements, output_path='output.html'):
    html_content = "<html><body>\n"

    images_html = ""

    # Add images to HTML
    for i, (x, y, w, h, img_path) in enumerate(visual_elements):
        images_html += f"<div style='position:relative;'>\n"
        images_html += f"  <img src='{img_path}' style='position:absolute; left:{x}px; top:{y}px; width:{w}px; height:{h}px;'>\n"
        images_html += "</div>\n"

    # Full paragraph text 
    full_text_html = f"<p>{texts[0].description}</p>" if texts else ""

    html_content += images_html + "\n" + full_text_html
    html_content += "</body></html>"

    with open(output_path, 'w') as html_file:
        html_file.write(html_content)


# Example usage
image_path = input("Enter the complete file path, make sure to add double slashes '/': " )
texts = analyze_image(image_path)
visual_elements = segment_visual_elements(image_path)
create_html(texts, visual_elements)