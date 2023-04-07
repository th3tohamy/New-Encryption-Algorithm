import datetime
import json
import random


def op_():
    with open('data_file.json', 'r') as f:
        nums = json.load(f)
    print(nums)
    return nums



def make_enc(*args, **kwargs):
    flag = True
    nums = op_()
    now = datetime.datetime.now()
    hour = now.hour  # if now.hour != 0 else 12
    minute = now.minute
    second = now.second
    if (hour and minute and second) in nums.keys():
        if flag:

                hour_ = random.choice(nums[hour])
                minute_ = random.choice(nums[minute])
                second_ = random.choice(nums[second])
                key_s = f'{hour_}_{minute_}_{second_}'
                pyscript.write('text', key_s)

    else:
        print('err')


