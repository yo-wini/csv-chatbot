import json
import pandas as pd

from schema import QueryIntent


# Load data
df = pd.read_csv("data.csv")

# Load JSON configuration
with open("config.json", "r") as file:
    config = json.load(file)


def detect_intent(question):
    question = question.lower()

    if "how many orders" in question or "total orders" in question:
        return "total_orders"

    if "total sales" in question or "total revenue" in question:
        return "total_sales"

    if "quantity" in question or "items sold" in question:
        return "total_quantity"

    if "cancelled" in question or "canceled" in question:
        return "cancelled_orders"

    if "category" in question and "sales" in question:
        return "category_sales"

    if "state" in question and "sales" in question:
        return "state_sales"

    return None


def process_query(intent):
    if intent == "total_orders":
        return f"There are {df['order_id'].count():,} orders in the dataset."

    elif intent == "total_sales":
        total = df["amount"].sum()
        return f"The total sales are ₹{total:,.2f}."

    elif intent == "total_quantity":
        quantity = df["qty"].sum()
        return f"The total quantity sold is {quantity:,.0f}."

    elif intent == "cancelled_orders":
        cancelled = (df["status"] == "Cancelled").sum()
        return f"There are {cancelled:,} cancelled orders."

    elif intent == "category_sales":
        result = (
            df.groupby("category")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

        top_category = result.index[0]
        sales = result.iloc[0]

        return f"The category with the highest sales is {top_category}, with ₹{sales:,.2f} in sales."

    elif intent == "state_sales":
        result = (
            df.groupby("ship_state")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

        top_state = result.index[0]
        sales = result.iloc[0]

        return f"The state with the highest sales is {top_state}, with ₹{sales:,.2f} in sales."

    return "I don't understand that question yet."


print("\n================================")
print("       CSV DATA CHATBOT")
print("================================")
print("Ask questions about the sales data.")
print("Type 'exit' to stop.\n")


while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    intent = detect_intent(question)

    if intent is None:
        print("Bot: I don't understand that question yet.")
        continue

    # Pydantic validation
    validated_intent = QueryIntent(intent=intent)

    answer = process_query(validated_intent.intent)

    print("Bot:", answer)
    