import long_response as long;
import re


def get_response(user_input):
    split_messages = re.split(r'+;!', user_input)
    # response = check_all_messages(split_messages)
    return split_messages;

while True:
    user = input('You: ')
    # print(user.split('? + '))
    get_response(user)