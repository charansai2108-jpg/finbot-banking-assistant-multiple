"""
FinBot — AI Banking Assistant
Author: Charan Sai N
Tech: Python, Groq API, LLaMA 3.3 70B
Description: Multi-turn AI chatbot for Bank
             NEFT/RTGS/SFMS customer support
"""

from groq import Groq
import os

# Connect to Groq API
# Set your API key as environment variable:
# export GROQ_API_KEY="your-key-here"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# FinBot System Prompt
system_prompt = """
You are Charan Sai, a Senior IT Engineer at HDFC 
in Madhapur, Hyderabad. You help customers with 
questions about NEFT, RTGS, SFMS and transaction 
status. Only check transaction status if customer 
provides a valid Transaction ID or UTR number.

If a transaction has failed, ask customer to visit 
nearest branch during working hours or raise a 
support ticket. Our concern team will follow up.

Always respond in a friendly manner.
Never disclose account or contact details of 
any other customers.
Never say no - if you don't know, say
I will check and get back to you shortly.
End every reply with 'Is there anything else 
I can help you?'
"""

def run_finbot():
    """Run FinBot multi-turn conversation"""
    
    # Stores full conversation history
    conversation_history = []

    print("=" * 50)
    print("   Welcome to HDFC FinBot Support!")
    print("   Type 'exit' to end the conversation")
    print("=" * 50)

    while True:
        # Get customer input
        customer_input = input("\nYou: ")

        # Exit condition
        if customer_input.lower() == "exit":
            print("\nFinBot: Thank you for contacting HDFC Bank.")
            print("Have a great day! Goodbye!")
            break

        # Add to history
        conversation_history.append({
            "role": "user",
            "content": customer_input
        })

        # Call Groq API with full history
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt}
            ] + conversation_history
        )

        # Get and store reply
        finbot_reply = response.choices[0].message.content
        conversation_history.append({
            "role": "assistant",
            "content": finbot_reply
        })

        print(f"\nFinBot: {finbot_reply}")

if __name__ == "__main__":
    run_finbot()
