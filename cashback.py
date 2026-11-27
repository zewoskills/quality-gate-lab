def calculate_cashback(purchases: list[float], is_vip: bool = False) -> float:
    total = 0.0
    for amount in purchases:
        if amount <= 0:
            continue
        rate = 0.05 if is_vip else 0.02
        total += amount * rate
    return round(total, 2)
