# AsyncIO in Python
# BAsic code 

# import time
# import asyncio
# import requests

# async def funcation1():
#   await asyncio.sleep(1)
#   print("funcation1")
#   return "Miraj"

# async def funcation2():
#   await asyncio.sleep(1)
#   print("funcation2")

# async def funcation3():
#   await asyncio.sleep(4)
#   print("funcation3")

# async def main():
#   # L = await asyncio.gather(
#   #   funcation1(),
#   #   funcation2(),
#   #   funcation3(),
#   # )
#   # print(L)
  
#   task = asyncio.create_task(funcation1())
#   # await funcation1()
#   await funcation2()
#   await funcation3()

# asyncio.run(main())





# URL ="https://instagram.com/favicon.ico"
# res ponse = requests.get(URL)
# open("instagram.ico","wb"). write(response.content)


# this is main code for asynclo dowlload 

import time
import asyncio
import requests

async def funcation1():
  URL ="https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram.ico","wb"). write(response.content)
  # await asyncio.sleep(1)
  print("funcation1")
  return "Miraj"



async def funcation2():
  URL ="https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram2.ico","wb"). write(response.content)
  # await asyncio.sleep(1)
  print("funcation2")



async def funcation3():
  URL ="https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram3.ico","wb"). write(response.content)
  # await asyncio.sleep(4)
  print("funcation3")

async def main():
  
  L = await asyncio.gather(
    
    funcation1(),
    funcation2(),
    funcation3(),
  )
  print(L)

  # task = asyncio.create_task(funcation1())
  # # await funcation1()
  # await funcation2()
  # await funcation3()

asyncio.run(asy())