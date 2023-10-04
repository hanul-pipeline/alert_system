from utils.gas import *

def create_alert(timestamp: datetime, loc_id: int, sensor_id: int, value: float):
    alert_data = alert_gas(timestamp, loc_id, sensor_id, value)
    
    # 가스 종류 설정
    alert_data["gas_type"] = determine_gastype(sensor_id)
    
    # 경고 레벨 설정
    alert_data["warning_level"] = determine_warning(value)

    return alert_data