from openai import OpenAI
import time
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('openai_api'))

QA = input("무엇이 궁금한가요?")

my_assistant_id = os.getenv('assistant_id')

thread_id = os.getenv('thread_id')

thread_message = client.beta.threads.messages.create(
  thread_id,
  role="user",
  content=QA,
)

run = client.beta.threads.runs.create(
  thread_id=thread_id,
  assistant_id=my_assistant_id
)

run_id = run.id

while True:
  run = client.beta.threads.runs.retrieve(
  thread_id=thread_id,
  run_id=run_id
  )
  if run.status == "completed":
    break
  else:
    time.sleep(2)
    print("생각 중이에요....")


thread_messages = client.beta.threads.messages.list(thread_id)
print(thread_messages.data[0].content[0].text.value)