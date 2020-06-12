from utils import DriverUtils
import pytest


@pytest.mark.run(order=1)
class TestBegin:

    def test_begin(self):
        # 关闭 关闭浏览器驱动的开关
        DriverUtils.change_mp_key(False)