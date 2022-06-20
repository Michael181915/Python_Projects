from json import dumps
import json
#import math

filename_1 = 'tests.json'
filename_2 = 'values.json'
inputfile = 'report.json'

#with open(filename_1, 'r', encoding='utf-8') as f1:
#    text_1 = json.load(f1)



print(len(text_1) + 1)
print()
#print(dumps(text_1, indent=4))    #, ensure_ansii=False

print()
#print(text_1['tests'][0]['values'][0]['values'][0]['values'][0]['title'])
print(text_1['tests'][2]['values'][0]['values'][0]['values'][0]['title'])
print()
print(text_1['tests'][2]['id'])



#      text_1['tests'][0]['title'] 
#           id, title, value
#                                     9
#      text_1['tests'][3]['values'][0]['values'][0]['values'][0]['value']        
#                     2 3           0            0           0 1   

def enum_array(array):
    for array in text_1['tests']:
        print('Лицо ', array['id'], ' had passed ', array['title'], ' ', array['value'], ' .')    
        
    print()

    
print(list(text_1.keys()))  # 
'''print(list(txt_1))       # 
print(list(txt_2))          # 
print(list(txt_3))          # 
print(list(txt_4))          # 
print(list(txt_5))          # 
print(list(txt_6))          # 
print(list(txt_7))          # 
print(list(txt_8))          # 
print(list(txt_9))'''       # 


for txt_1 in text_1['tests']:
    print(list(txt_1))
    print(txt_1)
    
    #for txt_2 in txt_1['values']:
    for txt_2 in txt_1['values']):
        print(len(txt_2))
        print(txt_2)

        
        for txt_3 in txt_1['values']:
            print(list(txt_3))
            print(txt_3)


            for txt_4 in txt_3['values']:
                print(list(txt_4))
                print(txt_4)

                
                for txt_5 in txt_4['values']:
                    print(list(txt_5))
                    print(txt_5)

                    
                    for txt_6 in txt_5['values']:
                        print('Лицо ', txt_6['id'], ' had passed ', txt_6['title'], ' ', txt_6['value'], ' .')

                        for txt_7 in txt_6['values']:
                            print('Лицо ', txt_7['id'], ' had passed ', txt_7['title'], ' ', txt_7['value'], ' .')
                
                            for txt_8 in txt_7['values']:
                                print('Лицо ', txt_8['id'], ' had passed ', txt_8['title'], ' ', txt_8['value'], ' .')

                                for txt_9 in txt_8['values']:
                                    print('Лицо ', txt_9['id'], ' had passed ', txt_9['title'], ' ', txt_9['value'], ' .')
                                    
                                print('Всё!')    
                                print()
                                
                            print('Всё!')    
                            print()
                            
                        print('Всё!')    
                        print()
                        
                    print('Всё!')
                    print()
                    
                print('Всё!')    
                print()
                
            print('Всё!')              
            print()
            
        print('Всё!')    
        print()
        
    print('Всё!')
    print()

#    print('Лицо  {0} \t {1}  \t {2} exam.'.format(txt['id'], txt['title'], txt['id'])) 
#    print('Лицо ', txt['id'], ' had passed ', txt['title'], ' ', txt['value'], ' ', txt['values'], ' .')
#    print('Лицо  {0} \t {1}  \t {2} exam.'.format(txt['id'], txt['title'], txt['value']))
#print('Лицо ', txt_3['id'], ' had passed ', txt_3['title'], ' ', txt_3['value'], ' .')


print()
print('-----------------------------------------')
print()

with open(filename_2, 'r', encoding='utf-8') as f2:
    text_2 = json.load(f2)


print(len(text_2) + 1)
print()
print(dumps(text_2, indent=4))    #, ensure_ansii=False

for txt in text_2['values']:         
    print('Лицо  {0} \t {1} exam.'.format(txt['id'], txt['value'])) 
    #print('Лицо ', txt['id'], '\t', txt['value'], 'exam.')


