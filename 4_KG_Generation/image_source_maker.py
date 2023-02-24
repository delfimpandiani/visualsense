import json
import csv

def get_frame_source(image_ids_list, split_name):
    out_path = 'sources/frames.json'
    # Initialize an empty list to store the frames
    frames_evoked = []
    for image_id in image_ids_list:
        tsv_file_path = str('../3_Framal_Knowledge_Extraction/knowledge_extraction_outputs/' + split_name + '/image_tsvs/img_' + image_id + '.tsv')
        # Open the TSV file
        with open(tsv_file_path, newline='') as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter='\t')
            # Loop through each row in the TSV file
            for row in reader:
                # Split the Emotions and Emotions Triggers columns by comma and strip whitespace
                emotions = [e.strip() for e in row['Emotions'].split(',')]
                # emotions_triggers = [et.strip() for et in row['Emotions Triggers'].split(',')]

                # Split the Values and Values Triggers columns by comma and strip whitespace
                values = [v.strip() for v in row['Values'].split(',')]
                # values_triggers = [vt.strip() for vt in row['Values Triggers'].split(',')]

                # Split the Frames column by comma and strip whitespace
                frames = [f.strip() for f in row['Frames'].split(',')]

                # Loop through each frame and append it to the frames_evoked list
                for emotion in emotions:
                    if emotion != '':
                        frames_evoked.append({
                            'frame': emotion,
                            'type': 'emotion',
                            'image_id': int(row['image_id']),
                            'region_id': int(row['region_id'])
                        })

                for value in values:
                    if value != '':
                        frames_evoked.append({
                            'frame': value,
                            'type': 'value',
                            'image_id': int(row['image_id']),
                            'region_id': int(row['region_id'])
                        })

                for frame in frames:
                    if frame != '':
                        frames_evoked.append({
                            'frame': frame,
                            'type': 'frame',
                            'image_id': int(row['image_id']),
                            'region_id': int(row['region_id'])
                        })

    # Create a dictionary with the frames_evoked list as the value

    # Write the dictionary to a JSON file
    with open(out_path, 'w') as jsonfile:
        json.dump(frames_evoked, jsonfile, indent=4)
    return frames_evoked

def get_image_source(image_ids_list, source_type):
    full_source_path = '../VG_data/' + source_type + '.json'
    out_path = open('sources/' + source_type + '.json', 'w')
    source_list = []
    for image_id in image_ids_list:
        try:
            with open(full_source_path) as f:
                data = json.load(f)
                for image in data:
                    if image['image_id'] == int(image_id):
                        source_list.append(image)
        except FileNotFoundError:
            print(f"Error: File '{full_source_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")
        except:
            print('error')
    json.dump(source_list, out_path, indent=4)
    return source_list

def get_all_image_sources(image_ids_list, split_name):
    image_data = get_image_source(image_ids_list, 'image_data')
    region_graphs = get_image_source(image_ids_list, 'region_graphs')
    scene_graphs = get_image_source(image_ids_list, 'scene_graphs')
    frame_data = get_frame_source(image_ids_list, split_name)
    return image_data, region_graphs, scene_graphs, frame_data

def load_data():
    with open('sources/scene_graphs.json', 'r') as scene_graphs:
        source_scene_graphs = json.load(scene_graphs)

    with open('sources/region_graphs.json', 'r') as region_graphs:
        source_region_graphs = json.load(region_graphs)

    with open('sources/frames.json', 'r') as frames:
        source_frame_data = json.load(frames)

    with open('sources/image_data.json', 'r') as image_data:
        source_image_data = json.load(image_data)

    return source_image_data, source_region_graphs, source_scene_graphs, source_frame_data