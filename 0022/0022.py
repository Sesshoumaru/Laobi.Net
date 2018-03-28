'''
    提取win10壁纸
'''
import os
import shutil
from datetime import datetime


save_folder = os.path.dirname(os.path.realpath(__file__)) + '\wallpapers'
source_folder = os.path.join(os.getenv('LOCALAPPDATA') , 'Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')

print(save_folder)
print(source_folder)

if os.path.exists(save_folder) == False:
    os.mkdir(save_folder)

wallpapers = os.listdir(source_folder)
for wallpaper in wallpapers:
    wallpaper_path = os.path.join(source_folder,wallpaper)

    if (os.path.getsize(wallpaper_path) / 1024) < 150:
        continue
    
    wallpaper_name = wallpaper + '.jpg'
    save_path = os.path.join(save_folder,wallpaper_name)
    shutil.copyfile(wallpaper_path,save_path)

print('save wallpaper success')