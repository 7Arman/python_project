import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("budget.csv")

# Plot a pie chart
plt.figure(figsize=(6,6))
plt.pie(data["Amount"], labels=data["Category"], autopct="%1.1f%%", startangle=140)
plt.title("Monthly Personal Budget")
plt.tight_layout()

# Save and show the chart
plt.savefig("budget_chart.png")
plt.show()
