import matplotlib.pyplot as plt

data = [('A', 10), ('B', 20), ('C', 30)]
color = ['red', 'green', 'blue']
xtics = ['A사', 'B사', 'C사']

        
plt.title("graph test")
plt.bar([k for k, v in data], [v for k, v in data], label = [k for k, v in data], color = color)
plt.xlabel('vender')
plt.ylabel('count')
plt.legend()
plt.show()