import re

patterns_responses = {
    # greetings
    r"(hi|hello|hey|good\s?morning|good\s?afternoon|good\s?evening)":
        "Hello! How can I assist you today?",

    # hours / working time
    r"(what.*hours|opening.*hours|working.*hours|business.*hours|timings)":
        "We are open Monday to Friday from 9 AM to 6 PM, and Saturday 10 AM to 2 PM.",

    # location / address
    r"(where.*located|address|location|branch|office)":
        "We are located at 123 Main Street, Hyderabad. We also have branches in Mumbai and Bengaluru.",

    # contact info
    r"(contact|phone|email|support.*contact)":
        "You can email us at support@example.com or call +91-9876543210.",

    # refund / return
    r"(refund|return.*policy|money.*back|exchange.*policy)":
        "Our refund policy allows returns within 30 days of purchase. Please keep the receipt.",

    # price / cost
    r"(price|cost|charges|how.*much|fees)":
        "Our prices vary by product or service. Could you specify which one you’re interested in?",

    # order status
    r"(order.*status|track.*order|where.*order)":
        "Please provide your order ID so I can check the status for you.",

    # shipping / delivery
    r"(shipping|delivery|how.*long.*deliver|when.*arrive)":
        "We deliver within 3–5 business days. Express shipping is also available.",

    # payment methods
    r"(payment.*methods|pay.*options|accept.*cards|upi|wallets)":
        "We accept all major credit/debit cards, UPI, and popular wallets like Paytm and PhonePe.",

    # account help
    r"(reset.*password|forgot.*password|login.*issue|account.*help)":
        "For account issues, please click 'Forgot Password' on the login page or contact support@example.com.",

    # products
    r"(what.*products|list.*products|services.*offered)":
        "We offer electronics, accessories, and repair services. You can browse our catalog on the website.",

    # offers / discounts
    r"(offers|discounts|coupon|promo)":
        "We frequently run promotional offers! Subscribe to our newsletter to stay updated.",

    # thank you
    r"(thank you|thanks|thx)":
        "You're welcome! Happy to help.",

    # goodbye
    r"(bye|goodbye|see you|exit)":
        "Goodbye! Have a great day.",
}

default_response = (
    "I'm sorry, I didn't understand that. "
    "Could you rephrase your question or contact support@mani.com?"
)

def get_response(user_input):
    """Return a response based on the user's input."""
    text = user_input.lower().strip()
    for pattern, response in patterns_responses.items():
        if re.search(pattern, text):
            return response
    return default_response
