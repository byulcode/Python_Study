# import travel.thailand #모듈이나 패키지만 import 가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

from travel import *    
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))