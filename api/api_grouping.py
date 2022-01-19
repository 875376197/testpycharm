

from api.base_api import BaseApi


class Grouping(BaseApi):

    def add_group(self, name):
        data = {"method": "post",
                "url": "http://123.56.138.96:3012/api/ainews-user/company-group/create",
                "headers": self.header,
                "json": {"name": name}
                }
        return self.send(data)

    def get_id(self, num):
        data = {"method": "get",
                "url": "http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group",
                "headers": self.header,
                "params": {'page': num,
                           'per_page': 10,
                           'start_time': '2021-12-30',
                           'end_time': '2022-01-13'}}
        return self.send(data)

    # more页面
    def new_more(self,a):
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-espy/api/opinion/flash-news",
            "json": {"start_time": "2022-01-04T16:51:49", "end_time": "2022-01-11T16:51:49", "page":a, "pagesize": 20},
            "headers": self.header
        }
        return self.send(data)

    # def index(self):
    #     data = {"method": "post",
    #             "url": "http://123.56.138.96:3012/api/ainews-user/v2/company-list/index",
    #             "headers": self.header,
    #             "json": {"page": 1, "page_size": 10, "order_by": "", "order_type": "DESC", "cp_type": "",
    #                      "board": "",
    #                      "keyword": "",
    #                      "is_new_data": 0, "classification": "", "category_key": "", "min_score": 0,
    #                      "max_score": 100,
    #                      "start_time": "2021-12-27", "end_time": "2022-01-10"}}
    #     return self.send(data)

    def add_company(self, id):
        data = {"method": "post",
                "url": "http://123.56.138.96:3012/api/ainews-user/company-group/company-create",
                "json": {"company_code": "000001", "group_id": id},
                "headers": self.header
                }
        return self.send(data)

    def del_group(self, a):
        data = {"method": 'get',
                "url": "http://123.56.138.96:3012/api/ainews-user/company-group/delete",
                "headers": self.header,
                "params": {'id': a}}
        return self.send(data)

# if __name__ == '__main__':
#     case = Grouping()
#     case.get_id()
#     case.add_group()
#     case.index()
#     case.article_list()
