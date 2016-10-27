from pyspark import SparkContext

sc = SparkContext("local", "Euler Prob 1")
limit = range(1000)
result = sc.parallelize(limit) \
.filter(lambda x: x % 3 == 0 or x % 5 == 0) \
.reduce(lambda x, y: x + y)

print result  #233168