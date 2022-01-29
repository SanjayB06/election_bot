import pandas as pd
from data.abrevs import codes
import random
# ---------- Pre existing Data ---------
# states ideology
#-------- Ask user for info ----------
# Ideology: 1-100
# Home State

# -------- Ask User Questions --------
#Policy Questions
#answers have corresponding ideology values
# answers affect ideology score
# campaign Questions
# campaign boosts score in state

#------- winner ---------
#go through all states
#libs go for more lib candidate
#cons go for more con candidate
#independents go for more moderate candidate
#take into account answers to campaign question:
#higher score > shifts in that direction

#take into account campaign:
#more visits > shifts in that direction
#take into account region:
#from region> shifts in that direction
#--------- data -----------
state_ideologies = pd.read_csv('data/state_ideologies.csv')
state_ideologies.set_index('state', inplace=True, drop=True)
codes = codes
# ------------------- Candidate Definition--------------------
# candidate_ideology = 75
# candidate_state = "CA"
# comp_ideology = random.randint(0,100)
# comp_state = random.choice(list(codes.values()))
