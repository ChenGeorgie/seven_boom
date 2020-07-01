
def seven_boom(end_number):
    '''seven boom game in a list '''
    arr = []
    for i in range(1, end_number+1):
        #1.check if the num is divisible by 7.
        #2.and A number is divisible by 7 and checks whether the remainder is equal to 0.
        if i % 7 == 0 or '7' in str(i):
            arr.append('BOOM')
        else:
            arr.append(i)
    return arr

print(seven_boom(15)
