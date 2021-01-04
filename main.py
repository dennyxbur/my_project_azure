from fastapi import FastAPI
import pendulum
from caching.cache_base import ProjectCache


app = FastAPI()
pc = ProjectCache()


@app.get("/ping")
def ping():
    return {"message": "PONG!"}


@app.get("/dow")
def get_dow():
    now = pendulum.now('UTC')
    pc.put()
    return now.format('dddd')


@app.get("/last_call_time")
def get_last_call():
    loc_last = pc.r.get(name="last_call")
    return {"message": "Last API call at :{}".format(loc_last)}
