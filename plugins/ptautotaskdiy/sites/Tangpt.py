from ..base.NexusPHP import NexusPHP
from lxml import etree
from ..base.Decorator import task_info
from ..base.BaseTask import BaseTask


class Tangpt(NexusPHP):

    def __init__(self, cookie):
        super().__init__(cookie)

    @staticmethod
    def get_site_name():
        return "躺平"

    @staticmethod
    def get_url():
        return "https://www.tangpt.top"

    @staticmethod
    def get_site_domain():
        return "tangpt.top"

    def send_messagebox(self, message: str, callback=None) -> str:
        return super().send_messagebox(message)

    def claim_task(self, task_id: str, rt_method=None):
        return super().claim_task(task_id, lambda response: response.json().get("msg", "未知错误"))


class Tasks(BaseTask):
    def __init__(self, cookie: str):
        super().__init__(Tangpt(cookie))

    @task_info(label="躺平任务领取", hint="领取躺平站点的苍蝇腿/VIP任务，平日选苍蝇腿任务，月末选VIP任务。")
    def daily_claim_task(self):
        # 获取今天日期，判断是否当月最后一天
        today = datetime.date.today()
        _, month_last_day = calendar.monthrange(today.year, today.month)
        if today.day == month_last_day:
            task_id = "4"
        else:
            task_id = "5"
        
        result = self.client.claim_task(task_id)
        return result
        
    def daily_checkin(self):
        return self.client.attendance()
