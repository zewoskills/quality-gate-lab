from cashback import calculate_cashback


def test_regular_cashback():
    assert calculate_cashback([1000.0, 500.0], is_vip=False) == 30.0


def test_vip_cashback_with_cents():
    assert calculate_cashback([125.0], is_vip=True) == 6.25
