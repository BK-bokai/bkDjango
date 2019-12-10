import os
from django.conf import settings
print(__file__)#返回此檔案檔名
print(os.path.abspath(__file__))#返回此檔案絕對路徑
print(os.path.dirname(os.path.abspath(__file__)))#返回此路徑的上一層資料夾
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#在上一層資料夾

print(settings.BASE_DIR())
