
import io
import json
from collections import Counter
from collections import defaultdict
import glob
all_info = defaultdict(lambda: 0)
percentaldict = defaultdict(lambda: 0)


def read_info(filename, userFinal):
    """ Read profiles into a list of Counter objects.
    DO NOT MODIFY"""
    user_data = defaultdict(lambda: 0)
    percentdict = defaultdict(lambda: 0)
    total = 0
    fileN = io.open(userFinal, mode='w+', encoding='utf-8')
    with io.open(filename, mode='rt', encoding = 'utf-8') as infile:

        for line in infile:
            line = line.encode('utf-8')
            
            line = json.loads(line)
            for genre in line['genre']:
               
               user_data[genre] += 1
               all_info[genre] += 1
               total += 1
               
    for genre in user_data.keys():
        if total is not 0:
            percent = user_data[genre]/float(total) 
            percent = percent * 100
            percentdict[genre] = percent
            percentdict['totalnumber'] = total    
    if percentdict: 
        fileN.write(json.dumps(percentdict, ensure_ascii=False, encoding='utf-8') + u"\n")
    return total
                                  
def main():
    total_all = 0
    total_main = 0
    for files in glob.glob("data/*.json"):
        user = str.split(files, ".")
        user = str.split(user[0], "\\")
        userFinal = "data_person/" + user[1] + ".json"
        
        total_main = read_info(files, userFinal)
        total_all = total_all + total_main
    fileinfo = io.open("data_person/general_info.json", mode='w+', encoding='utf-8')
    for genre in all_info.keys():
        perc = all_info[genre]/float(total_all)
        perc = perc * 100
        percentaldict[genre] = perc
    percentaldict['totalnumber'] = total_all
    fileinfo.write(json.dumps(percentaldict, ensure_ascii=False, encoding='utf-8') + u"\n")    
    """for x in range (len(twit)):
    
        if twit[x]["user"]["statuses_count"] > 500:
            screen_name = twit[x]["user"]["screen_name"]
            define_users(screen_name)

    """
if __name__ == '__main__':
    main()            
            