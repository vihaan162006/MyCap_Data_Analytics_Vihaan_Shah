import matplotlib.pyplot as plt

# Time of the day
time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']

# Productivity level (Hypothetical data)
productivity_level = [4, 3, 5, 2]

# Create the bar plot
plt.bar(time_of_day, productivity_level)

# Add labels and title
plt.xlabel('Time of the Day')
plt.ylabel('Productivity Level')
plt.title('Productivity Level by Time of the Day')

# Display the plot
plt.show()
