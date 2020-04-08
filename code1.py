import pandas as pd

index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

data = [['1000', 'Steve', 90.72],
        ['1001', 'James', 78.09],
        ['1002', 'Doyeon', 98.43],
        ['1003', 'Jane', 64.19],
        ['1004', 'Pilwoong', 81.30],
        ['1005', 'Tony', 99.14],
        ]
df = pd.DataFrame(data, columns=['학번', '이름', '점수'])


data1 = {'학번': ['2015', '2016', '2017'],
         '이름': ['화석', '공룡', '지층'],
         '성적': ['A+', 'B0', 'C+']}
df2 = pd.DataFrame(data1)


df3 = pd.read_csv(r'C:\Users\User\Desktop\file1.csv')
print(df3)
print(df3.columns)
