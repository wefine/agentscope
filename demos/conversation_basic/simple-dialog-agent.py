# -*- coding: utf-8 -*-
"""A simple example for conversation between user and assistant agent."""
import os

import agentscope
from agentscope.agents import DialogAgent
from agentscope.agents.user_agent import UserAgent
from agentscope.pipelines.functional import sequentialpipeline

# 环境变量导入
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

def main() -> None:
    """A basic conversation demo"""

    agentscope.init(
        model_configs=[
            {
                "model_type": "openai_chat",
                "config_name": "gpt4o",
                "model_name": os.environ["OPENAI_MODEL_NAME"],
                "api_key": os.environ["OPENAI_API_KEY"],  # Load from env if not provided
                "organization": "",  # Load from env if not provided
                "generate_args": {
                    "temperature": 0.5,
                },
            },
        ],
        project="Multi-Agent Conversation",
        save_api_invoke=True,
    )

    # Init two agents
    dialog_agent = DialogAgent(
        name="Assistant",
        sys_prompt="You're a helpful assistant.",
        model_config_name="gpt4o",  # replace by your model config name
    )
    user_agent = UserAgent()

    # start the conversation between user and assistant
    x = None
    while x is None or x.content != "exit":
        x = sequentialpipeline([dialog_agent, user_agent], x)


if __name__ == "__main__":
    main()
