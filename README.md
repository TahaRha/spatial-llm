
# SpatialLLM

SpatialLLM is a project focused on creating and managing spatial objects and paths, leveraging LLMs to keep track and use spatial attributes for symbolic reasoning and chain-of-thought.

## Structure

- `src/`: Source code for the project.
- `tests/`: Unit tests for the project.
- `data/`: Example data used in the project.
- `scripts/`: Example scripts to demonstrate usage.

## How to Run

1. **Create a `.env` file**:
   
   Create a `.env` file in the root directory of your project and set the environment variable `OPENAI_API_KEY` to your given OpenAI key.

   ```plaintext
   OPENAI_API_KEY=your_actual_api_key
   ```

2. **Install Dependencies**:
   
   Make sure you have all the necessary dependencies installed. You can create a virtual environment using `conda` or `venv` and install the required packages.

   ```bash
   conda create --name spatial-llm-env python=3.8
   conda activate spatial-llm-env
   pip install -r requirements.txt (use conda with a .yaml otherwise)
   ```

3. **Run Tests**:
   
   You can run all the tests using `unittest` to ensure everything works.

   ```bash
   python -m unittest discover -s tests
   ```

4. **Run Example Scripts**:
   
   Use the example scripts in the `scripts` folder to interact with the spatial system and see how the LLM processes and updates the data.

   ```bash
   python scripts/run_example.py
   ```

## What is Missing

1. **Implement Chain-of-Thought and Symbolic Reasoning**:
   - Implement steps to optimize paths given the space system.
   - This will be useful for future enhancements as more representations and attributes are added to the space system, including virtual and physical spaces.

2. **Kernel Integration for Low Latency**:
   - To achieve low latency and better parallelization, consider refactoring parts of the codebase that do not interact with the LLM directly into a more performant language such as C++, Zig, Rust, or Golang.
   - The goal is to potentially run a similar process inside the kernel of an operating system.

3. **And a lot more..**

## Future Directions

- **Spatial Web Integration**:
  - Explore integration with Spatial Web concepts to create Smart Spaces that are programmable, semantically aware, and securely encrypted.

- **Advanced Mathematical Techniques**:
  - Continue leveraging advanced mathematical techniques like transportation theory, facility location problems, and differential geometry to enhance the spatial system.

## Context

The project involves managing spatial objects and paths, leveraging LLMs for symbolic reasoning and chain-of-thought processing. The focus is on optimizing the spatial configuration for better computing performance and resource management.

**Inspiration**:
A stateful Spatial Web enables smart digital twins of people, physical spaces, and objects to be reliably and securely linked together. The project aims to bring similar capabilities into the kernel of an operating system, enhancing compute speed, caching, and resource management through advanced spatial configurations.
