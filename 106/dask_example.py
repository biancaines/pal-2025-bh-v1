from prefect import flow, task
from prefect_dask.task_runners import DaskTaskRunner
import asyncio


@task
async def say_hello(name):
    print(f"hello {name}")


@task
async def say_goodbye(name):
    print(f"goodbye {name}")


@flow(task_runner=DaskTaskRunner())
async def greetings(names):
    for name in names:
        say_hello.submit(name)
        say_goodbye.submit(name)


if __name__ == "__main__":
    asyncio.run(greetings(["arthur", "trillian", "ford", "marvin"]))
