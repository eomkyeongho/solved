from apscheduler.schedulers.background import BackgroundScheduler
from api.models import User
from collections import deque
from api.crawling import getRating

que = deque(['rudgh9242','citrus_unshiu','seojh0330','qwcol032'])
model = User

def job():
    user_id = que.popleft()
    user_rating = int(getRating(user_id))
    que.append(user_id)
    user = User(id=user_id, rating=user_rating, tier='test')
    user.save()
    getUser = User.objects.get(id=user_id)
    print(getUser.id, getUser.rating, getUser.tier)

def main():
    sched = BackgroundScheduler()
    sched.add_job(job,'interval', seconds=1800, id='test')
    sched.start()