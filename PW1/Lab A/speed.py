import decay
import time

n0 = 20000
lam = 0.4
dt = 0.05
steps = 200

# Python loop version
loop_start = time.perf_counter()
decay.simulate_loop(n0, lam, dt=dt, steps=steps)  # stepc -> steps
end_loop = time.perf_counter()
time_loop = end_loop - loop_start
print(f"Python loop version took {time_loop:.4f} seconds")

# Numpy version
start_numpy = time.perf_counter()
decay.simulate(n0, lam, dt=dt, steps=steps)  # stepc=stepc -> steps=steps
end_numpy = time.perf_counter()
time_numpy = end_numpy - start_numpy  # time.numpy -> time_numpy (variable, not attribute)
print(f"Numpy version took {time_numpy:.4f} seconds")

time_ratio = time_loop / time_numpy  # time.time_ratio -> time_ratio
print(f"Numpy version is {time_ratio:.4f} times faster than Python version")
