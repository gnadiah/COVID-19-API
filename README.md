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

###### PHP Usage

```
// Using file_get_contents function
$result = file_get_contents("http://localhost:5000/api/get-world-data/");

// Using PHP cURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_URL, "http://localhost:5000/api/get-world-data/");
$result = curl_exec($ch);
curl_close($ch);

// Convert to Associative array type
$json = json_decode($result, true);

// Convert to Object type
$json = json_decode($result);
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

###### PHP Usage

```
// Using file_get_contents function
$result = file_get_contents("http://localhost:5000/api/get-vn-data/");

// Using PHP cURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_URL, "http://localhost:5000/api/get-vn-data/");
$result = curl_exec($ch);
curl_close($ch);

// Convert to Associative array type
$json = json_decode($result, true);

// Convert to Object type
$json = json_decode($result);
```

---

# INSTALLING DEPENDENCIES

##### Needs Python >= 3.9

##### Open the terminal in the directory have a requirements.txt file

##### Run PIP command to install all dependencies

###### MacOS, Linux or Unix

```
pip3 install -r requirements.txt
```

###### Windows

```
pip install -r requirements.txt
```

---

# INSTRUCTIONS

1. Run the command in "INSTALLING DEPENDENCIES" part
2. Run the app.py in src file with the command below

###### MacOS, Linux or Unix

```
python3 src/app.py
```

###### Windows

```
python src\app.py
```

---

# CREDITS

[Nguyen Hai Dang (ndangmods)](https://github.com/ndangmods/) - API CREATOR

[Viet Trung](https://www.facebook.com/trungsociupro/) - VIETNAM COVID-19 LIVE DATA

[Worldometers](https://www.worldometers.info/) - WORLD COVID-19 LIVE DATA
