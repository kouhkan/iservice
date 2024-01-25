from config.celery import celery
from herfeei.orders.selectors.orders import get_incomplete_user_orders
from herfeei.orders.services.orders import change_status_notified

ONE_HOUR = 60 * 60 * 1.0


@celery.task()
def send_sms_incomplete_order() -> None:
    orders = get_incomplete_user_orders(time_passed=6)
    orders = change_status_notified(orders=orders)
    for order in orders:
        print(f"User {orders.user_answer.user} complete your order by [{order.order_trakck_id}")


celery.conf.beat_schedule = {
    "run-send-sms-incomplete-orders": {
        "task": "herfeei.orders.tasks.send_sms_incomplete_order",
        "schedule": ONE_HOUR
    }
}
