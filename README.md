# ELEC5619-chatbot Iris chatbot AI System

Iris is an intelligent chatbot deliver mental healthcare in a unique way that combines artificial intelligence, zen and rogerian therapy practices.


## Pre-requisites
You will need to prepare following components:
1. Setup Anki Vector Robot SDK https://developer.anki.com/vector/docs
2. Install `ngrok` https://ngrok.com
3. Setup Dialogflow account https://dialogflow.com and create your agent

## Installation

1. Git clone the project to your local computer.
2. Download project requirements (use virtual environment if needed)
```bash
pip install -r requirements.txt
```
3. Run project
```bash
python app.py
```
4. Copy the address and add as webhook to Dialogflow, to do so you use `ngrok` to expose the project as webhook
```bash
# Use the port number where python project is running
ngrok http 5000
```

5. You see a public accessible url like for example "https://ed672d9b.ngrok.io", copy this into your Dialogflow's Fulfilment. 
Be sure to add "/webhook" i.e. "https://ed672d9b.ngrok.io/webhook". Save and your fulfilment to start Iris's advanced function.

6. Go to Telegram, open this url "t.me/meowirisbot" to add Iris as your friend and start chatting!

## Usage
Iris by default will greet you upon first encounter. 

To activate her function, you can ask her "What can you do?" to see the full menu.

Press the option button once the menu is shown.

There is two mode in Iris: 1) Rogerian therapist or 2) Yichan zen monk.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)