import json


source = '/home/sdg/Desktop/VG/interesting_images.json'
out = open('/home/sdg/Desktop/VG/quant_ranked_rel_split1.json', 'w')
ranked_img = dict()


def img_rank(file):
    with open(file) as f:
        imgs = json.load(f)
        imgs_sorted = sorted(imgs.items(), key=lambda x:x[1], reverse=True)
#        print(imgs_sorted)
        for img_id, occurr_numb in imgs_sorted:
            ranked_img.setdefault(img_id, []).append(occurr_numb)
    json.dump(ranked_img, out)
    print(ranked_img)

img_rank(source)