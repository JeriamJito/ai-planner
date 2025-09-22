from core.models import ScheduleDay, TimeSlot, Activity, Category
from fastapi import FastAPI
from core.models import ScheduleDay

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "schedule-api", "version": "0.2.0"}

@app.post("/schedule")
def create_schedule(schedule: ScheduleDay):
    return {"message": "Schedule received", "slots": len(schedule.slots)}
