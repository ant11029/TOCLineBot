from transitions.extensions import GraphMachine

from utils import send_text_message

import random


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "吃啥"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        list = ['雙饗丼', '元之氣', '七海', '五花馬', 'Mr.拉麵', '成大館',
                '鐵板麵', '鍋燒', '早到', '麥當勞', '阿發', '蒸蛋飯', '咖哩飯']

        reply_token = event.reply_token
        print(reply_token)
        text = random.choice(list)
        send_text_message(reply_token, text)
        print("Send message")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
