import csv
import os
import numpy as np
import math
from shutil import copyfile

#将图片分到类别文件夹中
_reader = open("train.csv", "r")
reader = list(csv.reader(_reader))
for line in reader:
    if line[0] == 'Type':
       continue
    AdoptionSpeed=line[23]
    PetID=line[21]
    PhotoAmt=line[22]
    print(int(float(PhotoAmt)))
    if int(float(PhotoAmt))>0:
        for i in range(int(float(PhotoAmt))):
            ori_name = '/root/kagglePetFinder/cy/train_images/'+str(PetID)+'-'+str(i+1)+'.jpg'
            dst_name = '/root/kagglePetFinder/cy/train_images/'+str(AdoptionSpeed)+'/'+str(PetID)+'-'+str(i+1)+'.jpg'
            copyfile(ori_name,dst_name)




# total_num = 0
# num = 0
# for root, dirs, files in os.walk('/home/zengh/Dataset/ActivityNet/Crawler/Kinetics/kinetics-400/'):
#     _class = root.split('/')[-1]
#     for temp in files:
#         total_num += 1
#         video_name = temp.split('.')[0]
#         path = os.path.join('/home/zengh/Dataset/ActivityNet/Crawler/Kinetics/kinetics-400-train/frames',_class,video_name)
#         if not os.path.isdir(path):
#             num += 1
#             print(path)
#             print('not ok!')

# print(num,total_num)
# print(len(os.listdir('/home/zengh/Dataset/ActivityNet/Crawler/Kinetics/kinetics-400-train-1/')))

#生成前10个label的csv，筛选掉未下载的record
# _reader = open("kinetics-400_val_10c.csv", "r")
# reader = list(csv.reader(_reader))

# _writer = open('kinetics-400_train_10c_temp.csv', 'w')
# writer = csv.writer(_writer)
# for line in reader:
#     _class = line[0]
#     video_name = line[1]
#     start_time = line[2]
#     end_time = line[3]

#     temp = video_name+str('_')+start_time.zfill(6) + \
#         str('_')+end_time.zfill(6)

#     path = os.path.join(
#         '/home/zengh/Dataset/ActivityNet/Crawler/Kinetics/kinetics-400-val/frames',_class,temp)
#     print(path)
#     if os.path.isdir(path):
#         writer.writerow(line)


# 记录mini-kinetics的label和csv
# _reader = open("./Mini-Kinetics-200-master/val_ytid_list.csv", "r")
# reader_mini = list(csv.reader(_reader))  

# _reader = open("kinetics-400_val.csv", "r")
# reader_full = list(csv.reader(_reader))    

# _writer = open('mini-kinetics-200-val.csv', 'w')
# writer = csv.writer(_writer)

# mini_label=[]
# for line_mini in reader_mini:
#     for line_full in reader_full:
#         # print('mini name ',line_mini[0],'full name',line_full[1])
#         if line_mini[0] == line_full[1]:
#             print("find you!")
#             writer.writerow(line_full)
#             label=line_full[0]
#             if label not in mini_label:
#                 mini_label.append(label)
#             break

# writer.writerow(mini_label)
# print("label num is",len(mini_label))

#记录未下载的minikinetics
# _reader = open("mini-kinetics-200-train.csv", "r")
# reader_mini = list(csv.reader(_reader))  

# _reader = open("kinetics-400_train_not_downloaded.csv", "r")
# reader_not_download = list(csv.reader(_reader))    

# _writer = open('mini-kinetics-200-train-not-download.csv', 'w')
# writer = csv.writer(_writer)

# for line_mini in reader_mini:
#     if line_mini in reader_not_download:
#         print("find you!")
#         writer.writerow(line_mini)


    



    

# 把已下载的视频，1/4作为val，3/4作为train
# csv_num = np.zeros([400,],dtype=int)
# csvFile_r = open("kinetics-400_train_downloaded.csv", "r")
# reader_ed = list(csv.reader(csvFile_r))
# index = -1
# last_class = ''

# for line in reader_ed:
#     _class = line[0]
#     if _class != 'label':
#         if _class != last_class:
#             last_class = _class
#             index = int(index+1)
#         csv_num[index]+=1

# # print(csv_num.sum())

# _writer_val = open("kinetics-400_train_60_val.csv", "w")
# _writer_train = open("kinetics-400_train_60_train.csv", "w")
# writer_val = csv.writer(_writer_val)
# writer_train = csv.writer(_writer_train)
# temp = int(1)
# for i in range(400):
#     val_num = math.floor(csv_num[i]/4)
#     for j in range(temp+0, temp+val_num):
#         writer_val.writerow(reader_ed[j])
#     for j in range(temp+val_num, temp+csv_num[i]):
#         writer_train.writerow(reader_ed[j])
#     temp+=csv_num[i]





# file_num = np.array([954.0,918.0,282.0,221.0,270.0,923.0,889.0,323.0,58.0,141.0,138.0,130.0,126.0,139.0,137.0,137.0,136.0,140.0,127.0,142.0,128.0,137.0,141.0,144.0,136.0,144.0,130.0,145.0,127.0,142.0,137.0,135.0,120.0,135.0,137.0,140.0,133.0,138.0,136.0,140.0,142.0,143.0,142.0,137.0,57.0,55.0,48.0,55.0,55.0,48.0,56.0,48.0,54.0,53.0,58.0,58.0,55.0,55.0,54.0,54.0,58.0,56.0,51.0,50.0,51.0,57.0,57.0,58.0,52.0,55.0,55.0,55.0,55.0,46.0,51.0,59.0,49.0,57.0,56.0,54.0,42.0,51.0,54.0,51.0,56.0,56.0,55.0,55.0,57.0,53.0,56.0,55.0,57.0,54.0,58.0,52.0,55.0,51.0,47.0,53.0,56.0,55.0,55.0,44.0,54.0,57.0,56.0,54.0,50.0,49.0,56.0,57.0,53.0,48.0,54.0,56.0,55.0,54.0,57.0,55.0,57.0,59.0,54.0,57.0,56.0,57.0,44.0,56.0,55.0,52.0,57.0,50.0,51.0,48.0,53.0,51.0,58.0,50.0,59.0,56.0,56.0,54.0,58.0,57.0,53.0,54.0,54.0,56.0,57.0,59.0,55.0,55.0,56.0,57.0,56.0,51.0,55.0,45.0,56.0,59.0,57.0,56.0,58.0,58.0,56.0,57.0,53.0,57.0,36.0,55.0,57.0,50.0,49.0,54.0,57.0,55.0,33.0,52.0,53.0,58.0,50.0,53.0,57.0,55.0,49.0,55.0,54.0,54.0,56.0,55.0,52.0,54.0,57.0,40.0,41.0,38.0,45.0,53.0,30.0,43.0,56.0,55.0,53.0,54.0,52.0,58.0,55.0,31.0,21.0,39.0,57.0,54.0,56.0,52.0,55.0,57.0,58.0,22.0,26.0,55.0,53.0,55.0,48.0,57.0,47.0,55.0,41.0,51.0,58.0,56.0,56.0,50.0,50.0,58.0,57.0,49.0,37.0,41.0,33.0,54.0,32.0,54.0,44.0,50.0,53.0,55.0,53.0,55.0,57.0,56.0,52.0,54.0,55.0,56.0,55.0,56.0,56.0,54.0,47.0,52.0,56.0,55.0,51.0,55.0,53.0,52.0,56.0,58.0,58.0,55.0,55.0,54.0,57.0,51.0,53.0,53.0,55.0,56.0,56.0,52.0,55.0,53.0,57.0,57.0,56.0,51.0,57.0,55.0,57.0,56.0,55.0,50.0,52.0,52.0,56.0,55.0,50.0,47.0,56.0,57.0,59.0,56.0,57.0,45.0,41.0,54.0,50.0,57.0,58.0,55.0,59.0,59.0,50.0,56.0,54.0,59.0,45.0,50.0,57.0,55.0,53.0,58.0,57.0,58.0,58.0,54.0,56.0,53.0,54.0,57.0,56.0,54.0,55.0,56.0,56.0,53.0,59.0,57.0,54.0,53.0,59.0,56.0,56.0,53.0,54.0,55.0,56.0,50.0,57.0,58.0,56.0,53.0,55.0,52.0,53.0,51.0,57.0,54.0,58.0,45.0,53.0,54.0,55.0,56.0,55.0,54.0,57.0,55.0,53.0,57.0,58.0,49.0,54.0,50.0,53.0,56.0,51.0,57.0,56.0,54.0,53.0,7.0,50.0,54.0,55.0,56.0,52.0,54.0,51.0,50.0,59.0,57.0,54.0,55.0,49.0,55.0,52.0,56.0,50.0,56.0])
# #已下载的各个类别的num
# csv_num = np.array([954.0,918.0,282.0,221.0,270.0,923.0,889.0,323.0,58.0,141.0,138.0,130.0,126.0,139.0,137.0,137.0,136.0,140.0,127.0,142.0,128.0,137.0,141.0,144.0,136.0,144.0,130.0,145.0,127.0,142.0,137.0,135.0,120.0,135.0,137.0,140.0,133.0,138.0,136.0,140.0,142.0,143.0,142.0,137.0,57.0,55.0,48.0,55.0,55.0,48.0,56.0,48.0,54.0,53.0,58.0,58.0,55.0,55.0,54.0,54.0,58.0,56.0,51.0,50.0,51.0,57.0,57.0,58.0,52.0,55.0,55.0,55.0,55.0,46.0,51.0,59.0,49.0,57.0,56.0,54.0,42.0,51.0,54.0,51.0,56.0,56.0,55.0,55.0,57.0,53.0,56.0,55.0,57.0,54.0,58.0,52.0,55.0,51.0,47.0,53.0,56.0,55.0,55.0,44.0,54.0,57.0,56.0,54.0,50.0,49.0,56.0,57.0,53.0,48.0,54.0,56.0,55.0,54.0,57.0,55.0,57.0,59.0,54.0,57.0,56.0,57.0,44.0,56.0,55.0,52.0,57.0,50.0,51.0,48.0,53.0,51.0,58.0,50.0,59.0,56.0,56.0,54.0,58.0,57.0,53.0,54.0,54.0,56.0,57.0,59.0,55.0,55.0,56.0,57.0,56.0,51.0,55.0,45.0,56.0,59.0,57.0,56.0,58.0,58.0,56.0,57.0,53.0,57.0,36.0,55.0,57.0,50.0,49.0,54.0,57.0,55.0,33.0,52.0,53.0,58.0,50.0,53.0,57.0,55.0,49.0,55.0,54.0,54.0,56.0,55.0,52.0,54.0,57.0,40.0,41.0,38.0,45.0,53.0,30.0,43.0,56.0,55.0,53.0,54.0,52.0,58.0,55.0,31.0,21.0,39.0,57.0,54.0,56.0,52.0,55.0,57.0,58.0,22.0,26.0,55.0,53.0,55.0,48.0,57.0,47.0,55.0,41.0,51.0,58.0,56.0,56.0,50.0,50.0,58.0,57.0,49.0,37.0,41.0,33.0,54.0,32.0,54.0,44.0,50.0,53.0,55.0,53.0,55.0,57.0,56.0,52.0,54.0,55.0,56.0,55.0,56.0,56.0,54.0,47.0,52.0,56.0,55.0,51.0,55.0,53.0,52.0,56.0,58.0,58.0,55.0,55.0,54.0,57.0,51.0,53.0,53.0,55.0,56.0,56.0,52.0,55.0,53.0,57.0,57.0,56.0,51.0,57.0,55.0,57.0,56.0,55.0,50.0,52.0,52.0,56.0,55.0,50.0,47.0,56.0,57.0,59.0,56.0,57.0,45.0,41.0,54.0,50.0,57.0,57.0,55.0,59.0,59.0,50.0,56.0,54.0,59.0,45.0,50.0,57.0,55.0,53.0,58.0,57.0,58.0,58.0,54.0,56.0,53.0,54.0,57.0,56.0,54.0,55.0,56.0,56.0,53.0,59.0,57.0,54.0,53.0,59.0,56.0,56.0,53.0,54.0,55.0,56.0,50.0,57.0,58.0,56.0,53.0,55.0,52.0,53.0,51.0,57.0,54.0,58.0,45.0,53.0,54.0,55.0,56.0,55.0,54.0,57.0,55.0,53.0,57.0,58.0,49.0,54.0,50.0,53.0,56.0,51.0,57.0,56.0,54.0,53.0,7.0,50.0,54.0,55.0,56.0,52.0,54.0,51.0,50.0,59.0,57.0,54.0,55.0,49.0,55.0,52.0,56.0,50.0,56.0])
# csv_num = csv_num.astype(int)

# 
    

# index = -1
# last_class = ''

# for line in reader:
#     _class = line[0]
#     if _class == 'label':
#         continue

#     if _class != last_class:
#         index += 1
#         index = int(index)
#         last_class = _class

#     video_name = line[1]
#     start_time = line[2]
#     end_time = line[3]

#     temp = video_name+str('_')+start_time.zfill(6) + \
#         str('_')+end_time.zfill(6)+'.mp4'

#     path = os.path.join(
#         '/home/zengh/Dataset/ActivityNet/Crawler/Kinetics/kinetics-400', _class, temp)

#     if os.path.isfile(path):
#         num[index] += 1
#         writer.writerow(line)

# writer.writerow(num)


