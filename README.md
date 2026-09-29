# PySpark + Databricks CSV Data Chatbot

## Overview

This project combines **PySpark, Databricks, Python, Pandas, JSON, and Pydantic** to create a simple chatbot that can answer questions about Amazon sales data.

The data is first processed and cleaned using **PySpark in Databricks** and then exported as a CSV file. The cleaned data is used by a Python chatbot to answer basic natural-language questions about sales, orders, quantity, categories, and states.

## Project Flow

```text
Amazon Sales CSV
       ↓
   Databricks
       ↓
     PySpark
       ↓
Bronze → Silver → Gold
       ↓
  Cleaned CSV
       ↓
 Python Chatbot
       ↓
JSON + Pydantic
       ↓
Data-based Answer
```

## Technologies Used

* Python
* PySpark
* Databricks
* Pandas
* JSON
* Pydantic
* Git & GitHub

## Databricks Data Processing

The Amazon Sale Report dataset was processed in Databricks using PySpark.

### Bronze Layer

The raw Amazon sales CSV was loaded into Databricks and stored as a Bronze Delta table.

### Silver Layer

The data was cleaned by:

* Removing the unnecessary `Unnamed: 22` column
* Standardizing column names
* Checking for missing values
* Checking for duplicate records
* Removing rows missing important fields such as `order_id`, `sku`, and `date`
* Adding an `is_cancelled` column based on order status

### Gold Layer

Business-level datasets were created for:

* Sales by category
* Sales by state
* Monthly sales

These were stored as Delta tables in Databricks.

## Chatbot

The cleaned data was exported from Databricks as a CSV and used by the Python chatbot.

The chatbot can answer questions such as:

```text
How many orders are there?

What are the total sales?

How many items were sold?

How many orders were cancelled?

Which category has the highest sales?

Which state has the highest sales?
```

The chatbot reads the actual CSV data and performs the required calculations using Pandas.

## JSON Configuration

`config.json` defines the types of queries supported by the chatbot.

Example:

```json
{
    "total_sales": {
        "description": "Find total sales",
        "operation": "sum",
        "column": "amount"
    }
}
```

This keeps the query definitions separate from the Python code.

## Pydantic Validation

Pydantic is used to validate the query intent before processing it.

Example:

```python
class QueryIntent(BaseModel):
    intent: str
```

This provides a structured way of handling chatbot requests.

## Project Structure

```text
csv-chatbot/
│
├── data.csv
├── chatbot.py
├── config.json
├── schema.py
├── test.py
└── README.md
```

### File Description

| File          | Purpose                                     |
| ------------- | ------------------------------------------- |
| `data.csv`    | Cleaned sales data exported from Databricks |
| `chatbot.py`  | Main chatbot and data-processing logic      |
| `config.json` | Supported query definitions                 |
| `schema.py`   | Pydantic validation model                   |
| `test.py`     | Used to test CSV loading                    |
| `README.md`   | Project documentation                       |

## How to Run

### 1. Install dependencies

```bash
pip install pandas pydantic
```

### 2. Make sure the project contains

```text
data.csv
chatbot.py
config.json
schema.py
```

### 3. Run the chatbot

```bash
python chatbot.py
```

### 4. Ask a question

Example:

```text
You: What are the total sales?

Bot: The total sales are ₹...
```

Type:

```text
exit
```

to close the chatbot.

## Learning Outcomes

Through this project, I worked with:

* Loading and processing CSV data using PySpark
* Using Databricks for data processing
* Understanding Bronze, Silver, and Gold data layers
* Cleaning and transforming data
* Creating Delta tables
* Exporting processed data for further use
* Reading CSV data using Pandas
* Using JSON for configuration
* Using Pydantic for data validation
* Building a simple data-driven chatbot
* Managing the project using Git and GitHub

## Future Improvements

Possible improvements include:

* Connecting an LLM for more flexible natural-language queries
* Adding FastAPI as a backend API
* Supporting more complex data queries
* Adding filtering by date, category, or state
* Connecting the chatbot directly to Databricks instead of using an exported CSV
* Adding a simple web interface
