import json
import string
import re



out = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/correct_syn_scenegraph1.json', 'w')
scenes_file = "/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/out_scenegraph1.json"

def format_obj_syn():
     # put the path of the file
    with open(scenes_file) as f:
        scenegraph = json.load(f)
        for jsonObj in scenegraph:
            for obj in jsonObj['objects']:
                for syn in obj['synsets']:
                    for v in syn:
                        # These replace numbers with "0" before in numbers without
                        obj['synsets'] = str(obj['synsets']).replace("01", "1")
                        obj['synsets'] = str(obj['synsets']).replace("02", "2")
                        obj['synsets'] = str(obj['synsets']).replace("03", "3")
                        obj['synsets'] = str(obj['synsets']).replace("04", "4")
                        obj['synsets'] = str(obj['synsets']).replace("05", "5")
                        obj['synsets'] = str(obj['synsets']).replace("06", "6")
                        obj['synsets'] = str(obj['synsets']).replace("07", "7")
                        obj['synsets'] = str(obj['synsets']).replace("08", "8")
                        obj['synsets'] = str(obj['synsets']).replace("09", "9")
                        # This lowercase all the synsets (some of them are in caps lock for no reason)
                        obj['synsets'] = str(obj['synsets']).lower()
                        # These replace the squared brackets and the apostrophe
                        obj['synsets'] = str(obj['synsets']).replace('[', '')
                        obj['synsets'] = str(obj['synsets']).replace(']', '')
                        obj['synsets'] = str(obj['synsets']).replace("'", "")
                        # This capitalize only the first character of the string
                        obj['synsets'] = string.capwords(obj['synsets'])
                        # Honestly? I don't remember what this was for, it was used in the frame extraction pipeline
                        obj['synsets'] = re.sub(r"\([^()]*\)", "", obj['synsets'])
            # Finally we dump everything in the main file           
        json.dump(scenegraph, out)


format_obj_syn()