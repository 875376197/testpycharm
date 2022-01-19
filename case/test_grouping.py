import jmespath
import pytest
from loguru import logger

from api.api_grouping import Grouping


class TestGrouping:
    def setup_class(self):
        self.group = Grouping()

    # todo:查询公司列表

    @pytest.mark.smoke
    @pytest.mark.parametrize("a,check", [(1, 200)], ids=['123'])
    def test_get_list(self, a, check):
        r = self.group.get_id(a)
        assert r.status_code == check

    # todo:添加公司分组

    @pytest.mark.parametrize("a,check", [("中文", 200), ("tay", 200), ("123", 200)], ids=["chin", "english", "int"])
    def test_add_group(self, a, check):
        r = self.group.add_group(a)
        assert r.status_code == check

    #     todo:公司分组名称添加公司

    @pytest.mark.parametrize("a,check", [["[?name=='中文'].id", 200]], ids=['123'])
    def test_add_company(self, a, check):
        r = self.group.get_id(1)
        id = jmespath.search(a, r.json())
        res = self.group.add_company(id)
        assert res.status_code == check

    # todo:删除公司分组

    @pytest.mark.parametrize("a,check", [
        ("[?name=='中文'].id", 200),
        ("[?name=='123'].id", 200),
        ("[?name=='tay'].id", 200),
    ], ids=["汉字", "english", "int"])
    def test_del_group(self, a, check):
        r = self.group.get_id(1)
        id = jmespath.search(a, r.json())
        res = self.group.del_group(id)
        assert res.status_code == check

    @pytest.mark.smoke
    def test_all_group(self):
        self.group.add_group("宝藏挖掘机")
        r = self.group.get_id(1)
        id = jmespath.search("[?name=='宝藏挖掘机'].id", r.json())
        logger.info(id)
        self.group.add_company(id)
        r = self.group.del_group(id)
        assert r.json() == True



