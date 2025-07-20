# Story Generator with OpenAI API using Deterministic flows
# Project Summary

This project demonstrates how to integrate OpenAI's GPT models to generate a story based on user input. The process involves:

1. Generating a story outline.
2. Checking the outline's quality and genre.
3. Writing the full story if the outline meets the criteria.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/story_generator.git
   cd story_generator

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ## Usage

1. Run the script:

   ```bash
   python main.py

## Notes
- Ensure you have a valid OpenAI API key set up in a `.env` file.
- The project uses asynchronous programming to handle API requests efficiently.

---

## ✅ Step 5: Run the Project

1.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Script**:
    ```bash
    python main.py
    ```

## Execution Flow

The script `main.py` orchestrates the story generation process as follows:

1.  **User Input**: The program prompts the user to specify what kind of story they want.
2.  **Generate Outline**: The `story_outline_agent` takes the user's input and generates a short story outline.
3.  **Check Outline**: The `outline_checker_agent` evaluates the generated outline for two criteria:
    *   Is it of good quality?
    *   Is it a sci-fi story?
4.  **Conditional Story Generation**:
    *   If the outline is not of good quality or is not a sci-fi story, the program exits.
    *   If the outline passes both checks, the `story_agent` uses the outline to write the full story.
5.  **Output**: The final story is printed to the console.

## Agents

The project uses three distinct agents:

*   `story_outline_agent`:
    *   **Purpose**: To generate a short story outline from the user's prompt.
    *   **Model**: `gpt-4o-mini`
    *   **Output**: `string`

*   `outline_checker_agent`:
    *   **Purpose**: To assess the quality of the outline and verify its genre is sci-fi.
    *   **Model**: `gpt-4o-mini`
    *   **Output**: A `pydantic.BaseModel` containing two boolean fields: `good_quality` and `is_scifi`.

*   `story_agent`:
    *   **Purpose**: To write a complete short story based on the provided outline.
    *   **Model**: `gpt-4o-mini`
    *   **Output**: `string`

## Provide Input:

When prompted, enter the type of story you want (e.g., "a short sci-fi adventure"). The story generation will only proceed if the generated outline is determined to be of good quality and of the sci-fi genre.

📝 Notes
API Key Security: Never hard-code your API key in the source code. Always use environment variables or secure storage mechanisms.

Error Handling: Ensure proper error handling is implemented to manage API limits and potential failures.

Asynchronous Programming: The use of asyncio allows for non-blocking API calls, improving performance.