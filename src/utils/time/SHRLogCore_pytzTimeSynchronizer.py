
import pytz
from datetime import datetime
from typing import Union

def sync_system_time() -> Union[str , None]:
    try:
        time_zone : pytz.timezone = pytz.timezone('Asia/Shanghai')
        now = datetime.now(time_zone)
        return now.strftime("%Y-%m-%d %H:%M:%S")

    except:
        return None

    finally:
        del time_zone , now