# Python-REST-API-for-AWS

![AWS API](https://github.com/DarshanRaul94/Python-REST-API-for-AWS/blob/master/Screenshots/2march.png)

# Google Firebase Real-time Database to hold the keys for AWS users
![Firebase console](https://github.com/DarshanRaul94/Python-REST-API-for-AWS/blob/master/Screenshots/firebaseconsole.png)
# Pre-requisites:

Make sure that you run ```aws configure``` on the server/machine you will be running it because the code will be using those credentials while executing the code.

# Steps:

1) Download the repository:
```git clone https://github.com/DarshanRaul94/Python-REST-API-for-AWS.git ```

2) Change to that directory:
```cd Python-REST-API-for-AWS```

3) Install all the required python packages:
```pip install --trusted-host pypi.python.org -r requirements.txt```

4) Run the main python file:
```python app.py```

You should get similar output:

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 280-246-667
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
# Steps if you want to containerize the app

1) Run the Docker build command:

```docker build -t <image-name> . ```

2) Check if the image is created:

```docker images```

3) Run the docker image:

```docker run -it -p 8080:8080 <image-name>```

use -d if you want to run in detached mode

```docker run -it -d -p 8080:8080 <image-name>```
