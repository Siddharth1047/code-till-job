import multiprocessing

def sum_of_squares(numbers):
  return sum([x**2 for x in numbers])

if __name__ == "__main__":
  numbers = range(1, 10000)

  #define the number of processes
  num_processes = multiprocessing.cpu_count()

  #split the numbers into sublists for each process
  chunk_size = len(numbers) // num_processes
  number_chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

  #create a pool
  pool = multiprocessing.Pool(processes=num_processes)

  #use map() to distribute the sum_of_squares function across the number_chunks
  results = pool.map(sum_of_squares, number_chunks)

  #close the pool
  pool.close()
  pool.join()

  #final results
  final_result = sum(results)
  print(f"Final Sum is : {final_result}")