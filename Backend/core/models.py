from datetime import datetime, time
from typing import List, Optional
from pydantic import BaseModel


class Category(BaseModel):
    """Representa uma categoria de atividade (ex: Dormir, Lazer)."""
    id: str
    name: str
    color: Optional[str] = None  # cor sugerida para UI


class Activity(BaseModel):
    """Atividade atribuída a um bloco de tempo."""
    id: str
    name: str
    category: Category


class TimeSlot(BaseModel):
    """Bloco de tempo de 30min ou mais (agregado)."""
    start: datetime
    end: datetime
    activity: Activity


class ScheduleDay(BaseModel):
    """Agenda diária completa (24h)."""
    date: datetime
    slots: List[TimeSlot] = []

    def add_slot(self, slot: TimeSlot):
        """Adiciona um bloco de tempo à agenda."""
        self.slots.append(slot)

    def get_slots(self) -> List[TimeSlot]:
        """Retorna todos os blocos de tempo."""
        return self.slots
