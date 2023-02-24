import os
import urllib
import json
from datetime import time
import requests
import json
from PIL import Image, ImageDraw


def get_v1_imgs_list(split_name):
    top_images_path = '../VG_data/VG_data_ranked/composite_ranked/split2_verbal_images_ranked_c.json'
    image_ids_list = []
    with open(top_images_path, 'r') as f:
        # Load the list from the file
        original_list = json.load(f)
    new_list = [sublist[1] for sublist in original_list]
    for image_id in new_list:
        file_path = '../3_Framal_Knowledge_Extraction/knowledge_extraction_outputs/' + split_name + '/image_tsvs/' + 'img_' + image_id + '.tsv'
        if os.path.isfile(file_path):
            image_ids_list.append(image_id)
    print(image_ids_list)
    return image_ids_list

def mine_KG_v1_imgs(split_name):
    image_ids_list = get_v1_imgs_list(split_name)
    if not os.path.exists("KG_v1/images"):
        os.mkdir("KG_v1/images")
    directory = "KG_v1/images"
    failed = []
    succeed = []
    for img_id in image_ids_list:
        new_name = "" + img_id +".jpg"
        image_url = "https://cs.stanford.edu/people/rak248/VG_100K_2/" + new_name
        new_path = os.path.join(directory, new_name)
        if os.path.exists(new_path):
            succeed.append(img_id)
        else:
            response = requests.get(image_url)
            with open(new_path, 'wb') as f:
                f.write(response.content)

            # # for downloading images directly from url
            # try:
            #     urllib.request.urlretrieve(image_url, new_path)
            #     succeed.append(img_id)
            # except:
            #     try:
            #         print("sleeping for a sec to make another request for", image_url)
            #         time.sleep(10)
            #         urllib.request.urlretrieve(image_url, new_path)
            #         succeed.append(img_id)
            #     except:
            #         print("could not find", image_url)
            #         failed.append(img_id)
            #         continue

    # print("For dataset", dataset_name, "SUCCEEDED", succeed)
    print("NUMBER SUCCEEDED", len(succeed))
    # print("For dataset", dataset_name, "FAILED", failed)
    print("NUMBER FAILED", len(failed))
    return

def draw_boxes(image_path, json_file_path):
    # Load the image
    image = Image.open(image_path)

    # Load the JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Create a new image with the same size as the original
    new_image = Image.new('RGBA', image.size, (0, 0, 0, 0))

    # Draw the boxes on the new image
    draw = ImageDraw.Draw(new_image)
    for label in data:
        x, y, w, h = label['box']
        box = (x, y, x + w, y + h)
        draw.rectangle(box, outline='red')
        draw.text((box[0], box[1]), label['label'], fill='red')

    # Merge the new image with the original
    result = Image.alpha_composite(image.convert('RGBA'), new_image)

    # Save the result
    result.save('result.jpg')




mine_KG_v1_imgs('split2')

directory = "KG_v1/images"
for image in directory:
    draw_boxes(image_path)
