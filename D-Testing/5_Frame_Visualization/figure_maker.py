import json
from PIL import Image, ImageDraw

def draw_boxes(image_id, frame_file_path, box_file_path):
    image_path = "image_scrapping/KG_v1/images/" + image_id + ".jpg"
    # Load the image
    image = Image.open(image_path)

    # Load the JSON files
    with open(frame_file_path, 'r') as f:
        frame_data = json.load(f)
    with open(box_file_path, 'r') as f:
        box_data = json.load(f)

    # Create a new image with the same size as the original
    new_image = Image.new('RGBA', image.size, (0, 0, 0, 0))

    # Draw the boxes and labels on the new image
    draw = ImageDraw.Draw(new_image)
    for image_data in box_data:
        if image_data["image_id"] == frame_data["images"][0]["image_id"]:

            for box_region in image_data['regions']:
                for frame_region in frame_data["images"][0]["regions"]:
                    if frame_region['region_id'] == box_region['region_id']:
                        print("found a match")
                        x = box_region['x']
                        y = box_region['y']
                        w = box_region['width']
                        h = box_region['height']
                        frames = frame_region['frames']
                        box = (x, y, x + w, y + h)
                        draw.rectangle(box, outline='purple')


                        for frame in frames:
                            text_size = draw.textsize(frame)
                            # Calculate the position of the text
                            text_x = box[0]
                            text_y = box[1]
                            text_box = (text_x - 2, text_y - 2, text_x + text_size[0] + 2, text_y + text_size[1] + 2)

                            # Check if the text box goes beyond the image bounds and adjust its position
                            if text_box[0] < 0:
                                text_x = max(text_x - text_box[0], 0)
                                text_box = (
                                text_x - 2, text_y - 2, text_x + text_size[0] + 2, text_y + text_size[1] + 2)
                            if text_box[1] < 0:
                                text_y = max(text_y - text_box[1], 0)
                                text_box = (
                                text_x - 2, text_y - 2, text_x + text_size[0] + 2, text_y + text_size[1] + 2)
                            if text_box[2] > image.width:
                                text_x = max(text_x - (text_box[2] - image.width), 0)
                                text_box = (
                                text_x - 2, text_y - 2, text_x + text_size[0] + 2, text_y + text_size[1] + 2)
                            if text_box[3] > image.height:
                                text_y = max(text_y - (text_box[3] - image.height), 0)
                                text_box = (
                                text_x - 2, text_y - 2, text_x + text_size[0] + 2, text_y + text_size[1] + 2)

                            # Draw the text
                            draw.rectangle(text_box, fill='white')

                            draw.text((text_x, text_y), frame, fill='purple')

    # Merge the new image with the original
    result = Image.alpha_composite(image.convert('RGBA'), new_image)

    # Convert the image to RGB mode
    result = result.convert('RGB')

    # Save the result
    result.save('result.jpg')
    return

image_id = "2411415"
frame_file_path = image_id + "_draw.json"
box_file_path = "../4_KG_Generation/sources/region_graphs.json"
draw_boxes(image_id, frame_file_path, box_file_path)
