


# import multiprocessing
# print(multiprocessing.cpu_count())













































# import multiprocessing
# multiprocessing.cpu_count() 






# import multiprocessing
# import time

# def my_process(file_name):
#     print(f"{file_name} has started.")
#     time.sleep(10) 
#     print(f"{file_name} has ended.")

# if __name__ == "__main__":

#     files = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
    
#     p = multiprocessing.Pool()
#     with p:
#         p.map(my_process, files)

#     print("All processes have finished.")








# import datetime
# import hashlib
# import pathlib

# start_time = datetime.datetime.now()
# files = pathlib.Path.cwd() / 'media' / 'film_scan' / 'data'
# for file in files.iterdir():
#     with open(file, 'rb') as f:  
#         file_content = f.read()  
#         result = hashlib.md5(file_content).hexdigest()  

# end_time = datetime.datetime.now()
# print('processing time:', end_time-start_time)











import hashlib
import datetime
import multiprocessing
import pathlib
import time

def my_process(file_name):

    with open(file_name, 'rb') as f:  
        file_content = f.read()  
        result = hashlib.md5(file_content).hexdigest()  

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    files = pathlib.Path.cwd() / 'media' / 'film_scan' / 'data'
    files = [x for x in files.iterdir()]

    p = multiprocessing.Pool()
    with p:
        p.map(my_process, files)
    end_time = datetime.datetime.now()

    print('processing time:', end_time-start_time)