# chatbot_logic.py
def get_response(user_input):
    """
    Rule-based customer service chatbot with interactive-like responses.
    """
    text = user_input.lower().strip()

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
        return (
            "Hello! 👋 Welcome to our support chat.<br>"
            "How can I assist you today?<br>"
            "<small>Quick topics: "
            "<button onclick=\"document.getElementById('userInput').value='Pricing';sendMessage()\">💰 Pricing</button> "
            "<button onclick=\"document.getElementById('userInput').value='Refund';sendMessage()\">↩️ Refund</button> "
            "<button onclick=\"document.getElementById('userInput').value='Delivery';sendMessage()\">🚚 Delivery</button></small>"
        )

    # Working hours
    elif "hours" in text or "timings" in text or "open" in text or "working time" in text:
        return "⏰ Our support team is available <b>Monday to Friday, 9 AM – 6 PM</b>."

    # Pricing / Plans
    elif any(word in text for word in ["price", "cost", "plan", "plans", "subscription"]):
        return (
            "💰 We offer these plans:<ul>"
            "<li>Free</li>"
            "<li>Standard</li>"
            "<li>Premium</li></ul>"
            "<a href='https://example.com/pricing' target='_blank'>View full pricing here</a>"
        )

    # Order tracking
    elif any(word in text for word in ["order status", "track order", "tracking", "where is my order"]):
        return "🔎 Please share your order ID and I’ll help you track it."

    # Refunds / Returns
    elif any(word in text for word in ["refund", "return", "money back", "cancel order"]):
        return (
            "↩️ Refunds are available within 30 days of purchase.<br>"
            "<button onclick=\"document.getElementById('userInput').value='Refund form';sendMessage()\">📄 Send refund form</button>"
        )

    # Contact info
    elif any(word in text for word in ["contact", "phone", "email", "support number", "customer care"]):
        return (
            "📞 You can contact us at <a href='mailto:support@example.com'>support@example.com</a><br>"
            "Or call +1-234-567-8901"
        )

    # Complaints / Issues
    elif any(word in text for word in ["complaint", "problem", "issue", "bug", "error"]):
        return "😔 I'm sorry to hear that. Please describe your issue, and I’ll escalate it."

    # Location / Address
    elif any(word in text for word in ["location", "address", "office", "where are you"]):
        return "📍 Our main office is at 123 Main Street, New York."

    # Discounts / Offers
    elif any(word in text for word in ["discount", "offer", "coupon", "promo code"]):
        return "🎉 We currently offer a 10% discount for new users!"

    # Delivery times
    elif any(word in text for word in ["delivery", "shipping", "how long"]):
        return "🚚 Standard delivery takes 3–5 business days. Express delivery takes 1–2 days."

    # Payment methods
    elif any(word in text for word in ["payment", "pay", "credit card", "debit card", "upi"]):
        return "💳 We accept credit cards, debit cards, UPI, and PayPal."

    # Account creation
    elif any(word in text for word in ["sign up", "create account", "register"]):
        return (
            "📝 You can sign up easily at "
            "<a href='https://example.com/register' target='_blank'>https://example.com/register</a>"
        )

    # Password reset
    elif any(word in text for word in ["reset password", "forgot password", "change password"]):
        return (
            "🔐 Reset your password here: "
            "<a href='https://example.com/reset-password' target='_blank'>Reset Password</a>"
        )

    # Languages
    elif any(word in text for word in ["language", "support language", "languages"]):
        return "🌐 We currently support English, Spanish, and French."

    # Thanks
    elif "thank" in text or "thanks" in text:
        return "😊 You're welcome! Anything else I can assist you with?"

    # Goodbye
    elif any(word in text for word in ["bye", "goodbye", "see you", "exit"]):
        return "👋 Goodbye! Have a wonderful day."

    # Default fallback
    else:
        return (
            "🤔 I'm not sure I understand. Could you rephrase your question?<br>"
            "<small>Try: <button onclick=\"document.getElementById('userInput').value='Pricing';sendMessage()\">Pricing</button> "
            "<button onclick=\"document.getElementById('userInput').value='Refund';sendMessage()\">Refund</button></small>"
        )
