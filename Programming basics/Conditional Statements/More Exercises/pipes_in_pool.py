pool_volume_l = int(input())
first_pipe_debit_h = int(input())
second_pipe_debit_h = int(input())
worker_absent_h = float(input())
pipe_1 = first_pipe_debit_h * worker_absent_h
pipe_2 = second_pipe_debit_h * worker_absent_h
all_pipes = pipe_1 + pipe_2

if all_pipes > pool_volume_l:
    print(f"For {worker_absent_h:.2f} hours the pool overflows with {all_pipes - pool_volume_l:.2f} liters.")
else:
    print(f"The pool is {(all_pipes / pool_volume_l) * 100:.2f}% full. Pipe 1: {(pipe_1 / all_pipes) * 100:.2f}%. Pipe 2: {(pipe_2 / all_pipes) * 100:.2f}%.")
