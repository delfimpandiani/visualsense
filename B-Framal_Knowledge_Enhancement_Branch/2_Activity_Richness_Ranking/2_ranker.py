import json
import nltk
from nltk import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def frequency_rank(split_name):
    f_verbal_imgs_ranked = {}
    verbal_imgs_path = 'VG_data/VG_data_verbal_imgs/' + split_name + "_verbal_images.json"
    ranked_verbal_imgs_path = 'VG_data/VG_data_ranked/frequency_ranked/' + split_name + "_verbal_images_ranked_f.json"
    with open(verbal_imgs_path) as f:
        verbal_imgs = json.load(f)
        verbal_imgs_sorted = sorted(verbal_imgs.items(), key=lambda x:x[1], reverse=True)
        for img_id, occurr_numb in verbal_imgs_sorted:
            f_verbal_imgs_ranked.setdefault(img_id, []).append(occurr_numb)
    with open(ranked_verbal_imgs_path, 'w') as ranked_verbal_imgs:
        json.dump(f_verbal_imgs_ranked, ranked_verbal_imgs)
    print(f_verbal_imgs_ranked)
    return f_verbal_imgs_ranked

def verbal_variance_detector(split_name):
    verbal_detections = {}
    split_path = 'VG_data/VG_data_splits/' + split_name + "_scenegraph.json"
    verbal_detections_imgs_path = 'VG_data/VG_data_ranked/verbal_detections/' + split_name + "_verbal_detections_v.json"
    with open(verbal_detections_imgs_path, 'w') as ranked_verbal_imgs:
        with open(split_path) as f:
            split = json.load(f)
            for image in split:
                for rel in image['relationships']:
                    preds = rel["predicate"]
                    if isinstance(preds, str):
                        preds = preds.lower()
                        tok = word_tokenize(preds)
                        verbs = nltk.pos_tag(tok)
                        for s in verbs:
                            if s[1] in ('VB' ,'VBD' ,'VBG' ,'VBN' ,'VBP' ,'VBZ'):
                                if '.r.' not in rel['synsets']:
                                    if len(rel['synsets']) > 0:
                                        verbal_detections.setdefault(image['image_id'], []).append(rel['synsets'][0])
        json.dump(verbal_detections, ranked_verbal_imgs)
    return verbal_detections

def variance_rank(split_name):
    vv_verbal_imgs_ranked = {}
    d1 = {}
    d2 = {}
    ranked_verbal_imgs_path = 'VG_data/VG_data_ranked/verb_variance_ranked/' + split_name + "_verbal_images_ranked_v.json"
    verbal_detections = verbal_variance_detector(split_name)
    for k, v in verbal_detections.items():
        # create a new dict with unique values
        d1[k] = list(set(v))
        # create another dict taking as value the length of the list of unique values
        d2[k] = len(list(set(v)))
        # create a final dict in which items are sorted by the number of items in each list of values
        unique_list = sorted(d2.items(), key=lambda x: x[1], reverse=True)
        for x in unique_list:
            vv_verbal_imgs_ranked.setdefault(x[0], x[1])
    new_vv_verbal_imgs_ranked = {}
    ranked = sorted(vv_verbal_imgs_ranked.items(), key=lambda x:x[1], reverse=True)
    for img_id, occurr_numb in ranked:
        new_vv_verbal_imgs_ranked.setdefault(img_id, []).append(occurr_numb)
    with open(ranked_verbal_imgs_path, 'w') as ranked_verbal_imgs:
        json.dump(new_vv_verbal_imgs_ranked, ranked_verbal_imgs)
    print(new_vv_verbal_imgs_ranked)
    return new_vv_verbal_imgs_ranked

def composite_rank(split_name):
    composite_ranked_verbal_imgs_path = 'VG_data/VG_data_ranked/composite_ranked/' + split_name + "_verbal_images_ranked_c.json"

    frequency_scores = 'VG_data/VG_data_ranked/frequency_ranked/' + split_name + "_verbal_images_ranked.json"
    variance_scores = 'VG_data/VG_data_ranked/verb_variance_ranked/' + split_name + "_verbal_images_ranked_v.json"
    with open(frequency_scores, 'r') as f:
        scores_dim1 = json.load(f)
        scores_dim1 = {k: v[0] for k, v in scores_dim1.items()}
    with open(variance_scores, 'r') as f:
        scores_dim2 = json.load(f)
        scores_dim2 = {k: v[0] for k, v in scores_dim2.items()}

    common_image_ids = set(scores_dim1.keys()) & set(scores_dim2.keys())
    scores_dim1 = {k: v for k, v in scores_dim1.items() if k in common_image_ids}
    scores_dim1 = {k: v for k, v in scores_dim1.items() if k in common_image_ids}

    # compute the normalized scores for each dimension
    max_dim1 = max(scores_dim1.values())
    min_dim1 = min(scores_dim1.values())
    max_dim2 = max(scores_dim2.values())
    min_dim2 = min(scores_dim2.values())
    normalized_scores = {img_id: [(scores_dim1[img_id] - min_dim1) / (max_dim1 - min_dim1),
                                  (scores_dim2[img_id] - min_dim2) / (max_dim2 - min_dim2)] for img_id in scores_dim1}

    # compute the rankings on each dimension
    rankings_dim1 = sorted(scores_dim1.keys(), key=lambda x: scores_dim1[x], reverse=True)
    rankings_dim2 = sorted(scores_dim2.keys(), key=lambda x: scores_dim2[x], reverse=True)

    # compute the weighted average of the rankings
    weight = 0.5  # equal weight for both dimensions
    final_rankings = [(weight * rankings_dim1.index(img_id) + (1 - weight) * rankings_dim2.index(img_id), img_id) for
                      img_id in normalized_scores]
    final_rankings = sorted(final_rankings)

    # compute the minimum and maximum ranks
    min_rank = min(rank for rank, img_id in final_rankings)
    max_rank = max(rank for rank, img_id in final_rankings)

    # scale the final rankings between 0 and 100
    scaled_final_rankings = [(100 * (rank - min_rank) / (max_rank - min_rank), img_id) for rank, img_id in
                             final_rankings]
    scaled_final_rankings = sorted(scaled_final_rankings)

    # print the final rankings
    for rank, img_id in scaled_final_rankings:
        print(f"Image {img_id} has final ranking of {rank}")

    with open(composite_ranked_verbal_imgs_path, 'w') as composite_ranked_verbal_imgs:
        json.dump(scaled_final_rankings, composite_ranked_verbal_imgs)
    print(scaled_final_rankings)
    return scaled_final_rankings


#########################################################
####################### Execution #######################
#########################################################
# composite_rank("split2")
