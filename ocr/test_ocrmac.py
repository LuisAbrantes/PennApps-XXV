from ocrmac import ocrmac
import time

start_time = time.time()
annotations = ocrmac.OCR('test.png').recognize()
print(annotations)

end_time = time.time() 
execution_time = end_time - start_time 
print(f"Execution Time: {execution_time:.4f} seconds")