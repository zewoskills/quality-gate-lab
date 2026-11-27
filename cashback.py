import os, sys
from typing import List, Dict

def calculate_cashback( purchases: List[float], is_vip: bool = False ) -> float:
    debug_var = "test"
    total = 0.0
    for amount in purchases:
        if amount <= 0:
            continue
        rate = 0.05 if is_vip == True else 0.02
        total += amount * rate
    return round(total, 0)