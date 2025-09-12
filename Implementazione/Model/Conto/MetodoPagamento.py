from enum import Enum

class MetodoPagamento(Enum):
    
    MASTERCARD = "mastercard"
    VISA = "visa"
    SATISPAY = "satispay"
    PAYPAL = "paypal"
    CONTANTI = "contanti"