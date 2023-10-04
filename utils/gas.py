from datetime import datetime
def alert_gas(timestamp, loc_id, sensor_id, value):
    alert_data = {
        "timestamp": timestamp,
        "loc_id": loc_id,
        "sensor_id": sensor_id,
        "value": value,
        "gas_type": None,
        "warning_level": None
    }
    
    return alert_data
def determine_warning(value):
    if value >= 12.8 & value <= 19:
        return "경고"
    else:
        return "위험"

def determine_gastype(sensor_id):
    sensor_gas_mapping = {
        1: "인화성 가스",
        2: "이산화탄소",
    }
    gas_type = sensor_gas_mapping.get(sensor_id)
    
    return gas_type



    
