import csv
import random
from datetime import datetime, timedelta

# Configuration
symbols = ['CL=F', 'GC=F', 'SI=F']
actions = ['buy', 'sell']
start_date = datetime(2024, 1, 1)
end_date = datetime(2026, 3, 11)
total_rows = 5000

# Weights for more realistic distribution
symbol_weights = [0.4, 0.35, 0.25]  # CL=F more frequent, SI=F less frequent
action_weights = [0.48, 0.52]  # Slightly more sells than buys

# Generate random data
data = []
date_range = (end_date - start_date).days

for _ in range(total_rows):
    # Random date between start and end (with some clustering for realism)
    random_days = random.randint(0, date_range)
    current_date = start_date + timedelta(days=random_days)
    date_str = current_date.strftime('%Y-%m-%d')
    
    # Random symbol with weights
    symbol = random.choices(symbols, weights=symbol_weights)[0]
    
    # Random action with weights
    action = random.choices(actions, weights=action_weights)[0]
    
    # Random quantity (higher for sells, lower for buys - just for variety)
    if action == 'sell':
        quantity = random.randint(10, 100)
    else:
        quantity = random.randint(1, 50)
    
    data.append([date_str, symbol, action, quantity])

# Sort by date
data.sort(key=lambda x: x[0])

# Write to CSV
filename = 'trading_data.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['date', 'symbol', 'action', 'quantity'])
    writer.writerows(data)

# Print statistics
print(f"Generated {total_rows} rows of trading data in {filename}")
print(f"Date range: {data[0][0]} to {data[-1][0]}")
print(f"\nSymbol distribution:")
for symbol in symbols:
    count = sum(1 for row in data if row[1] == symbol)
    print(f"  {symbol}: {count} rows ({count/total_rows*100:.1f}%)")

print(f"\nAction distribution:")
for action in actions:
    count = sum(1 for row in data if row[2] == action)
    print(f"  {action}: {count} rows ({count/total_rows*100:.1f}%)")

print(f"\nFirst 5 rows:")
for row in data[:5]:
    print(row)