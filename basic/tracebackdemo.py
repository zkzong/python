# author: admin
# date: 2022/5/12 15:15
import traceback
try:
    print('-----------')
    print(1/0)
except:
    traceback.print_exc()