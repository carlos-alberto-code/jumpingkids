from enum import Enum, auto
from datetime import datetime
from dataclasses import dataclass


class SubscriptionPeriod(Enum):
    MONTH = auto()
    QUARTER = auto()
    HALF_YEAR = auto()
    YEAR = auto()


class SubscriptionStatus(Enum):
    ACTIVE = auto()
    EXPIRED = auto()
    CANCELLED = auto()
    PENDING = auto()


class SubscriptionType(Enum):
    FREE = auto()
    PREMIUM = auto()


@dataclass
class SubscriptionPlan:
    id: int
    type: SubscriptionType
    price: float


@dataclass
class Subscription:
    id: int
    tutor_id: int
    plan: SubscriptionPlan
    period: SubscriptionPeriod
    status: SubscriptionStatus
    start_date: datetime
    end_date: datetime

    @property
    def is_active(self) -> bool:
        return self.status == SubscriptionStatus.ACTIVE
    
    @property
    def today(self) -> datetime:
        return datetime.now()
    
    @property
    def remaining_days(self) -> int:
        if not self.is_active:
            return 0
        if self.today > self.end_date:
            return 0
        return (self.end_date - self.today).days
    