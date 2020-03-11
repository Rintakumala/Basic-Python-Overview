# ### Soal Nomor 1 ###

# def Hestek(string):
#     if string == '':
#         print('False')
#     else:
#         a = string.split()
#         z = '#'
#         for i in range(len(a)):
#             z += str(a[i]).capitalize()
#         print(z)
# Hestek('Hello how are you doing')

# ### Soal Nomor 2 ###

# def creat_phone_number(number):
#     z = '('
#     for i in range(3):
#         z += str(number[i])
#     z += ') '
#     for i in range(3,6):
#         z += str(number[i])
#     z  +='-'
#     for i in range(6,len(number)):
#         z += str(number[i])
#     print(z)

# creat_phone_number([1,2,3,4,5,6,7,8,9,0])

# ### Soal Nomor 3 ###

# def Sort_odd_even(num):
#     for i in range(len(num)):
#         for j in range(i+1, len(num)):
#             if num[i] % 2 == 0 and num[j] % 2 == 0:
#                 if num[i] < num[j]:
#                     num[i], num[j] = num[j], num[i]
#             elif num [i] % 2 != 0 and num[j] % 2 != 0:
#                 if num[i] > num[j]:
#                         num[i], num[j] = num[j], num[i]
#     print(num)
# Sort_odd_even([5,3,2,8,1,4])

### Soal Nomor 4 ###

def hollowTriangle(row):
    for i in range(row):
        for j in range((2*row)-1):
            if i==row-1 or i+j == row-1 or j-i == row-1:
                print('#',end='')
            else:
                print(end='_')
        print()
hollowTriangle(5)
