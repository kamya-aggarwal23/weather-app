# reading a csv file 
# import csv
# with open('NetFlix.csv','r') as csv_file:
#     csv_reader=csv.reader(csv_file)#file must be differently encded so this code wont work 
#     for line in csv_reader:
#         print(line)

# # this code is to print whole csv file 
# import csv
# with open('NetFlix.csv', 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

# # this print only all list's specified element at specified position
# import csv
# with open('NetFlix.csv', 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(next(csv_reader))#this will loop over the first row (it generally is the header line)
#     # for line in csv_reader:
#     #     print(line[0])

# writing to a csv file or writing a csv file
# import csv
# with open('NetFlix.csv','r',encoding='utf-8') as csv_file:
#     csv_reader=csv.reader(csv_file)
#     with open('NewNetFlix.csv','w',encoding='utf-8') as new_file:
#         csv_writer=csv.writer(new_file,delimiter='\t')#delimiter is like something which changes ','other are ';','|' etc
#         for line in csv_reader:
#             csv_writer.writerow(line)

# parsing and using DictReader
# import csv
# with open('NetFlix.csv', 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)#DictReader gives the file in dictionary format
#     for line in csv_reader:
#         print(line['title'])

import csv
with open('NetFlix.csv','r',encoding='utf-8') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    with open('NewNetFlix.csv','w',encoding='utf-8') as new_file:
        fieldnames=['show_id','type','title','director','cast','country','date_added','release_year','rating','duration','genres','description']
        csv_writer=csv.DictWriter(new_file,fieldnames,delimiter='\t')#delimiter is like something which changes ','other are ';','|' etc
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)



