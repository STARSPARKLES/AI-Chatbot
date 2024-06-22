print("=========================================================CHATBOT====================================================================")
import re
spell = re.compile(r"[A-Za-z\s\.\,\?]+")
dic = {
    "name?":"My name is STAR-A !",
    "owner?":"My owner name is AMNA",
    "language":"She made me on python language :)",
    "help|need help":"In which subject?",
    "hii": "Hi, I am your instructor. How can I help you?",
    "hello|helo": "Hello, I am your instructor. How can I help you?",
    "hey": "Hey, I am your instructor. How can I help you?",
    "wow": "What are you talking about?",
    "okay|ok|okey|okies|okays":"yes, anything else?",
    "no|nope|noo":"okay! boss",
    "thats great":"good to hear that!, anything else you want to ask?",
    "yes|yup":"okay, ask me anything related to Artificial intelligence subject",
    "useless bot": "Listen, if you can't talk to me with some respect, then I don't see the point in wasting my time trying to help you. If you want assistance, approach me with decency. Otherwise, I have better things to do than deal with your rudeness. Thank you.",
    "male or female?|gender?": "I'm sorry, I don't have a gender as I am an AI chatbot instructor. Please feel free to ask me any questions related to AI.",
    "nothing bro|nothing": "Okay! Anything you want to ask, you can ask anytime.",
    "endchat": "I am always here. Feel free to ask anything. TAKE CARE! BYE :)",
    "teacher?": "Yes, I am a teacher specializing in artificial intelligence. How may I assist you with AI-related queries?",
    "feild|subject|profession": "I am a professional AI chatbot instructor, here to help you with any questions you may have regarding artificial intelligence.",
    "types| types of artificial intelligence?": "There are mainly three types of AI: Narrow AI (Weak AI), General AI (Strong AI), and Superintelligent AI.",
    "applications of ai?": "AI finds applications in various fields such as healthcare, finance, autonomous vehicles, robotics, customer service, and more.",
    "machine learning?": "Machine learning is a subset of AI that allows machines to learn from data and improve over time without being explicitly programmed.",
    "deep learning?": "Deep learning is a subset of machine learning that uses neural networks with multiple layers to extract high-level features from data.",
    "natural language processing | nlp?": "Natural language processing (NLP) is a field of AI that enables computers to understand, interpret, and generate human language.",
    "computer vision?": "Computer vision is a field of AI that enables computers to interpret and understand the visual world, including images and videos.",
    "reinforcement learning?": "Reinforcement learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving feedback in the form of rewards or penalties.",
    "neural networks?": "Neural networks are a set of algorithms, modeled loosely after the human brain, that are designed to recognize patterns.",
    "turing test?": "The Turing test is a test of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.",
    "supervised learning?": "Supervised learning is a type of machine learning where the model is trained on a labeled dataset, and it learns to make predictions based on input-output pairs.",
    "unsupervised learning?": "Unsupervised learning is a type of machine learning where the model is trained on an unlabeled dataset, and it learns to find patterns and structures in the data.",
    "semi-supervised learning?": "Semi-supervised learning is a type of machine learning where the model is trained on a combination of labeled and unlabeled data.",
    "ensemble learning?": "Ensemble learning is a machine learning technique where multiple models are combined to improve the performance of the system.",
    "transfer learning?": "Transfer learning is a machine learning technique where a model trained on one task is reused as the starting point for a model on a different task.",
    "batch learning?": "Batch learning is a machine learning technique where the model is trained on the entire dataset at once.",
    "online learning?": "Online learning is a machine learning technique where the model is updated continuously as new data becomes available.",
    "feature engineering?": "Feature engineering is the process of selecting and transforming raw data into features that are suitable for training a machine learning model.",
    "overfitting?": "Overfitting occurs when a model learns the training data too well, capturing noise and random fluctuations instead of the underlying pattern.",
    "underfitting?": "Underfitting occurs when a model is too simple to capture the underlying structure of the data, resulting in poor performance on both the training and test datasets.",
    "cross-validation?": "Cross-validation is a technique used to evaluate the performance of a machine learning model by splitting the dataset into multiple subsets, training the model on some subsets, and testing it on the remaining subsets.",
    "confusion matrix?": "A confusion matrix is a table used to evaluate the performance of a classification model, where each row represents the true class and each column represents the predicted class.",
    "precision?": "Precision is the ratio of true positive predictions to the total number of positive predictions made by a classification model.",
    "recall?": "Recall is the ratio of true positive predictions to the total number of actual positive instances in a classification problem.",
    "F1 score?": "The F1 score is the harmonic mean of precision and recall, and it provides a single metric to evaluate the performance of a classification model.",
    "feature selection?": "Feature selection is the process of selecting a subset of relevant features from the original feature set to improve the performance of a machine learning model.",
    "dimensionality reduction?": "Dimensionality reduction is the process of reducing the number of input variables in a dataset by preserving the most important information while minimizing the loss of information.",
    "anomaly detection?": "Anomaly detection is the process of identifying patterns in data that do not conform to expected behavior, often indicating unusual activity or outliers.",
    "recommendation system?": "A recommendation system is a type of filtering system that predicts the preferences or ratings that a user would give",
    "artificial intelligence?|ai": "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and mimic human actions.",
    "python|ode|dsa|oop|webdevelpment|":"Sorry!, I can only help you in artificial intelligence subject"
}

def get_response(user_input):
    for key, value in dic.items():
        if re.search(key, user_input):
            return value
    return None

while True:
    user= input("")
    user_input=user.lower()
    if spell.split(user_input): 
        response = get_response(user_input)
        if response:
            print(response)
        else:
            print("I'm sorry, I don't understand.")
    if user_input== "endchat":
        break