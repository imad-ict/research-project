import autogen

# Configuration for GPT-4
config_list = [
    {
        'model': 'gpt-4',
        'api_key': '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'
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0.6
}

# Assistant Agents
assistant_data_preparation = autogen.AssistantAgent(
    name="Data_Preparation",
    llm_config=llm_config,
    system_message="Responsible for collecting, annotating, and preprocessing the dataset."
)

assistant_model_development = autogen.AssistantAgent(
    name="Model_Development",
    llm_config=llm_config,
    system_message="Responsible for developing and training the computer vision models."
)

assistant_evaluation = autogen.AssistantAgent(
    name="Evaluation",
    llm_config=llm_config,
    system_message="Responsible for evaluating the models and comparing them with state-of-the-art models."
)

assistant_paper_drafting = autogen.AssistantAgent(
    name="Paper_Drafting",
    llm_config=llm_config,
    system_message="Responsible for drafting, revising, and formatting the research paper."
)

# User Proxy Agent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "cv_research"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

# Tasks
task_data_preparation = """
Collect and prepare a dataset for object detection:
1. Select a relevant dataset.
2. Annotate the dataset for object detection.
3. Preprocess the data to be used for training and testing.
"""

task_model_development = """
Develop the object detection algorithm:
1. Select a suitable model architecture.
2. Train the model on the prepared dataset.
3. Optimize the model for better performance.
"""

task_evaluation = """
Evaluate the developed algorithm:
1. Calculate performance metrics such as accuracy, precision, recall, and F1-score.
2. Compare the model's performance with state-of-the-art models in object detection.
"""

task_paper_drafting = """
Draft the research paper:
1. Write the introduction, literature review, and methodology sections.
2. Document the experiments, results, and discussions.
3. Conclude the paper and suggest future work.
"""

# Initiating tasks via User Proxy Agent
user_proxy.initiate_chat(assistant_data_preparation, message=task_data_preparation)
user_proxy.initiate_chat(assistant_model_development, message=task_model_development)
user_proxy.initiate_chat(assistant_evaluation, message=task_evaluation)
user_proxy.initiate_chat(assistant_paper_drafting, message=task_paper_drafting)
