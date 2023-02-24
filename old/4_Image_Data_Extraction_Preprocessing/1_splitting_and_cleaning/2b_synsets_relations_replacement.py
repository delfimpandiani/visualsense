import json
import re
import string


out = open('/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/correct_syn_scenegraph1.json', 'w')
scenes_file = "/media/sten-doipanni/Mattonella Rossa/backups/backup_asus_23_07_2021/Desktop/VG/out_scenegraph1.json"

def format_rel_syns():
    # put the path of the file
    with open(scenes_file) as f:
        scenegraph = json.load(f)
        for jsonObj in scenegraph:
            for rel in jsonObj['relationships']:
                for syn in rel['synsets']:
                    # These replace numbers with "0" before in numbers without
                    rel['synsets'] = str(rel['synsets']).replace("01", "1")
                    rel['synsets'] = str(rel['synsets']).replace("02", "2")
                    rel['synsets'] = str(rel['synsets']).replace("03", "3")
                    rel['synsets'] = str(rel['synsets']).replace("04", "4")
                    rel['synsets'] = str(rel['synsets']).replace("05", "5")
                    rel['synsets'] = str(rel['synsets']).replace("06", "6")
                    rel['synsets'] = str(rel['synsets']).replace("07", "7")
                    rel['synsets'] = str(rel['synsets']).replace("08", "8")
                    rel['synsets'] = str(rel['synsets']).replace("09", "9")
                    # This lowercase all the synsets (some of them are in caps lock for no reason)
                    rel['synsets'] = str(rel['synsets']).lower()
                    # These replace the squared brackets and the apostrophe
                    rel['synsets'] = str(rel['synsets']).replace('[', '')
                    rel['synsets'] = str(rel['synsets']).replace(']', '')
                    rel['synsets'] = str(rel['synsets']).replace("'", "")
                    # This capitalize only the first character of the string
                    rel['synsets'] = string.capwords(rel['synsets'])
                    # Honestly? I don't remember what this was for, it was used in the frame extraction pipeline
                    rel['synsets'] = re.sub(r"\([^()]*\)", "", rel['synsets'])
    # Finally we dump everything in the main file           
    json.dump(scenegraph, out)




format_rel_syns()