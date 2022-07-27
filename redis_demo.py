import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('name', 'su')
print(r['name'])

r['name1']="su2"
print(r.get('name1'))

print(type(r.get('name1')))


#https://www.jianshu.com/p/2639549bedc8