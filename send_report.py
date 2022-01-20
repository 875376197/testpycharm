import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://admin:Aa123456@39.105.54.35:3000/job/郑嘉仪/21/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=c28b8986df2572e30066f931fb688073724996b58e5c15363d064497a85054bc'
        self.error = self.get_allure_error()

    def get_allure_error(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号admin,密码Aa123456",
                    "title": "!" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://admin:Aa123456@39.105.54.35:3000/job/郑嘉仪/21/allure"
                }
            }
            response = requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
