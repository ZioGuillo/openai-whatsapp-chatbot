from setuptools import find_packages, setup

setup(
    name="openai-agent",
    packages=find_packages("openai-chatbot"),
    version="0.1.0",
    description="A Whatsapp bot to talk with OpenAI's GTP-3 language model using their private API.",
    author="Simon E. Sanchez Viloria (simonsanvil)",
    license="MIT",
)
