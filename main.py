import asyncio


async def main():
  print("Amit")


#main() # gives error of coroutine
asyncio.run(main())  # creating event loop


async def foo():
  print("Amit")
  task = asyncio.create_task(goo("Execute after 3 seconds"))

  print(
    "finished after waiting 3 seconds"
  )  # instead create a task to execute this line means allow this lie to execute as previous LOC is taking time


async def goo(text):

  await asyncio.sleep(3)
  print(text)


asyncio.run(foo())
