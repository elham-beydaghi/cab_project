from typing import Union
import ujson
import redis_db

redis_db = redis_db.Redis(host='hostname', port='port')


def set_request_id(request_key: str) -> None:
    ok_value: bytes = ujson.dumps("ok").encode()
    redis_db.set(name=request_key, value=ok_value, ex=600)


def get_number_of_cabs_in_specific_origin(location_suburb: str) -> Union[dict, None]:
    dumped_location_suburb: bytes = redis_db.get(location_suburb)
    if dumped_location_suburb:
        return ujson.loads(dumped_location_suburb.decode())
    return None
