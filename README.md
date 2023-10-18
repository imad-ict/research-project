# Research Project on Computer Vision

This repository contains the collaborative work on a Computer Vision (CV) research project, managed using a multi-agent system via the AutoGen framework.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Assistant Agents](#assistant-agents)
- [User Proxy Agent](#user-proxy-agent)
- [Tasks](#tasks)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

The project is focused on developing and evaluating object detection algorithms. The research workflow is organized through multiple AutoGen agents, each handling a distinct aspect of the project: data preparation, model development, evaluation, and paper drafting.

## Getting Started

### Prerequisites

- Install the AutoGen framework as per the official [documentation](https://github.com/microsoft/autogen).
- Install other required libraries: 

### Clone the Repository

```
git clone https://github.com/imad-ict/research-project.git
cd research-project
```

## Assistant Agents

- **Data Preparation Agent**: Handles the collection, annotation, and preprocessing of the dataset.
- **Model Development Agent**: Takes care of developing and training the computer vision models.
- **Evaluation Agent**: Responsible for evaluating the models and comparing them with state-of-the-art models.
- **Paper Drafting Agent**: Manages the drafting, revising, and formatting of the research paper.

## User Proxy Agent

The User Proxy Agent manages the interactions with the assistant agents, initiates tasks, and ensures the tasks are executed as per the specifications.

## Tasks

Detailed task descriptions for each assistant agent can be found in the `work_dir/` directory.

## Running the Project

'''bash
python main.py

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

- Imad Ahmad - imadahmad104@gmail.com
- Project Link: [https://github.com/imad-ict/research-project](https://github.com/imad-ict/research-project)
