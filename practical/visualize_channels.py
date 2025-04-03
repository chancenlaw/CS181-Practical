import pandas as pd
import matplotlib.pyplot as plt

# Read the training data
train = pd.read_csv('practical/data/train.csv')

# Count the number of entries for each channel
channel_counts = train['channel'].value_counts()

# Create the bar chart
plt.figure(figsize=(12, 6))
channel_counts.plot(kind='bar')
plt.title('Number of Entries per Channel in Training Data')
plt.xlabel('Channel')
plt.ylabel('Number of Entries')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('practical/plots/channel_distribution.png')
plt.close() 