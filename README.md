
🎯
I built a Flask-based API that allows users to submit participants and randomly draw a winner. The frontend interacts with the backend using modern fetch() requests, and the data is exchanged via JSON.
-An Api(Application Programming Interfaces) lets the front end to talk to the backend

 The idea sparked when I was practising Function generators - random number
https://www.geeksforgeeks.org/html/javascript-application-for-random-number-generator/
 
Aloterry App was one of the real life ideas i wanted to try,but the winner is chosen in backend part 

lottery_app/
├── app.py
└── static/
    └── index.html

What I learned 

We Use async(used to handle tasks that take time)and await to pause code until a result is ready without freezing the app.

async-Marks a function as asynchronous
await-Waits for a promise to resolve
Benefit	-Non-blocking, cleaner code
Common Uses-API calls, delays, event handling
Flask	-Python tool for building websites or APIs
API	-A system that allows apps to communicate
Endpoint	-A specific URL (like /api/quote) your API responds to
One Endpoint	-Your API has only one route available to use (e.g., /api/quote)

Endpoint	Method	What It Does
/api/add	POST	Adds a participant to the list
/api/draw	GET	Picks and returns a random winner

import random, in function  random.choice(participants) in python to pic a winner



--Challenges--
I spent about 30 minutes trying to get a url in my terminal,I had recieved different feedback using a different flask npm
I tried this one 
python -m pip install flask
then ran the code  

I spend another hour trying to display the hmtl structure on the browser
I found out that my htm file containing javascript was not great

##What I was curious about##

ternary operator - I saw  ? and : from a react code and tried to use it for fun  

random module, gives a random result from the list. It's not "truly" random like quantum randomness, but:

It's unpredictable to users

There's no pattern

No one can "cheat" it from the frontend
