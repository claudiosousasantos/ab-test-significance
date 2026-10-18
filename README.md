# A/B Test Significance Calculator

A Python script that checks whether the difference in conversion rates between two versions of something (like a web page) is statistically significant or could just be random chance.

## How it works
- Takes results for two groups as arrays of 0s and 1s (1 = converted, 0 = did not)
- Calculates each group's conversion rate and the difference between them
- Calculates the standard error for each group and combines them
- Computes a z-score for the difference
- Compares the z-score to 1.96, the cutoff for 95% confidence

## How to run
```bash
python ab_test.py
```

## What I learned
- Using `np.mean()` on an array of 0s and 1s to get a conversion rate directly
- What standard error measures: how much a rate would vary from sample to sample
- Using a z-score to judge whether an observed difference is bigger than random chance would explain
- Using a threshold (1.96 for 95% confidence) to turn a statistic into a yes/no decision

## Limitations
- The sample sizes are very small (20 per group), so the normal approximation behind the z-test is rough. Real A/B tests use hundreds or thousands of users per group.
- A significant result shows a difference is unlikely to be chance, not that the difference is large or important.

## Dependencies
Requires NumPy:
```bash
pip install numpy
```
