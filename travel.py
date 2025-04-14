# import travel.thailand
# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to=ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to=vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
trip_to=thailand.ThailandPackage() # 공개범위를 설정하기 위해 __init__.py 에 Thailand 모듈추가
trip_to.detail()