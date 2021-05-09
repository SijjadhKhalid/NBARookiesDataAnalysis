# -*- coding: utf-8 -*-
"""
Sijjad Khalid
SCM 200
FINAL PROJECT
"""

import pandas as pd
from nba_api.stats.static import players
player_dict = players.get_players()


# GET PLAYER ID'S
Ja_Morant = [player for player in player_dict if player['full_name'] == 'Ja Morant'][0]
Ja_Morant_ID = Ja_Morant['id']

Tyler_Herro = [player for player in player_dict if player['full_name'] == 'Tyler Herro'][0]
Tyler_Herro_ID = Ja_Morant['id']

Brandon_Clarke = [player for player in player_dict if player['full_name'] == 'Brandon Clarke'][0]
Brandon_Clarke_ID = Brandon_Clarke['id']

Kendrick_Nunn = [player for player in player_dict if player['full_name'] == 'Kendrick Nunn'][0]
Kendrick_Nunn_ID = Kendrick_Nunn['id']

PJ_Washington = [player for player in player_dict if player['full_name'] == 'P.J. Washington'][0]
PJ_Washington = PJ_Washington['id']

Zion_Williamson = [player for player in player_dict if player['full_name'] == 'Zion Williamson'][0]
Zion_Williamson_ID = Zion_Williamson['id']

Rui_Hachimura = [player for player in player_dict if player['full_name'] == 'Rui Hachimura'][0]
Rui_Hachimura = Rui_Hachimura['id']

Michael_Porter = [player for player in player_dict if player['full_name'] == 'Michael Porter Jr.'][0]
Michael_Porter_ID = Michael_Porter['id']

Cam_Reddish = [player for player in player_dict if player['full_name'] == 'Cam Reddish'][0]
Cam_Reddish_ID = Cam_Reddish['id']

Eric_Paschall = [player for player in player_dict if player['full_name'] == 'Eric Paschall'][0]
Eric_Paschall_ID = Eric_Paschall['id']

Keldon_Johnson = [player for player in player_dict if player['full_name'] == 'Keldon Johnson'][0]
Keldon_Johnson_ID = Keldon_Johnson['id']

Coby_White = [player for player in player_dict if player['full_name'] == 'Coby White'][0]
Coby_White_ID = Coby_White['id']

Cameron_Johnson = [player for player in player_dict if player['full_name'] == 'Cameron Johnson'][0]
Cameron_Johnson_ID = Cameron_Johnson['id']

DeAndre_Hunter = [player for player in player_dict if player['full_name'] == "De'Andre Hunter"][0]
DeAndre_Hunter_ID = DeAndre_Hunter['id']

Darius_Garland = [player for player in player_dict if player['full_name'] == 'Darius Garland'][0]
Darius_Garland_ID = Darius_Garland['id']

Matisse_Thybulle = [player for player in player_dict if player['full_name'] == 'Matisse Thybulle'][0]
Matisse_Thybulle_ID = Matisse_Thybulle['id']

Kevin_Porter = [player for player in player_dict if player['full_name'] == 'Kevin Porter Jr.'][0]
Kevin_Porter_ID = Kevin_Porter['id']

Ky_Bowman = [player for player in player_dict if player['full_name'] == 'Ky Bowman'][0]
Ky_Bowman_ID = Ky_Bowman['id']

Terence_Davis = [player for player in player_dict if player['full_name'] == 'Terence Davis'][0]
Terence_Davis_ID = Terence_Davis['id']

Jaxson_Hayes = [player for player in player_dict if player['full_name'] == 'Jaxson Hayes'][0]
Jaxson_Hayes_ID = Jaxson_Hayes['id']

Nicolo_Melli = [player for player in player_dict if player['full_name'] == 'Nicolo Melli'][0]
Nicolo_Melli_ID = Nicolo_Melli['id']

Talen_Tucker = [player for player in player_dict if player['full_name'] == 'Talen Horton-Tucker'][0]
Talen_Tucker_ID = Talen_Tucker['id']

Luguentz_Dort = [player for player in player_dict if player['full_name'] == 'Luguentz Dort'][0]
Luguentz_Dort_ID = Luguentz_Dort['id']

RJ_Barrett = [player for player in player_dict if player['full_name'] == 'RJ Barrett'][0]
RJ_Barrett_ID = RJ_Barrett['id']

Jarrett_Culver = [player for player in player_dict if player['full_name'] == 'Jarrett Culver'][0]
Jarrett_Culver_ID = Jarrett_Culver['id']

Jordan_Poole = [player for player in player_dict if player['full_name'] == 'Jordan Poole'][0]
Jordan_Poole_ID = Jordan_Poole['id']

Luka_Samanic = [player for player in player_dict if player['full_name'] == 'Luka Samanic'][0]
Luka_Samanic_ID = Luka_Samanic['id']

Grant_Williams = [player for player in player_dict if player['full_name'] == 'Grant Williams'][0]
Grant_Williams_ID = Grant_Williams['id']

Nickeil_Walker = [player for player in player_dict if player['full_name'] == 'Nickeil Alexander-Walker'][0]
Nickeil_Walker_ID = Nickeil_Walker['id']

Bruno_Fernando = [player for player in player_dict if player['full_name'] == 'Bruno Fernando'][0]
Bruno_Fernando_ID = Bruno_Fernando['id']





from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import time


#GET ALL PLAYERS DATA
gamelog_Ja_Morant = playergamelog.PlayerGameLog(player_id='1629630', season=SeasonAll.all)
gamelog_Ja_Morant_df = gamelog_Ja_Morant.get_data_frames()[0]
time.sleep(.600)
gamelog_Brandon_Clarke = playergamelog.PlayerGameLog(player_id='1629630', season=SeasonAll.all)
gamelog_Brandon_Clarke_df = gamelog_Brandon_Clarke.get_data_frames()[0]
time.sleep(.600)
gamelog_Kendrick_Nunn = playergamelog.PlayerGameLog(player_id='1629134', season=SeasonAll.all)
gamelog_Kendrick_Nunn_df = gamelog_Kendrick_Nunn.get_data_frames()[0]
time.sleep(.600)
gamelog_PJ_Washington  = playergamelog.PlayerGameLog(player_id='1629023', season=SeasonAll.all)
gamelog_PJ_Washington_df = gamelog_PJ_Washington.get_data_frames()[0]
time.sleep(.600)
gamelog_Zion_Williamson  = playergamelog.PlayerGameLog(player_id='1629627', season=SeasonAll.all)
gamelog_Zion_Williamson_df = gamelog_Zion_Williamson.get_data_frames()[0]
time.sleep(.600)
gamelog_Rui_Hachimura  = playergamelog.PlayerGameLog(player_id='1629060', season=SeasonAll.all)
gamelog_Rui_Hachimura_df = gamelog_Rui_Hachimura.get_data_frames()[0]
time.sleep(.600)
gamelog_Tyler_Herro  = playergamelog.PlayerGameLog(player_id='1629060', season=SeasonAll.all)
gamelog_Tyler_Herro_df = gamelog_Tyler_Herro.get_data_frames()[0]
time.sleep(.600)
gamelog_Michael_Porter  = playergamelog.PlayerGameLog(player_id='1629008', season=SeasonAll.all)
gamelog_Michael_Porter_df = gamelog_Michael_Porter.get_data_frames()[0]
time.sleep(.600)
gamelog_Cam_Reddish  = playergamelog.PlayerGameLog(player_id='1629629', season=SeasonAll.all)
gamelog_Cam_Reddish_df = gamelog_Cam_Reddish.get_data_frames()[0]
time.sleep(.600)
gamelog_Eric_Paschall  = playergamelog.PlayerGameLog(player_id='1629672', season=SeasonAll.all)
gamelog_Eric_Paschall_df = gamelog_Eric_Paschall.get_data_frames()[0]
time.sleep(.600)
gamelog_Keldon_Johnson  = playergamelog.PlayerGameLog(player_id='1629640', season=SeasonAll.all)
gamelog_Keldon_Johnson_df = gamelog_Keldon_Johnson.get_data_frames()[0]
time.sleep(.600)
gamelog_Coby_White  = playergamelog.PlayerGameLog(player_id='1629632', season=SeasonAll.all)
gamelog_Coby_White_df = gamelog_Coby_White.get_data_frames()[0]
time.sleep(.600)
gamelog_Cameron_Johnson  = playergamelog.PlayerGameLog(player_id='1629661', season=SeasonAll.all)
gamelog_Cameron_Johnson_df = gamelog_Cameron_Johnson.get_data_frames()[0]
time.sleep(.600)
gamelog_DeAndre_Hunter  = playergamelog.PlayerGameLog(player_id='1629631', season=SeasonAll.all)
gamelog_DeAndre_Hunter_df = gamelog_DeAndre_Hunter.get_data_frames()[0]
time.sleep(.600)
gamelog_Darius_Garland  = playergamelog.PlayerGameLog(player_id='1629636', season=SeasonAll.all)
gamelog_Darius_Garland_df = gamelog_Darius_Garland.get_data_frames()[0]
time.sleep(.600)
gamelog_Matisse_Thybulle  = playergamelog.PlayerGameLog(player_id='1629680', season=SeasonAll.all)
gamelog_Matisse_Thybulle_df = gamelog_Matisse_Thybulle.get_data_frames()[0]
time.sleep(.600)
gamelog_Kevin_Porter  = playergamelog.PlayerGameLog(player_id='1629645', season=SeasonAll.all)
gamelog_Kevin_Porter_df = gamelog_Kevin_Porter.get_data_frames()[0]
time.sleep(.600)
gamelog_Ky_Bowman  = playergamelog.PlayerGameLog(player_id='1629065', season=SeasonAll.all)
gamelog_Ky_Bowman_df = gamelog_Ky_Bowman.get_data_frames()[0]
time.sleep(.600)
gamelog_Terence_Davis  = playergamelog.PlayerGameLog(player_id='1629056', season=SeasonAll.all)
gamelog_Terence_Davis_df = gamelog_Terence_Davis.get_data_frames()[0]
time.sleep(.600)
gamelog_Jaxson_Hayes  = playergamelog.PlayerGameLog(player_id='1629637', season=SeasonAll.all)
gamelog_Jaxson_Hayes_df = gamelog_Jaxson_Hayes.get_data_frames()[0]
time.sleep(.600)
gamelog_Nicolo_Melli  = playergamelog.PlayerGameLog(player_id='1629740', season=SeasonAll.all)
gamelog_Nicolo_Melli_df = gamelog_Nicolo_Melli.get_data_frames()[0]
time.sleep(.600)
gamelog_Talen_Tucker  = playergamelog.PlayerGameLog(player_id='1629659', season=SeasonAll.all)
gamelog_Talen_Tucker_df = gamelog_Talen_Tucker.get_data_frames()[0]
time.sleep(.600)
gamelog_Luguentz_Dort  = playergamelog.PlayerGameLog(player_id='1629652', season=SeasonAll.all)
gamelog_Luguentz_Dort_df = gamelog_Luguentz_Dort.get_data_frames()[0]
time.sleep(.600)
gamelog_RJ_Barrett  = playergamelog.PlayerGameLog(player_id='1629628', season=SeasonAll.all)
gamelog_RJ_Barrett_df = gamelog_RJ_Barrett.get_data_frames()[0]
time.sleep(.600)
gamelog_Jarrett_Culver  = playergamelog.PlayerGameLog(player_id='1629633', season=SeasonAll.all)
gamelog_Jarrett_Culver_df = gamelog_Jarrett_Culver.get_data_frames()[0]
time.sleep(.600)
gamelog_Jordan_Poole  = playergamelog.PlayerGameLog(player_id='1629673', season=SeasonAll.all)
gamelog_Jordan_Poole_df = gamelog_Jordan_Poole.get_data_frames()[0]
time.sleep(.600)
gamelog_Luka_Samanic  = playergamelog.PlayerGameLog(player_id='1629677', season=SeasonAll.all)
gamelog_Luka_Samanic_df = gamelog_Luka_Samanic.get_data_frames()[0]
time.sleep(.600)
gamelog_Grant_Williams  = playergamelog.PlayerGameLog(player_id='1629684', season=SeasonAll.all)
gamelog_Grant_Williams_df = gamelog_Grant_Williams.get_data_frames()[0]
time.sleep(.600)
gamelog_Nickeil_Walker  = playergamelog.PlayerGameLog(player_id='1629638', season=SeasonAll.all)
gamelog_Nickeil_Walker_df = gamelog_Nickeil_Walker.get_data_frames()[0]
time.sleep(.600)
gamelog_Bruno_Fernando = playergamelog.PlayerGameLog(player_id='1628981', season=SeasonAll.all)
gamelog_Bruno_Fernando_df = gamelog_Bruno_Fernando.get_data_frames()[0]
time.sleep(.600)





# PLAYER AVERAGES
Zion_Williamson_avg = gamelog_Zion_Williamson_df.mean(axis=0)
Zion_Williamson_avg_x = pd.DataFrame({'Zion_Williamson_avg':Zion_Williamson_avg})
Zion_Williamson_avg_df = pd.DataFrame.transpose(Zion_Williamson_avg_x)
print("Zion_Williamson_avg")
print(Zion_Williamson_avg)
time.sleep(.600)

Ja_Morant_avg = gamelog_Ja_Morant_df.mean(axis=0)
Ja_Morant_avg_df1 = pd.DataFrame({'Ja_Morant_avg':Ja_Morant_avg})
Ja_Morant_avg_df = pd.DataFrame.transpose(Ja_Morant_avg_df1)
print("Ja_Morant_avg")
print(Ja_Morant_avg)
time.sleep(.600)

Tyler_Herro_avg = gamelog_Tyler_Herro_df.mean(axis=0)
Tyler_Herro_avg_df1 = pd.DataFrame({'Tyler_Herro_avg':Tyler_Herro_avg})
Tyler_Herro_avg_df = pd.DataFrame.transpose(Tyler_Herro_avg_df1)
print("Tyler_Herro_avg")
print(Tyler_Herro_avg)
time.sleep(.600)

Brandon_Clarke_avg = gamelog_Brandon_Clarke_df.mean(axis=0)
Brandon_Clarke_avg_df1 = pd.DataFrame({'Brandon_Clarke_avg':Brandon_Clarke_avg})
Brandon_Clarke_avg_df = pd.DataFrame.transpose(Brandon_Clarke_avg_df1)
print("Brandon_Clarke_avg")
print(Brandon_Clarke_avg)
time.sleep(.600)

Kendrick_Nunn_avg = gamelog_Kendrick_Nunn_df.mean(axis=0)
Kendrick_Nunn_avg_df1 = pd.DataFrame({'Kendrick_Nunn_avg':Kendrick_Nunn_avg})
Kendrick_Nunn_avg_df = pd.DataFrame.transpose(Kendrick_Nunn_avg_df1)
print("Kendrick_Nunn_avg")
print(Kendrick_Nunn_avg)
time.sleep(.600)

PJ_Washington_avg = gamelog_PJ_Washington_df.mean(axis=0)
PJ_Washington_avg_df1 = pd.DataFrame({'PJ_Washington_avg':PJ_Washington_avg})
PJ_Washington_avg_df = pd.DataFrame.transpose(PJ_Washington_avg_df1)
print("PJ_Washington_avg")
print(PJ_Washington_avg)
time.sleep(.600)

Rui_Hachimura_avg = gamelog_Rui_Hachimura_df.mean(axis=0)
Rui_Hachimura_avg_df1 = pd.DataFrame({'Rui_Hachimura_avg':Rui_Hachimura_avg})
Rui_Hachimura_avg_df = pd.DataFrame.transpose(Rui_Hachimura_avg_df1)
print("Rui_Hachimura_avg")
print(Rui_Hachimura_avg)
time.sleep(.600)

Michael_Porter_avg = gamelog_Michael_Porter_df.mean(axis=0)
Michael_Porter_avg_df1 = pd.DataFrame({'Michael_Porter_avg':Michael_Porter_avg})
Michael_Porter_avg_df = pd.DataFrame.transpose(Michael_Porter_avg_df1)
print("Michael_Porter_avg")
print(Michael_Porter_avg)
time.sleep(.600)

Cam_Reddish_avg = gamelog_Cam_Reddish_df.mean(axis=0)
Cam_Reddish_avg_df1 = pd.DataFrame({'Cam_Reddish_avg':Cam_Reddish_avg})
Cam_Reddish_avg_df = pd.DataFrame.transpose(Cam_Reddish_avg_df1)
print("Cam_Reddish_avg")
print(Cam_Reddish_avg)
time.sleep(.600)

Eric_Paschall_avg = gamelog_Eric_Paschall_df.mean(axis=0)
Eric_Paschall_avg_df1 = pd.DataFrame({'Eric_Paschall_avg':Eric_Paschall_avg})
Eric_Paschall_avg_df = pd.DataFrame.transpose(Eric_Paschall_avg_df1)
print("Eric_Paschall_avg")
print(Eric_Paschall_avg)
time.sleep(.600)

Keldon_Johnson_avg = gamelog_Keldon_Johnson_df.mean(axis=0)
Keldon_Johnson_avg_df1 = pd.DataFrame({'Keldon_Johnson_avg':Keldon_Johnson_avg})
Keldon_Johnson_avg_df = pd.DataFrame.transpose(Keldon_Johnson_avg_df1)
print("Keldon_Johnson_avg")
print(Keldon_Johnson_avg)
time.sleep(.600)

Coby_White_avg = gamelog_Coby_White_df.mean(axis=0)
Coby_White_avg_df1 = pd.DataFrame({'Coby_White_avg':Coby_White_avg})
Coby_White_avg_df = pd.DataFrame.transpose(Coby_White_avg_df1)
print("Coby_White_avg")
print(Coby_White_avg)
time.sleep(.600)

Cameron_Johnson_avg = gamelog_Cameron_Johnson_df.mean(axis=0)
Cameron_Johnson_avg_df1 = pd.DataFrame({'Cameron_Johnson_avg':Cameron_Johnson_avg})
Cameron_Johnson_avg_df = pd.DataFrame.transpose(Cameron_Johnson_avg_df1)
print("Cameron_Johnson_avg")
print(Cameron_Johnson_avg)
time.sleep(.600)

DeAndre_Hunter_avg = gamelog_DeAndre_Hunter_df.mean(axis=0)
DeAndre_Hunter_avg_df1 = pd.DataFrame({'DeAndre_Hunter_avg':DeAndre_Hunter_avg})
DeAndre_Hunter_avg_df = pd.DataFrame.transpose(DeAndre_Hunter_avg_df1)
print("DeAndre_Hunter_avg")
print(DeAndre_Hunter_avg)
time.sleep(.600)

Darius_Garland_avg = gamelog_Darius_Garland_df.mean(axis=0)
Darius_Garland_avg_df1 = pd.DataFrame({'Darius_Garland_avg':Darius_Garland_avg})
Darius_Garland_avg_df = pd.DataFrame.transpose(Darius_Garland_avg_df1)
print("Darius_Garland_avg")
print(Darius_Garland_avg)
time.sleep(.600)

Matisse_Thybulle_avg = gamelog_Matisse_Thybulle_df.mean(axis=0)
Matisse_Thybulle_avg_df1 = pd.DataFrame({'Matisse_Thybulle_avg':Matisse_Thybulle_avg})
Matisse_Thybulle_avg_df = pd.DataFrame.transpose(Matisse_Thybulle_avg_df1)
print("Matisse_Thybulle_avg")
print(Matisse_Thybulle_avg)
time.sleep(.600)

Kevin_Porter_avg = gamelog_Kevin_Porter_df.mean(axis=0)
Kevin_Porter_avg_df1 = pd.DataFrame({'Kevin_Porter_avg':Kevin_Porter_avg})
Kevin_Porter_avg_df = pd.DataFrame.transpose(Kevin_Porter_avg_df1)
print("Kevin_Porter_avg")
print(Kevin_Porter_avg)
time.sleep(.600)

Ky_Bowman_avg = gamelog_Ky_Bowman_df.mean(axis=0)
Ky_Bowman_avg_df1 = pd.DataFrame({'Ky_Bowman_avg':Ky_Bowman_avg})
Ky_Bowman_avg_df = pd.DataFrame.transpose(Ky_Bowman_avg_df1)
print("Ky_Bowman_avg")
print(Ky_Bowman_avg)
time.sleep(.600)

Terence_Davis_avg = gamelog_Terence_Davis_df.mean(axis=0)
Terence_Davis_avg_df1 = pd.DataFrame({'Terence_Davis_avg':Terence_Davis_avg})
Terence_Davis_avg_df = pd.DataFrame.transpose(Terence_Davis_avg_df1)
print("Terence_Davis_avg")
print(Terence_Davis_avg)
time.sleep(.600)

Jaxson_Hayes_avg = gamelog_Jaxson_Hayes_df.mean(axis=0)
Jaxson_Hayes_avg_df1 = pd.DataFrame({'Jaxson_Hayes_avg':Jaxson_Hayes_avg})
Jaxson_Hayes_avg_df = pd.DataFrame.transpose(Jaxson_Hayes_avg_df1)
print("Jaxson_Hayes_avg")
print(Jaxson_Hayes_avg)
time.sleep(.600)

Nicolo_Melli_avg = gamelog_Nicolo_Melli_df.mean(axis=0)
Nicolo_Melli_avg_df1 = pd.DataFrame({'Nicolo_Melli_avg':Nicolo_Melli_avg})
Nicolo_Melli_avg_df = pd.DataFrame.transpose(Nicolo_Melli_avg_df1)
print("Nicolo_Melli_avg")
print(Nicolo_Melli_avg)
time.sleep(.600)

Talen_Tucker_avg = gamelog_Talen_Tucker_df.mean(axis=0)
Talen_Tucker_avg_df1 = pd.DataFrame({'Talen_Tucker_avg':Talen_Tucker_avg})
Talen_Tucker_avg_df = pd.DataFrame.transpose(Talen_Tucker_avg_df1)
print("Talen_Tucker_avg")
print(Talen_Tucker_avg)
time.sleep(.600)

Luguentz_Dort_avg = gamelog_Luguentz_Dort_df.mean(axis=0)
Luguentz_Dort_avg_df1 = pd.DataFrame({'Luguentz_Dort_avg':Luguentz_Dort_avg})
Luguentz_Dort_avg_df = pd.DataFrame.transpose(Luguentz_Dort_avg_df1)
print("Luguentz_Dort_avg")
print(Luguentz_Dort_avg)
time.sleep(.600)

RJ_Barrett_avg = gamelog_RJ_Barrett_df.mean(axis=0)
RJ_Barrett_avg_df1 = pd.DataFrame({'RJ_Barrett_avg':RJ_Barrett_avg})
RJ_Barrett_avg_df = pd.DataFrame.transpose(RJ_Barrett_avg_df1)
print("RJ_Barrett_avg")
print(RJ_Barrett_avg)
time.sleep(.600)

Jarrett_Culver_avg = gamelog_Jarrett_Culver_df.mean(axis=0)
Jarrett_Culver_avg_df1 = pd.DataFrame({'Jarrett_Culver_avg':Jarrett_Culver_avg})
Jarrett_Culver_avg_df = pd.DataFrame.transpose(Jarrett_Culver_avg_df1)
print("Jarrett_Culver_avg")
print(Jarrett_Culver_avg)
time.sleep(.600)

Jordan_Poole_avg = gamelog_Jordan_Poole_df.mean(axis=0)
Jordan_Poole_avg_df1 = pd.DataFrame({'Jordan_Poole_avg':Jordan_Poole_avg})
Jordan_Poole_avg_df = pd.DataFrame.transpose(Jordan_Poole_avg_df1)
print("Jordan_Poole_avg")
print(Jordan_Poole_avg)
time.sleep(.600)

Luka_Samanic_avg = gamelog_Luka_Samanic_df.mean(axis=0)
Luka_Samanic_avg_df1 = pd.DataFrame({'Luka_Samanic_avg':Luka_Samanic_avg})
Luka_Samanic_avg_df = pd.DataFrame.transpose(Luka_Samanic_avg_df1)
print("Luka_Samanic_avg")
print(Luka_Samanic_avg)
time.sleep(.600)

Grant_Williams_avg = gamelog_Grant_Williams_df.mean(axis=0)
Grant_Williams_avg_df1 = pd.DataFrame({'Grant_Williams_avg':Grant_Williams_avg})
Grant_Williams_avg_df = pd.DataFrame.transpose(Grant_Williams_avg_df1)
print("Grant_Williams_avg")
print(Grant_Williams_avg)
time.sleep(.600)

Nickeil_Walker_avg = gamelog_Nickeil_Walker_df.mean(axis=0)
Nickeil_Walker_avg_df1 = pd.DataFrame({'Nickeil_Walker_avg':Nickeil_Walker_avg})
Nickeil_Walker_avg_df = pd.DataFrame.transpose(Nickeil_Walker_avg_df1)
print("Nickeil_Walker_avg")
print(Nickeil_Walker_avg)
time.sleep(.600)

Bruno_Fernando_avg = gamelog_Bruno_Fernando_df.mean(axis=0)
Bruno_Fernando_avg_df1 = pd.DataFrame({'Bruno_Fernando_avg':Bruno_Fernando_avg})
Bruno_Fernando_avg_df = pd.DataFrame.transpose(Bruno_Fernando_avg_df1)
print("Bruno_Fernando_avg")
print(Bruno_Fernando_avg)
time.sleep(.600)





# JOIN AVERAGES
players_avg_join = pd.concat([Bruno_Fernando_avg_df,
                              Nickeil_Walker_avg_df,
                              Grant_Williams_avg_df,
                              Luka_Samanic_avg_df,
                              Jordan_Poole_avg_df, 
                              Jarrett_Culver_avg_df, 
                              RJ_Barrett_avg_df, 
                              Luguentz_Dort_avg_df, 
                              Talen_Tucker_avg_df, 
                              Nicolo_Melli_avg_df, 
                              Jaxson_Hayes_avg_df, 
                              Terence_Davis_avg_df, 
                              Ky_Bowman_avg_df, 
                              Kevin_Porter_avg_df, 
                              Matisse_Thybulle_avg_df, 
                              Darius_Garland_avg_df, 
                              DeAndre_Hunter_avg_df, 
                              Cameron_Johnson_avg_df, 
                              Coby_White_avg_df, 
                              Keldon_Johnson_avg_df, 
                              Eric_Paschall_avg_df, 
                              Cam_Reddish_avg_df, 
                              Michael_Porter_avg_df, 
                              Rui_Hachimura_avg_df, 
                              PJ_Washington_avg_df, 
                              Kendrick_Nunn_avg_df, 
                              Brandon_Clarke_avg_df, 
                              Tyler_Herro_avg_df, 
                              Ja_Morant_avg_df, 
                              Zion_Williamson_avg_df], axis=0, sort=False)


players_avg_join.drop('SEASON_ID', inplace=True, axis=1)
players_avg_join.drop('Player_ID', inplace=True, axis=1)
players_avg_join.drop('Game_ID', inplace=True, axis=1)
players_avg_join.drop('VIDEO_AVAILABLE', inplace=True, axis=1)

players_avg_join.rename(columns={'Index':'Player_Name'}, inplace=True)



import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


# GRAPHING NAME VS FGM AVERAGE
x_Index = players_avg_join.index.str[:3]
Y_FGM = players_avg_join.FGM
plt.figure(figsize=(9, 7), dpi=80)
plt.bar(x_Index, Y_FGM, width=.4)
plt.title("TOP PERFORMED FGM", fontweight='bold')
plt.xticks(color='r', fontsize=7.5)
plt.xlabel("Player", fontweight='bold')
plt.ylabel("FGM AVERAGE", fontweight='bold')



# CALCLATE FIELD GOAL PERCENTAGE
plt.figure(figsize=(9, 7), dpi=80)
players_avg_join['FGP_MANUAL']=  (players_avg_join['FGM'] / players_avg_join['FGA']*100) 
x_Index = players_avg_join.index.str[:3]
Y_FGM = players_avg_join.FGP_MANUAL

plt.bar(x_Index, Y_FGM, width=.4)
plt.title("Players FGP", fontweight='bold')
plt.xticks(color='r', fontsize=7.5)
plt.xlabel("Player", fontweight='bold')
plt.ylabel("FIELD GOAL PERCENTAGE", fontweight='bold')
plt.show()




# CALCULATE AVERAGE POINTS SCORED PER GAME
plt.figure(figsize=(9, 7), dpi=80)
x_Index = players_avg_join.index.str[:3]
Y_FGM = players_avg_join.PTS
plt.bar(x_Index, Y_FGM, width=.4)
plt.title("Players Average Points Per Game", fontweight='bold')
plt.xticks(color='r', fontsize=7.5)
plt.xlabel("Player", fontweight='bold')
plt.ylabel("Average Points Per Game", fontweight='bold')
plt.show()




# ZION WILLIAMSON PROGRESS
plt.figure(figsize=(9, 7), dpi=80)
x_Index = gamelog_Zion_Williamson_df.index
Y_FGM = gamelog_Zion_Williamson_df.PTS
plt.scatter(x_Index, Y_FGM)
plt.title("Zion WILLIAMSONS' Progress", fontweight='bold')
plt.xticks(color='r', fontsize=7.5)
plt.xlabel("RECENT[0] TO OLDEST[79]", fontweight='bold')
plt.ylabel("Points Scored", fontweight='bold')
plt.show()




# JA MORANT PROGRESS
plt.figure(figsize=(9, 7), dpi=80)
x_Index = gamelog_Ja_Morant_df.index
Y_FGM = gamelog_Ja_Morant_df.PTS
plt.scatter(x_Index, Y_FGM)
plt.title("JA MORANTs' Progress", fontweight='bold')
plt.xticks(color='r', fontsize=7.5)
plt.xlabel("RECENT[0] TO OLDEST[79]", fontweight='bold')
plt.ylabel("Points Scored", fontweight='bold')
plt.show()









