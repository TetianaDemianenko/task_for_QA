import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.lpush("name", "Ben")
r.lpush("name", "Cary")
r.lpush("name", "Alex")
r.lpush("name", "Andrew")
r.lpush("name", "Elvis")
r.lpush("name", "George")
r.lpush("name", "Joe")

r.lpush("position", "Project manager")
r.lpush("position", "Software tester")
r.lpush("position", "Systems analyst")
r.lpush("position", "Web developer")
r.lpush("position", "Network designer")
r.lpush("position", "Helpdesk support")
r.lpush("position", "Business analyst")
r.lpush("position", "QA")
