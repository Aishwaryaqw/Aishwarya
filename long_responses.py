import openai
openai.api_key = "sk-59NUZtqWHiBDn-5RbtG7XCaQSEPJhCEiidOO8w_qjfT3BlbkFJRpo1MKpR_XdIapiaNF0pvdDA4rRnO0Jz702qzV5XIA"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)
