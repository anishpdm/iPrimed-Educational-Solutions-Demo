#logging
import logging
import sys
logging.basicConfig(filename='demo.log',level=logging.DEBUG)


x=10
y=10
z=x+y

logging.info(z,exc_info=True)
# print(z)




