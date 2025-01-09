from deco_pack.ex17_package import plot_graph
import numpy as np

# Example usage:
@plot_graph
def my_function(x):
  """
  #Returns x and the cosine of x.
  """
  import numpy as np
  y = np.cos(x)
  return x, y

# Call the decorated function
x_values = np.linspace(0, 8 * np.pi, 100)
result = my_function(x_values)