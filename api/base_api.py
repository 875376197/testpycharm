import json
import jmespath
import requests
from loguru import logger




class BaseApi:
    def __init__(self):
        self.header = {"Content-Type": "application/json;charset=UTF-8", 'Authorization': self.get_token()}

    def send(self, data):
        res = requests.request(**data)
        # logger.info(res.json())
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

        return res

    def get_token(self):
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/user/login",
            "json": {"name": "lsj1", "password": "123123"}
        }
        # logger.info(r.json().get("access_token"))
        r = self.send(data)
        return jmespath.search('access_token', r.json())
        # logger.debug(token)

if __name__ == '__main__':
    print(BaseApi().get_token())


