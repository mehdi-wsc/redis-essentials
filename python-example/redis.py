import redis
#CONNECTION TO REDIS SERVER 
redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8") # You cna specify more parameters 



#SE, GET AND DELETE A KEY/VALUE
redis_cli.set("version", "v1.0")
redis_cli.get("version")
redis_cli.delete("version")

#USE json.dumps to convert dictionaries or lists in Python to JSON strings.

import json
product_stock = {"pid": 123, "in_stock": False}
redis_cli.set("product_stock", json.dumps(product_stock))

# SCAN ITER

redis_cli.set("student:john", '{"score": 90, "bonus": 10}')
redis_cli.set("student:tom", '{"score": 80, "bonus": 5}')
for key in redis_cli.scan_iter("student:*"):
    print(redis_cli.get(key))

### REDIS PIPELINE


pubsub = redis_cli.pubsub()  # CREATE A PUBSUB OBJECT
pubsub.subscribe('channel-1') # we don’t need to create a channel explicitly. The channel is created automatically when it is subscribed to for the first time

redis_cli.publish('channel-1', 'value-1') # IT RETURNS THE NUMBER OF SUBSCRIBERS (RECEIVERS)

pubsub.psubscribe('channel-*') # we can subscribe to multiple channels at the same time.

pubsub.get_message() # it delievers message from queue one by one, metadata are considered as messages too, message is composed of : type , pattern,channel and data

