import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace, set_default_openai_api, set_default_openai_client, set_trace_processors
from agents.run import RunConfig
from pydantic import BaseModel
import asyncio

# Load environment variables
load_dotenv()

# Retrieve the OPENAI API key
set_default_openai_api(os.getenv("OPENAI_API_KEY")) 


"""
This example demonstrates a deterministic flow, where each step is performed by an agent.
1. The first agent generates a story outline
2. We feed the outline into the second agent
3. The second agent checks if the outline is good quality and if it is a scifi story
4. If the outline is not good quality or not a scifi story, we stop here
5. If the outline is good quality and a scifi story, we feed the outline into the third agent
6. The third agent writes the story
"""

class OutlineCheckerOutput(BaseModel):
    good_quality: bool
    is_scifi: bool



story_outline_agent = Agent(
    name="story_outline_agent",
    instructions="Generate a very short story outline based on the user's input.",
    model="gpt-4o-mini",
    output_type=str,
)


outline_checker_agent = Agent(
    name="outline_checker_agent",
    instructions="Read the given story outline, and judge the quality. Also, determine if it is a scifi story.",
    output_type=OutlineCheckerOutput,
    model="gpt-4o-mini",
)

story_agent = Agent(
    name="story_agent",
    instructions="Write a short story based on the given outline.",
    output_type=str,
    model="gpt-4o-mini",
)


async def main():
    input_prompt = input("📩 What kind of story do you want? ")

    with trace("✍ Full story flow"):
        # 1. Generate outline
        outline_result = await Runner.run(story_outline_agent, input_prompt)
        print("\n📚 Outline:\n" + outline_result.final_output)

        # 2. Check outline quality and genre
        outline_checker_result = await Runner.run(outline_checker_agent, outline_result.final_output)

        # ✅ Optional debug print
        # print("Debug:", outline_checker_result.raw_output)

        # 3. Gate: Only continue if outline is good and scifi
        result_data = outline_checker_result.final_output
        if not result_data.good_quality:
            print("\n❌ Outline is not good quality. Exiting.")
            return

        if not result_data.is_scifi:
            print("\n⚠ Outline is not sci-fi. Exiting.")
            return

        print("\n✅ Outline is good and sci-fi. Generating full story...\n")

        # 4. Generate story
        story_result = await Runner.run(story_agent, outline_result.final_output)
        print("\n📝 Story:\n" + story_result.final_output)


if __name__ == "__main__":
    asyncio.run(main())













