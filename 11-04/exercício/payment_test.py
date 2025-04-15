import pytest
from unittest.mock import patch
from process_payment import process_payment, InvalidPaymentDetails, PaymentGatewayError, InvalidPaymentAmountDetails

def test_valid_payment():
    # Testa um pagamento válido
    with patch('random.randint', return_value=123456):
        assert process_payment("user_123", 100, "USD") == {
            "status": "success",
            "transaction_id": "TXN-123456",
            "amount_charged": 100.0,
            "currency": "USD",
        }
        
def test_invalid_user_id():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("", 100, "USD")
        
def test_invalid_amount():
    with pytest.raises(InvalidPaymentAmountDetails):
        process_payment("user_123", -1, "USD")
        
def test_invalid_currency():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("user_123", 100, "WTF")
            
def test_exceded_payment_attempts():
    with patch('random.random', side_effect=[0.2, 0.2, 0.2]):
        with pytest.raises(PaymentGatewayError):
            process_payment("user_123", 100, "USD")        