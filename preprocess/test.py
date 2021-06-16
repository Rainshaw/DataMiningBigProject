import os
import pandas as pd

dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', '互联网招聘网站数据-20190109')

files = ['1545993937965.csv', '1545995178836.csv', '1545994719214.csv', '1545993524166.csv', '1545994117111.csv',
         '1545993734962.csv', '1545995482689.csv', '1545994520923.csv', '1545993316117.csv', '1545996463690.csv',
         '1545995875667.csv', '1545996273574.csv', '1545995679248.csv', '1545993098203.csv', '1545995371123.csv',
         '1545996077068.csv', '1545994918682.csv', '1545994993854.csv', '1545994322721.csv']
files_path = [os.path.join(dir_path, file) for file in files]

# for file_path in files_path:
#     print(file_path)
#     csv = pd.read_csv(file_path, ',', encoding='gb18030', parse_dates=["page_publish_time"],
#                       dtype={
#                           "page_url": str,
#                           "pos_desc": str,
#                           # "page_publish_time": date,
#                           "pos_count": str,
#                           "page_province": str,
#                           "pos_class": str,
#                           "pos_industry": str,
#                           "site_name": str,
#                           "pos_age": str,
#                           "pos_name": str,
#                           "pos_welfare": str,
#                           "_id": str,
#                           "page_city": str,
#                           "old_industry": str,
#                           "deliver_count": str,
#                           "pos_salary": str,
#                           "com_name": str,
#                           "pos_education": str,
#                           "pos_experience": str,
#                           "read_count": str
#                       })
#     print(csv.shape)

# cnt = 0
#
# for file_path in files_path:
#     with open(file_path, 'rb') as f:
#         for line in f:
#             if line.find(b'\x00'):
#                 cnt += 1
#
# print(cnt)  # 16917223

# for file_path in files_path:
#     print(f'{file_path}')
#     with open(file_path, 'r', encoding='gb18030') as f:
#         table = csv.DictReader((line.replace('\0', '') for line in f))
#         cnt = 0
#         for row in table:
#             cnt += 1
#             # print('\b' * len(str(table.line_num-1)), end='')
#             # print(table.line_num, end='')
#             # if 297522 <= table.line_num and cnt > 0:
#             #     cnt -= 1
#             #     print(table.line_num)
#             #     print(row)
#         print(cnt)


#
# with open(file_path, 'rb') as f, open(file_path + ".1", 'wb') as f1:
#     for line in f:
#         f1.write(line.replace(b'\0', b''))


# with open(file_path + ".1", 'r', encoding='gb18030') as f:
#     cr = csv.DictReader(f)
#     for row in cr:
#         print(row)
#         print(cr.line_num)

# for file_path in files_path:
#     with open(file_path, 'rb') as f, open(file_path.replace('互联网招聘网站数据-20190109/', ''), 'wb') as f1:
#         line = f.readline()
#         cnt = line.count(b',')
#         while line:
#             if line.count(b',') != cnt:
#                 line = line.strip(b'\n')
#                 line += f.readline()
#                 continue
#             f1.write(line)
#             line = f.readline().replace(b'"', b'')

dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
files_path = [os.path.join(dir_path, file) for file in files]

for file_path in files_path:
    print(file_path)
    df = pd.read_csv(file_path, ',', encoding='gb18030', parse_dates=["page_publish_time"],
                     dtype={
                         "page_url": str,
                         "pos_desc": str,
                         # "page_publish_time": date,
                         "pos_count": str,
                         "page_province": str,
                         "pos_class": str,
                         "pos_industry": str,
                         "site_name": str,
                         "pos_age": str,
                         "pos_name": str,
                         "pos_welfare": str,
                         "_id": str,
                         "page_city": str,
                         "old_industry": str,
                         "deliver_count": str,
                         "pos_salary": str,
                         "com_name": str,
                         "pos_education": str,
                         "pos_experience": str,
                         "read_count": str
                     })
    print(df.shape)
    print(df.info())
