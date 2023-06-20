from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import VertexAI


class EnrichBackend:
    chain: LLMChain

    def request(self, text: str) -> str:
        result = self.chain.run(text=text)

        return result


class OpenAIBackend(EnrichBackend):
    def __init__(self):
        prompt_template = PromptTemplate(
            template='{text}',
            input_variables=['text'],
        )

        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.44, max_tokens=512)

        self.chain = LLMChain(prompt=prompt_template, llm=llm)


class PaLMBackend(EnrichBackend):
    def __init__(self):
        prompt_template = PromptTemplate(
            template='{text}',
            input_variables=['text'],
        )

        llm = VertexAI(model_name='text-bison@001', temperature=0.44, max_output_tokens=512)

        self.chain = LLMChain(prompt=prompt_template, llm=llm)


def run():
    backend = OpenAIBackend()
    return backend.request(text='Complete the sentence: noname security is...')


if __name__ == '__main__':
    print('noname security is...')
    print(run())
