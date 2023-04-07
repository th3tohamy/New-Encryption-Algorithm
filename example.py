import secrets
from string import ascii_letters
import json
from secrets import SystemRandom
from flask import Flask, render_template, jsonify
import datetime
import random

app = Flask(__name__)


def regen_enc():
    nums = {int(i): ["".join(rand.choices(ascii_letters, k=random.randint(15, 33))) for j in range(2)] for i in
            range(60)
            if i is not None}

    with open('static/data_file.json', 'w') as f:
        json.dump(nums, f)
    print('ok')
    return nums


def open_():
    with open('static/data_file.json', 'r') as f:
        data = json.load(f)
        return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/verify_time/<plaintext>', methods=['POST'])
def verify_encryption_key_time(plaintext):
    hour, minute, second = map(str, plaintext.split('_'))
    try:
        hour_ = [num for num in nums if hour in nums[num]][0]
        minute_ = [num for num in nums if minute in nums[num]][0]
        second_ = [num for num in nums if second in nums[num]][0]
        formatted_time_str = datetime.datetime.strptime(f'{hour_}:{minute_}:{second_}', '%H:%M:%S').time()
        print(formatted_time_str)
        time_now = datetime.datetime.now()
    except:
        return jsonify({'data': 'token not valid'})
    try:
        if int(formatted_time_str.hour) == int(time_now.hour):
            if int(formatted_time_str.minute) == int(time_now.minute):
                time_diff = int((time_now.second - formatted_time_str.second))
                if int(time_diff) >= 2:
                    print('timeout token ')
                    with open('static/data_file.json', 'w') as f:
                        json.dump(nums, f)
                    return jsonify({'data': 'timeout token'})
                print('good token')
                with open('static/data_file.json', 'w') as f:
                    json.dump(nums, f)
                return jsonify({'data': time_diff})
        else:
            return jsonify({'data': 'token not found'})
    except:
        return jsonify({'data': 'token not valid'})


if __name__ == '__main__':
    rand = SystemRandom()
    key = secrets.token_bytes(32)
    nums = {int(i): ["".join(rand.choices(ascii_letters, k=random.randint(15, 33))) for j in range(5000)] for i in
            range(100)
            if i is not None}
    with open('static/data_file.json', 'w') as f:
        json.dump(nums, f)
    app.run()
