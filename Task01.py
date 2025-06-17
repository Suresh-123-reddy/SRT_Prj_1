import matplotlib.pyplot as plt

# Age group data from the image
age_groups = ["0-20 Years", "21-64 Years", "65+ Years"]
population_millions = [512, 807, 98]

# Create the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(age_groups, population_millions, color=["gold", "deepskyblue", "hotpink"])

# Add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{yval} Mn', ha='center', va='bottom', fontsize=12)

# Title and labels
plt.title("India's Population Distribution by Age in 2022", fontsize=14, weight='bold')
plt.xlabel("Age Groups")
plt.ylabel("Population (in millions)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
