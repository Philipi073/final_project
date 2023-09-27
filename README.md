# Django Chatbot Web Application

This is a Django-based web application that allows users to interact with an AI chatbot powered by OpenAI's GPT-3 model. Users can chat with the chatbot, translate text to different languages, detect the language of a given text, and even generate images based on text prompts.

## Getting Started

To run this web application locally, follow these steps:

### Prerequisites

- Python 3.x
- Django
- OpenAI Python library (`openai`)
- Create a free OpenAI account and get an API key. Replace `'OPENAI_API_KEY'` in the `.env` file with your actual API key.

### Installation

1. Clone this repository to your local machine.

```
git clone <repository-url>
```

2. Change to the project directory.

```
cd final_project
```

3. Install the required Python packages using pip.

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project's root directory and add your OpenAI API key.

```
OPENAI_API_KEY=your-api-key-here
```

### Running the Application

1. Apply database migrations.

```
python manage.py migrate
```

2. Create a superuser for the Django admin panel (optional).

```
python manage.py createsuperuser
```

3. Start the development server.

```
python manage.py runserver
```

4. Access the application in your web browser at `http://localhost:8000`.

## Features

### Chat

- Users can have conversations with the chatbot by entering text messages.
- The chatbot uses OpenAI's GPT-3 model to generate responses.
- Conversations and responses are displayed in real-time.
- ![image](https://github.com/Philipi073/final_project/assets/111244428/e3075355-f49a-435c-9168-bbf8853aa637)
- ![image](https://github.com/Philipi073/final_project/assets/111244428/9631671b-ba03-48bb-a4a9-a6201bc76e32)



### Registration and Authentication

- Users can register for an account with a username, email, and password.
- Registered users can log in and access the chatbot features.

### Language Translation

- Users can translate text to different languages by providing a text input and selecting a target language.
- ![image](https://github.com/Philipi073/final_project/assets/111244428/9f0aac6b-4930-4c89-9263-2a141ac49cde)
 ![image](https://github.com/Philipi073/final_project/assets/111244428/227145e0-cdb3-4545-b817-3bc172f2add6)


### Language Detection

- Users can detect the language of a given text by entering it into the language detection feature.
- ![image](https://github.com/Philipi073/final_project/assets/111244428/c9898f1e-57a9-4590-a353-f4e77f0f9c8c)
- ![image](https://github.com/Philipi073/final_project/assets/111244428/df6fd65d-0f27-44be-8330-ff7cedadcc3b)



### Image Generation

- Users can generate images based on text prompts by providing a description or prompt.
- Images are created using the OpenAI API and displayed to the user.
- ![image](https://github.com/Philipi073/final_project/assets/111244428/d065d08a-5e0d-4617-979e-188fee5b419f)
- ![image](https://github.com/Philipi073/final_project/assets/111244428/2d36a744-60be-4d23-a717-62efc297ecb9)
- ![image](https://github.com/Philipi073/final_project/assets/111244428/a987a6c0-012f-4ef1-b8e5-3bdf4cf41e62)




## Usage

1. Register for an account or log in if you already have one.
2. Access the chatbot by clicking on the "Chat" link in the navigation menu.
3. Start a conversation with the chatbot by entering text messages in the input box.
4. Explore other features such as language translation, language detection, and image generation through the respective links in the navigation menu.

## Troubleshooting

If you encounter any issues while running the application, please check the following:

- Ensure that you have installed all the required Python packages.
- Double-check your OpenAI API key in the `.env` file.
- Make sure the development server is running (`python manage.py runserver`).

If you continue to experience problems, feel free to [contact us](mailto:your-email@example.com) for assistance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This web application was built using Django and OpenAI's GPT-3 model.
- Special thanks to the Django and OpenAI communities for their contributions and support.
