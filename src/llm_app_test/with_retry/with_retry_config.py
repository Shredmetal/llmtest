from dataclasses import dataclass
from typing import Optional, Tuple, Type


@dataclass
class WithRetryConfig:
    """Configuration data for retry"""
    retry_if_exception_type: Optional[Tuple[Type[BaseException], ...]] = None
    wait_exponential_jitter: Optional[bool] = None
    stop_after_attempt: Optional[int] = None
