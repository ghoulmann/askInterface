import openai
import config
from yaspin import yaspin

openai.api_key = config.OPENAI_API_KEY

@yaspin(text="Waiting for response from open AI")
def openAICompletion(query):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.8,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    if "choices" in response:
        if len(response["choices"]) > 0:
            answer = response["choices"][0]["text"]
        else:
            answer = "Opps sorry, you beat the AI this time"

    return answer

@yaspin(text="Waiting for response from open AI")
def openAIEdit(directions, source):
    response = openai.Edit.create(
        model="text-davinci-edit-001", input=source, instruction=directions, n=20
    )

    if "choices" in response:
        if len(response["choices"]) > 0:
            response = response["choices"][0]["text"]
        else:
            response = "Opps sorry, you beat the AI this time"

    return response


@yaspin(text="Waiting for response from open AI")
def generatEmail(query):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.8,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.36,
        presence_penalty=0.75,
    )

    if "choices" in response:
        if len(response["choices"]) > 0:
            answer = response["choices"][0]["text"]
        else:
            answer = "Opps sorry, you beat the AI this time"

    return answer
