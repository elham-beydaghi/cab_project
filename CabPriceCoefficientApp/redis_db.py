from typing import Union

import ujson
import redis


class RedisDataBaseAccessObject:

    def __int__(self):
        self.redis_client = redis.Redis(host='hostname', port=6379)

    def set_request_id(self, request_id: str) -> None:
        ok_value: bytes = ujson.dumps("ok").encode()
        self.redis_client.set(name=request_id, value=ok_value, ex=600)

    def get_number_of_cabs_in_specific_origin(self, location_suburb: str) -> Union[dict, None]:
        origin = location_suburb.split(":")[0]
        redis_prefix_matching_format = "{}*".format(origin)

        count = 0
        for _ in self.redis_client.scan_iter(redis_prefix_matching_format):
            count += 1
        return count
