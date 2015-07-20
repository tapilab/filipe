import io
import json
from collections import Counter
from collections import defaultdict
import glob
Agreeableness = defaultdict(lambda: 0)
Conscientiousness = defaultdict(lambda: 0)
Extraversion = defaultdict(lambda: 0)
Neuroticism = defaultdict(lambda: 0)
Openness = defaultdict(lambda: 0)

def define_behavior():
    for files in glob.glob("humor/*.csv"):
        behavior = str.split(files, ".")
        behavior = str.split(behavior[0], "\\")
        with io.open(files, mode='rt', encoding = 'utf-8') as infile:
            for line in infile:
                linebehavior = str.split(str(line), ",")
                if linebehavior[0]:
                    if "Agreeableness" in behavior[1] :
                        Agreeableness[linebehavior[0]] = linebehavior[1]
                    elif "Conscientiousness" in behavior[1] :
                        Conscientiousness[linebehavior[0]] = linebehavior[1]
                    elif "Extraversion" in behavior[1] :
                        Extraversion[linebehavior[0]] = linebehavior[1]
                    elif "Neuroticism" in behavior[1] :
                        Neuroticism[linebehavior[0]] = linebehavior[1]
                    elif "Openness" in behavior[1] :
                        Openness[linebehavior[0]] = linebehavior[1]
                        
       
        
    
def define_twitters():
    for files in glob.glob("twitters/*.json"):
         user = str.split(files, ".")
         user = str.split(user[0], "\\")
         userFinal = "data_twitter_person/" + user[1] + ".json"
         fileN = io.open(userFinal, mode='w+', encoding='utf-8')
         behaviordict = defaultdict(lambda: 0)
         with io.open(files, mode='rt', encoding = 'utf-8') as infile:
            for line in infile:
              pandoratwit = False
              twit = json.loads(line)                
              text = twit['text'].encode('utf-8')
              line_twitter = str.split(str(text), " ")
              'print len(line_twitter)'
              if "I'm listening to" in text:
                 if "#pandora"  in text:
                   pandoratwit = True
              if pandoratwit == False:
                 for keys in Agreeableness.keys():
                     key = str.split(keys," ")
                     
                     if len(key) == 1:
                         
                         for tokens in line_twitter:
                             """checking 
                             print tokens, key[0]
                             """
                             if key[0] == tokens:

                                 value =  Agreeableness[key[0]]
                                 behaviordict['Agreeableness'] += float(value)
                                 """checking tokens and dict
                                 print behaviordict
                                 print key, " ", tokens
                                 """
                     elif len(key) == 2:
                        if len(line_twitter) > 1:                            
                            for tokenLen in range(len(line_twitter)-1):
                                
                                'print line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                                'print key[0], " ", key[1]'
                                
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1]:
                                     value =  Agreeableness[key[0] +" " + key[1]]
                                     behaviordict['Agreeableness'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                     elif len(key) == 3:
                        if len(line_twitter) > 2:                            
                            for tokenLen in range(len(line_twitter)-2):
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1] and key[2] == line_twitter[tokenLen+2]:
                                     value =  Agreeableness[key[0] +" " + key[1]+" " + key[2]]
                                     behaviordict['Agreeableness'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", key[2], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1], " ", line_twitter[tokenLen+2]'
                 """
                 Conscientiousness
                 """
                 for keys in Conscientiousness.keys():
                     key = str.split(keys," ")
                     
                     if len(key) == 1:
                         
                         for tokens in line_twitter:
                             """checking 
                             print tokens, key[0]
                             """
                             if key[0] == tokens:

                                 value =  Conscientiousness[key[0]]
                                 behaviordict['Conscientiousness'] += float(value)
                                 """checking tokens and dict
                                 print behaviordict
                                 print key, " ", tokens
                                 """
                     elif len(key) == 2:
                        if len(line_twitter) > 1:                            
                            for tokenLen in range(len(line_twitter)-1):
                                
                                'print line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                                'print key[0], " ", key[1]'
                                
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1]:
                                     value =  Conscientiousness[key[0] +" " + key[1]]
                                     behaviordict['Conscientiousness'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                     elif len(key) == 3:
                        if len(line_twitter) > 2:                            
                            for tokenLen in range(len(line_twitter)-2):
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1] and key[2] == line_twitter[tokenLen+2]:
                                     value =  Conscientiousness[key[0] +" " + key[1]+" " + key[2]]
                                     behaviordict['Conscientiousness'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", key[2], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1], " ", line_twitter[tokenLen+2]'
                 """
                 Extraversion
                 """
                 for keys in Extraversion.keys():
                     key = str.split(keys," ")
                     
                     if len(key) == 1:
                         
                         for tokens in line_twitter:
                             """checking 
                             print tokens, key[0]
                             """
                             if key[0] == tokens:

                                 value =  Extraversion[key[0]]
                                 behaviordict['Extraversion'] += float(value)
                                 """checking tokens and dict
                                 print behaviordict
                                 print key, " ", tokens
                                 """
                     elif len(key) == 2:
                        if len(line_twitter) > 1:                            
                            for tokenLen in range(len(line_twitter)-1):
                                
                                'print line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                                'print key[0], " ", key[1]'
                                
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1]:
                                     value =  Extraversion[key[0] +" " + key[1]]
                                     behaviordict['Extraversion'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                     elif len(key) == 3:
                        if len(line_twitter) > 2:                            
                            for tokenLen in range(len(line_twitter)-2):
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1] and key[2] == line_twitter[tokenLen+2]:
                                     value =  Extraversion[key[0] +" " + key[1]+" " + key[2]]
                                     behaviordict['Extraversion'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", key[2], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1], " ", line_twitter[tokenLen+2]'
                 """
                 Neuroticism
                 """
                 for keys in Neuroticism.keys():
                     key = str.split(keys," ")
                     
                     if len(key) == 1:
                         
                         for tokens in line_twitter:
                             """checking 
                             print tokens, key[0]
                             """
                             if key[0] == tokens:

                                 value =  Neuroticism[key[0]]
                                 behaviordict['Neuroticism'] += float(value)
                                 """checking tokens and dict
                                 print behaviordict
                                 print key, " ", tokens
                                 """
                     elif len(key) == 2:
                        if len(line_twitter) > 1:                            
                            for tokenLen in range(len(line_twitter)-1):
                                
                                'print line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                                'print key[0], " ", key[1]'
                                
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1]:
                                     value =  Neuroticism[key[0] +" " + key[1]]
                                     behaviordict['Neuroticism'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                     elif len(key) == 3:
                        if len(line_twitter) > 2:                            
                            for tokenLen in range(len(line_twitter)-2):
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1] and key[2] == line_twitter[tokenLen+2]:
                                     value =  Neuroticism[key[0] +" " + key[1]+" " + key[2]]
                                     behaviordict['Neuroticism'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", key[2], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1], " ", line_twitter[tokenLen+2]'
                 """
                 Openness
                 """
                 for keys in Openness.keys():
                     key = str.split(keys," ")
                     
                     if len(key) == 1:
                         
                         for tokens in line_twitter:
                             """checking 
                             print tokens, key[0]
                             """
                             if key[0] == tokens:

                                 value =  Openness[key[0]]
                                 behaviordict['Openness'] += float(value)
                                 """checking tokens and dict
                                 print behaviordict
                                 print key, " ", tokens
                                 """
                     elif len(key) == 2:
                        if len(line_twitter) > 1:                            
                            for tokenLen in range(len(line_twitter)-1):
                                
                                'print line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                                'print key[0], " ", key[1]'
                                
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1]:
                                     value =  Openness[key[0] +" " + key[1]]
                                     behaviordict['Openness'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1]'
                     elif len(key) == 3:
                        if len(line_twitter) > 2:                            
                            for tokenLen in range(len(line_twitter)-2):
                                if key[0] == line_twitter[tokenLen] and key[1] == line_twitter[tokenLen+1] and key[2] == line_twitter[tokenLen+2]:
                                     value =  Openness[key[0] +" " + key[1]+" " + key[2]]
                                     behaviordict['Openness'] += float(value)                                    
                                     'print key[0], " ", key[1], " ", key[2], " ", line_twitter[tokenLen], " ", line_twitter[tokenLen+1], " ", line_twitter[tokenLen+2]'
                                                                                    
         if behaviordict:
             fileN.write(json.dumps(behaviordict, ensure_ascii=False, encoding='utf-8') + u"\n")                          
def main():
    define_behavior()
    define_twitters()
if __name__ == '__main__':
    main()            
            