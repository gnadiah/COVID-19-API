# COVID-19 LIVE API

##### API CREATOR - [Nguyen Hai Dang (ndangmods)](https://github.com/ndangmods/)

###### WITH HELP FOR VIETNAM COVID-19 LIVE DATA - [Viet Trung](https://www.facebook.com/trungsociupro/)

###### WITH HELP FOR WORLD COVID-19 LIVE DATA - [Worldometers](https://www.worldometers.info/)

---

# REQUIREMENTS

##### The Windows, Linux or MacOS machine have Python >= 3.9

##### The machine have a PIP library

---

# USAGE

##### Get World COVID-19 Data 

###### cURL Usage

```
curl http://localhost:5000/api/get-world-data/
```

###### Python requests Library Usage

```
import requests

# Get data from API and convert to JSON type
response = requests.get("http://localhost:5000/api/get-world-data/").json()

# Print out the response data
print(response)
```

###### Ajax jQuery Library Usage (JavaScript)

```
$.ajax({
    type: "GET",
    url: "http://localhost:5000/api/get-world-data/",
    dataType: "json",
    crossDomain: true,
    success: function(data) {
        # Variable data is a response data, already convert to JSON type
        # Print out the response data
        console.log(data);
    }
});
```

##### Get Vietnam COVID-19 Data

###### cURL Usage

```
curl http://localhost:5000/api/get-vn-data/
```

###### Python requests Library Usage

```
import requests

# Get data from API and convert to JSON type
response = requests.get("http://localhost:5000/api/get-vn-data/").json()

# Print out the response data
print(response)
```

###### Ajax jQuery Library Usage (JavaScript)

```
$.ajax({
    type: "GET",
    url: "http://localhost:5000/api/get-vn-data/",
    dataType: "json",
    crossDomain: true,
    success: function(data) {
        # Variable data is a response data, already convert to JSON type
        # Print out the response data
        console.log(data);
    }
});
```

---

# INSTALLING DEPENDENCIES

##### Needs Python >= 3.9

##### Open the terminal in the directory have a requirements.txt file

###### Run PIP command to install all dependencies

```
pip3 install -r requirements.txt
```

---

# INSTRUCTIONS

1. Run the command in "INSTALLING DEPENDENCIES" part
2. Run the app.py file with the command `python3 app.py`

---

# CREDITS

[Nguyen Hai Dang (ndangmods)](https://github.com/ndangmods/) - API CREATOR

[Viet Trung](https://www.facebook.com/trungsociupro/) - VIETNAM COVID-19 LIVE DATA

[Worldometers](https://www.worldometers.info/) - WORLD COVID-19 LIVE DATA
