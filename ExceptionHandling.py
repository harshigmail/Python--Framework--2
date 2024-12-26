
itemsinCart = 0
# exception method
if itemsinCart != 2:
    raise Exception("product in cart count is not matching")
cycles =0
if cycles != 3:
    raise Exception("Test case failed")

# assertion method
assert(itemsinCart == 2)
# using try catch method , if you want your code execuion shouldn't stop
# except will be executed only if there are any failures in the try method
try:
    with open(filedata.txt, 'r', encoding='utf-8') as file:
        content = file.readline()  # when we to read line by line
        print(content)
except:
    print(" try method is failed so except data printed")

# if you don't want to print above message then leave it
except Exception as e:
    print(e)

finally:
    print(" irrespective of whether try and catchup is passed or failed , the data in finally will be executed ")
