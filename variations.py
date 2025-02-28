import json
import random

# Possible values
customers = [100, 200, 300, 400, 500]
order_values = [5.0, 7.5, 9.0, 12.0]
operating_hours = [8, 10, 12, 14]
marketing_spend = [50, 100, 200, 500]
foot_traffic = [200, 400, 600, 800]

# Generate 500 examples
examples = []
for _ in range(50):
    c = random.choice(customers)
    o = random.choice(order_values)
    h = random.choice(operating_hours)
    m = random.choice(marketing_spend)
    f = random.choice(foot_traffic)
    
    prompt = f"My coffee shop has {c} daily customers, an average order value of ${o:.2f}, and operates for {h} hours. I spend ${m:.2f} on marketing, and my foot traffic is {f}. How can I increase revenue?"
    response = f"Based on your data, focus on these areas: 1) Increase marketing ROI by targeting local audiences. 2) Upsell higher-margin items. 3) Consider adjusting store hours to align with peak foot traffic. 4) Offer promotions to attract new customers."

    examples.append({"messages": [
        {"role": "system", "content": "You are a business consultant specializing in coffee shop revenue optimization."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response}
    ]})

# Save to JSONL
with open("coffee_shop_finetune.jsonl", "w") as f:
    for example in examples:
        f.write(json.dumps(example) + "\n")
