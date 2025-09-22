from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import os

app = FastAPI(title="Schedule API - Iteration 1")

class TimeSlot(BaseModel):
    start: str = Field(..., example="2025-09-21T09:00:00")
    end: str   = Field(..., example="2025-09-21T09:30:00")
    activity: str = Field(..., example="Estudo")

class ScheduleDay(BaseModel):
    date: str = Field(..., example="2025-09-21")
    slots: List[TimeSlot] = Field(default_factory=list)

@app.get("/health")
def health():
    return {"status": "ok", "service": "schedule-api", "version": "0.1.0"}

# Nesta iteração, apenas ecoamos o payload (sem regras de negócio ainda)
@app.post("/schedule", response_model=ScheduleDay)
def upsert_schedule(payload: ScheduleDay):
    return payload

# Observação: ao rodar no Replit, use host 0.0.0.0 e a porta do ambiente ($PORT)
# Ver passo a passo abaixo.
