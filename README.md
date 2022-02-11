# Twitch Stream Chat Analyzer - HackSC Project

Created by likhity, eszabo12, victorphan101, and Mnv07 for HackSC 2022.

A chrome extension that analyzes the chat of a twitch stream and displays the percentage positivity of the chat, with 50% meaning a neutral positivity.

![image](/README_assets/stream.PNG)

It gives twitch stream moderators an easy way to monitor the positivity of their stream without having to look at every chat.

## How It Works

When the client's browser is currently on a twitch stream and the user clicks on the chrome extension, the client will connect to Twitch IRC. This is done using [tmi.js](https://tmijs.com/).

The client will then send a stream of the chat to the server, which will perform a sentiment analysis of the chat stream and send back an update of the percentage positivity. The client will then render the percentage update on to the display in the chrome extension.

The user can input how many chats to analyze at a time. For example, if the user selects 10 as this input, every time a new chat arrives to the server, a new sentiment analysis of the last 10 chats is performed. A sentiment analysis on each single chat and returns the mean of the sentiment of all 10 chats.

The server was built using [Flask](https://flask.palletsprojects.com/en/2.0.x/), and all of the client/server communication was done using [Socket.io](https://socket.io/) so that the user gets real-time updates.

The analysis of the chat stream was done using [NLTK's Sentiment Intensity Analyzer](https://www.nltk.org/howto/sentiment.html).

## Try It On Your Machine

To start, make sure you have Python 3.10 installed.

Install the necessary packages:
```bash
$ pip install nltk
$ pip install emoji
$ pip install numpy
$ pip install Flask
$ pip install Flask-RESTful
$ pip install Flask-SocketIO
$ pip install Flask-Cors
```

Clone the repository and start the server.
```bash
$ git clone https://github.com/likhity/hacksc.git
$ cd hacksc
$ cd server
$ python server.py
```

This will start the server on your local machine at [http://127.0.0.1:5000/]. **Do not** close the terminal.

Now, load the extension on chrome.

Go to [chrome://extensions](chrome://extensions).

Make sure developer mode is on.

![image](/README_assets/developer_mode.PNG)

Now, click Load Unpacked.

![image](/README_assets/load_unpacked.PNG)

This will open the file explorer on your computer.

Navigate to the hacksc project directory and open the **client** directory.

You will now have the extension loaded in chrome.

Now, open any active twitch stream in chrome.

Open the extension. 

You should now see the stream's chat being analyzed in real time and the percentage positivity being updated with every new chat.

![image](/README_assets/chrome.PNG)

## Reflection

Developing this project was an absolute nightmare. Dealing with CORS issues and not being able to connect the browser successfully with the server was the bane of our existence.

We didn't eat, or sleep really, and kept working on this project trying to get a working product by the submission deadline.

We unfortunately didn't win but we all learned a lot. All of us went outside of our comfort zones, challenged ourselves, and worked with technologies and tools we never worked with.

However, the most important lesson we learned or at least I did, can't speak for everyone: hackathons are really bad unless you go in person.

*README authored by likhity*