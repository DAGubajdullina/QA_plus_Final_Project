# Динара Губайдуллина, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def get_new_orders_track():
    new_orders_track = sender_stand_request.post_new_order()
    return new_orders_track.json()["track"]

def test_getting_order_by_track():
    track = get_new_orders_track()
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200