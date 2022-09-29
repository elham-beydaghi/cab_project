import redis

from CabPriceCoefficientApp.apps import CabPriceCoefficientAppConfig


class RedisDataBaseAccessObject:

    def __init__(self):
        self.redis_client = redis.Redis(host=CabPriceCoefficientAppConfig.REDIS_HOST,
                                        port=CabPriceCoefficientAppConfig.REDIS_PORT)

    def set_request_id(self, request_id: str) -> None:
        """
          Set the given request by a formatted key and a dummy value in the redis with ttl of 600.
        """
        ok_value: bytes = "ok".encode()
        self.redis_client.set(name=request_id, value=ok_value, ex=600)

    def get_number_of_cabs_in_specific_origin(self, location_suburb: str) -> int:
        """
          Return the number of requests have been sent in the given region which are not older than 10 minutes.
        """
        origin: str = location_suburb.split(":")[0]
        redis_prefix_matching_format = "{}:*".format(origin)

        return sum(1 for _ in self.redis_client.scan_iter(redis_prefix_matching_format))
