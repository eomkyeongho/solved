from apscheduler.schedulers.background import BackgroundScheduler
from api.models import User
from collections import deque
from api.crawling import getRating
from datetime import datetime

idList = ['laks7985','rudgh9242','citrus_unshiu','seojh0330','qwcol032', 'kjo980822', 'susudjdi', 'cil6092', 'goei300', 'hh6196', 'llsy159', 'sametim', 'xofdus', 'flusha1216', 'ttochi0105']

que = deque(idList)
model = User
tierList = ['Bronze V', 'Bronze IV', 'Bronze III', 'Bronze II', 'Bronze I', 'Silver V', 'Silver IV', 'Silver III', 'Silver II', 'Silver I', 'Gold V', 'Gold IV', 'Gold III', 'Gold II', 'Gold I', 'Platinum V', 'Platinum IV','Platinum III','Platinum II','Platinum I']
tierCut = [30, 60, 90, 120, 150, 200, 300, 400, 500, 650, 800, 950, 1100, 1250, 1400, 1600, 1750, 1900, 2000, 2100]

def updateUser():
    user_id = que.popleft()
    que.append(user_id)
    user_rating = getRating(user_id)
    if user_rating == -1:
        print('Crawling Error! Can not update', user_id)
        return
    user_tier = getTier(user_rating)
    user = User(id=user_id, rating=user_rating, tier=user_tier)
    user.save()
    getUser = User.objects.get(id=user_id)
    now = datetime.now()
    print("Update user →", getUser.id, getUser.rating, getUser.tier, now)

def getTier(rating):
    tier = 'Unrated'
    
    for index in range(0, len(tierList)):
        if rating >= tierCut[index]:
            tier = tierList[index]
    
    return tier

def main():
    sched = BackgroundScheduler()
    sched.add_job(updateUser,'interval', seconds=600, id='updateUserInterval')
    sched.start()



