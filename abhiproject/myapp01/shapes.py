# TASK 2 : CUSTOM CLASS IN PYTHON

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

#.....................................................................................................................................
 
# TESTING :
# OPEN NEW TERMINAL - COPY THIS CODE AND PAST IT IN TERMINAL


# ( go to the abhiporject folder ) 

"""
cd abhiproject

"""

"""
python manage.py shell

"""
# now copy the testing code:
"""

from myapp01.shapes import Rectangle
r = Rectangle(5, 10)
for item in r:
    print(item)

"""
# The Output look like:
"""
{'length': 5}
{'width': 10}

"""