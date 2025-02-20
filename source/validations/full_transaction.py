from pydantic import BaseModel


class ValidateSuccessfulTransaction(BaseModel):
    cart_item_count: int
    total_price: str
    checkout_complete_message: str
