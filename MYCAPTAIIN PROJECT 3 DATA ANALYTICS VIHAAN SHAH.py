
import matplotlib.pyplot as plt


cycle_tests = ['Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4']
marks = [85, 76, 92, 81]


plt.bar(cycle_tests, marks)


plt.xlabel('Cycle Tests')
plt.ylabel('Marks')
plt.title('Marks scored in Cycle Tests')


plt.show()
