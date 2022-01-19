
#
# # #    todo:获取token登录
# import jmespath as jmespath
# import pytest as pytest
# import requests
#
#
# # @pytest.fixture()
# # def header():
# #     data = {"name": "lsj1", "password": "123123"}
# #     r = requests.post(
# #         "http://123.56.138.96:3012/api/ainews-user/user/login",
# #         json=data
# #     )
# #     # logger.info(r.json().get("access_token"))
# #     token = r.json().get("access_token")
# #     header = {"Content-Type": "application/json;charset=UTF-8", 'Authorization': token}
# #     return header
# #
# #
# #
# #
# # @pytest.fixture()
# # def id1(header):
# #     data = {'page': 1,
# #             'per_page': 10,
# #             'start_time': '2021-12-30',
# #             'end_time': '2022-01-13'}
# #     res = requests.request(method='get',
# #                            url='http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group',
# #                            headers=header, params=data)
# #     return jmespath.search("[?name=='李大鹅'].id",res.json())
# # # print(id1())
#
#
# #
# #
# class TestAiYuQing:
#
#     def setup_class(self):
#         pass
#
#          # todo:公司舆情
#
#     def test_index(self, header):
#         data = {"page": 1, "page_size": 10, "order_by": "", "order_type": "DESC", "cp_type": "", "board": "",
#                 "keyword": "",
#                 "is_new_data": 0, "classification": "", "category_key": "", "min_score": 0, "max_score": 100,
#                 "start_time": "2021-12-27", "end_time": "2022-01-10"}
#         res = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-user/v2/company-list/index',
#                                headers=header, json=data)
#         # print(json.dumps(res.json(), indent=1, ensure_ascii=False))
#         # logger.info(res.json().get('total'))
#         assert jmespath.search("total[0].count", res.json()) == '35062'
#
#     #
#     #     # # todo:公司舆情——公司详情
#     def test_article_list(self, header):
#         # header = {"Content-Type": "application/json;charset=UTF-8", 'Authorization': get_token()}
#         data = {"cp_code": ["300783"], "sort_by": "default", "sort_order": "desc", "start_time": "2021-12-27",
#                 "end_time": "2022-01-10", "page": 1, "risk_level": [0, 1, 2], "article_type": "all", "matter": "all"}
#         res = requests.request(method='post',
#                                url='http://123.56.138.96:3012/api/ainews-espy/api/opinion/company-article-list',
#                                headers=header,
#                                json=data)
#         assert jmespath.search("ok", res.json()) == True
#         # print(json.dumps(res.json(), indent=1, ensure_ascii=False))
#
#     # todo:行业新闻
#     def test_news(self, header):
#         data = {"industry": "all", "start_time": "2021-12-28", "end_time": "2022-01-11", "page": 1, "page_size": 10,
#                 "sort_order": "desc"}
#         res = requests.request(method='post',
#                                url='http://123.56.138.96:3012/api/ainews-espy/api/news/news-list-industry',
#                                headers=header, json=data)
#         assert jmespath.search("ok", res.json()) == True
#         # print(json.dumps(res.json(),indent=4,ensure_ascii=False))
#         # print(json.dumps(res.json(), indent=1, ensure_ascii=False))
#
#     # todo:添加公司分组
#     def test_add_group(self, header):
#         data = {"name": "李大鹅"}
#         res = requests.request(method='post',
#                                url='http://123.56.138.96:3012/api/ainews-user/company-group/create',
#                                headers=header, json=data)
#         assert res.json().get('name') == '李大鹅'
#         assert res.json().get('created_by') == 181
#         global id1
#         id1 = res.json().get('id')
#         # print(json.dumps(res.json(), indent=1, ensure_ascii=False))
#
#     # # todo:公司分组添加公司
#
#     def test_add_company(self, header, id1):
#         data = {"company_code": "000001", "group_id": id1}
#         res = requests.request(method='post',
#                                url='http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
#                                headers=header, json=data)
#         # assert jmespath.search('company_code', res.json()) == id1
#
#     # todo:删除公司分组
#     def test_del_group(self, header, id1):
#         data = {'id': id1}
#         res = requests.request(method='get',
#                                url='http://123.56.138.96:3012/api/ainews-user/company-group/delete',
#                                headers=header, params=data)
#
#         assert res.json() == True

# a=TestAiyuqing
# a.test_add_group()
