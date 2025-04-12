import random
import time

# Custom Exceptions
class InvalidPaymentAmountDetails(Exception):
    pass

class InvalidPaymentDetails(Exception):
    pass

class PaymentGatewayError(Exception):
    pass

def process_payment(user_id, amount, currency="USD", retries=3):
    # validar o user id e o montante
    # 1 e 2
    if not user_id:
        raise InvalidPaymentDetails("Invalid amount.")
    if amount <= 0:
        raise InvalidPaymentAmountDetails("Invalid user ID.")

    supported_currencies = {"USD": 1.0, "EUR": 0.9, "JPY": 110.0}
    # validar a moeda
    # 3
    if currency not in supported_currencies:
        raise InvalidPaymentDetails(f"Unsupported currency: {currency}")

    # Simulate currency conversion
    converted_amount = round(amount * supported_currencies[currency], 2)

    attempt = 0
    while attempt < retries:
        attempt += 1
        try:
            
            # validar se a conecção(?, não com 'x'?) é válida
            
            # Simulate a flaky payment gateway
            if random.random()<0.3:
                raise ConnectionError("Temporary network issue")
            # Simulate success
            transaction_id = f"TXN-{random.randint(100000, 999999)}"
            return {
                "status": "success",
                "transaction_id": transaction_id,
                "amount_charged": converted_amount,
                "currency": currency,
            }

        except ConnectionError as e:
            
            # validar se o erro é de conexão
            
            if attempt >= retries:
                # 4
                raise PaymentGatewayError(f"Payment failed after {retries} attempts.") from e
            time.sleep(0.1 * attempt)  # Exponential backoff