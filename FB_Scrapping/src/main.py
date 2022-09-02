from fastapi import FastAPI
from typing import Dict

app = FastAPI()

## get_all_events to extract all the data from the file
def get_all_events() -> Dict:
    with open("events.json") as events_file:
        data = _json.load(events_file)

    return data

## get_name_events to test if a given name of an event
def get_name_events(name: str) -> Dict:
    events = get_all_events()
    try:
        name_events =events[name]
        print(name_events)
        return name_events
    except:
        return "the name of the event is wrong! PLZ verify the name."


@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/history")
async def history():
    return get_all_events()

@app.get("/name_events/{name}")
async def get_name_events(name: str):
    return get_name_events(name)

