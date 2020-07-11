from creativecoin import db
from creativecoin.models import Payment, Transaction, User

from datetime import datetime

ROW_PER_PAGE = 3

def retrieve_payments(page, filter_str):
    raw_payments = Payment.query\
        .join(User, Payment.user_id == User.id)\
        .join(Transaction, Payment.txn_id == Transaction.txn_id)\
        .add_columns(User.email, User.firstname, User.lastname, User.phonenumber, Transaction.amount_php, Transaction.amount_usd)\
        .filter(Payment.status==filter_str)\
        .order_by(Payment.created.desc())\
        .paginate(page, ROW_PER_PAGE, False)

    return  raw_payments

def update_payment_status(payment_id, status):
    payment = Payment.query\
        .filter(Payment.id == payment_id)\
        .first()

    payment.status = status
    payment.updated = datetime.now()
    db.session.commit()

    return True
