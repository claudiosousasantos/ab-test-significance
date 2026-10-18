import numpy as np

# Step 1: Sample data
group_a = np.array([0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
group_b = np.array([1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])

# Step 2: Conversion rates
conversion_rate_a = np.mean(group_a)
conversion_rate_b = np.mean(group_b)
difference = conversion_rate_b - conversion_rate_a

# Step 3: Standard errors
def standard_error(group):
    p = np.mean(group)
    n = len(group)
    return np.sqrt((p * (1 - p)) / n)

se_a = standard_error(group_a)
se_b = standard_error(group_b)
pooled_se = np.sqrt(se_a**2 + se_b**2)

# Step 4: Z-score
z_score = difference / pooled_se

# Step 5: Results
print(f"Group A conversion rate: {conversion_rate_a:.1%}")
print(f"Group B conversion rate: {conversion_rate_b:.1%}")
print(f"Difference: {difference:.1%}")
print(f"Z-score: {z_score:.2f}")

significance_threshold = 1.96
if abs(z_score) > significance_threshold:
    print("✅ Statistically significant difference — Version B likely performs better")
else:
    print("⚠️ Not statistically significant — difference could be due to random chance")