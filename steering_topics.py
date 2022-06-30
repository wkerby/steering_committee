import csv
file_name = r'Z:\Shared\Users\WKerby\My Computer\Documents\D&I Steering Committee Monthly Sheet.csv'
with open(file_name, "r") as file_object:
    lines = list(csv.reader(file_object))[1:]
    topic_list = []
    for line in lines:
        topic_list.append(line[2])
file_name2 = r'Z:\Shared\Users\WKerby\My Computer\Documents\D&I Topics.txt'
with open(file_name2,"w") as file_object2:
    for topic in topic_list:
        file_object2.write(topic[3:]+ '\n')
        
