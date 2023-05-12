from aiogram_dialog import Dialog

from payment import payment


def payment_dialogs():
    return [
        Dialog(
            payment.payment_select_window(),
            payment.input_amount_window(),
            payment.payment_qiwi_window(),
            payment.successful_window()
        )
    ]
