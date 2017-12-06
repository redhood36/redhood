# -*- coding: utf-8 -*-


# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Boom Bap Playlist
# Author: Kratos
# Many thanks to Total Revolution for providing the template/base code used for this addon!!!


import os          
import xbmc         
import xbmcaddon  
import xbmcplugin  


from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File


debug        = Addon_Setting(setting='debug')       
addon_id     = xbmcaddon.Addon().getAddonInfo('id')

BASE  = "plugin://plugin.video.youtube/playlist/"


YOUTUBE_CHANNEL_ID_1 = "PLkoA185FDMCNEEkH20pZs_X8YfQAiS_h5"
YOUTUBE_CHANNEL_ID_2 = "PLkoA185FDMCPXoQNq6S-2Cdkeaj6m_3PU"
YOUTUBE_CHANNEL_ID_3 = "PLkoA185FDMCMiHRUWAJoyzh3xmNqytDq1"
YOUTUBE_CHANNEL_ID_4 = "PLkoA185FDMCNJyJTZQ3_YGVSh2Y5FPtC7"
YOUTUBE_CHANNEL_ID_5 = "PLkoA185FDMCN9WTV_HGYT1CrCSSidF2Ev"
YOUTUBE_CHANNEL_ID_6 = "PLkoA185FDMCMpC0_oToBDGK7UgHvCX_HU"
YOUTUBE_CHANNEL_ID_7 = "PLkoA185FDMCP4eM_x8YXG6L7OLxy5_FYn"
YOUTUBE_CHANNEL_ID_8 = "PLkoA185FDMCMfOYILaVthNEbL1jRQQIWA"
YOUTUBE_CHANNEL_ID_9 = "PLkoA185FDMCPzSmQsnztJ69G9WhmjWP6Q"
YOUTUBE_CHANNEL_ID_10 = "PLkoA185FDMCPgxtB7qGb7VgqjNebnTwX7"
YOUTUBE_CHANNEL_ID_11 = "PLkoA185FDMCO-0-cuGyEWjfeA9iywX3n4"
YOUTUBE_CHANNEL_ID_12 = "PLkoA185FDMCNku5EOE-pbv7u4X04hzxFc"
YOUTUBE_CHANNEL_ID_13 = "PLkoA185FDMCOpvnyacv78Pxj-6UM7dGiy"
YOUTUBE_CHANNEL_ID_14 = "PLkoA185FDMCO_DBcOo96IcLKH661rg_I-"
YOUTUBE_CHANNEL_ID_15 = "PLkoA185FDMCMyPUhhpO2-WQrtJ7jyS53x"

@route(mode='main_menu')
def Main_Menu():
    Add_Dir( 
        name="Wu-Tang and affiliated", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://archive.org/download/wumusic/wu.png")
        
    Add_Dir( 
        name="De La Soul", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://archive.org/download/delasoul_201711/dela.png")
        
    Add_Dir( 
        name="Soul Assassins Collection", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://archive.org/download/wumusic/soul.png")
        
    Add_Dir( 
        name="Tribe Called Quest Collection", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://archive.org/download/wumusic/tribe.png")
        
    Add_Dir( 
        name="The Pharcyde Collection", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://archive.org/download/wumusic/pharcyde.png")

    Add_Dir( 
        name="MF Doom Collection", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://archive.org/download/wumusic/doom.png")       

    Add_Dir( 
        name="KRS One-BDP Collection", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://archive.org/download/wumusic/krs.png")
        
    Add_Dir( 
        name="Echoes of Oratory Collection", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://archive.org/download/wumusic/eoo.png")    
 
    Add_Dir( 
        name="Freestyle Fellowship-Project Blowed Collection", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="https://archive.org/download/wumusic/ProjectBlowed.png")

    Add_Dir( 
        name="The Gang Starr Collection", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://archive.org/download/wumusic/gangstarr.png")

    Add_Dir( 
        name="D.I.T.C (Diggin in the Crates) Collection", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="https://archive.org/download/wumusic/ditc.png")

    Add_Dir( 
        name="Boot Camp Click", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="https://archive.org/download/wumusic/bootcamp.png")

    Add_Dir( 
        name="Madlib Collection", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="https://archive.org/download/wumusic/madlib.png")

    Add_Dir( 
        name="Brother J Collection", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="https://archive.org/download/wumusic/brotherj.png")

    Add_Dir( 
        name="Jedi Mind Tricks Collection", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="https://archive.org/download/wumusic/jedimind.png")
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)


if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))