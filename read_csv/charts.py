import matplotlib.pyplot as plt

def generate_bar_char(labels,values,country):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'bar_{country}.png')
  plt.close()

def generate_pie_char(labels,values,country):
  fig, ax = plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.savefig(f'pie_{country}.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a','b','c']
  values = [100,200,300]
  generate_bar_char(labels,values)
  generate_pie_char(labels,values)