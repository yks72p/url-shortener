# URL Shortener

* Build application with:
    ```bash
    docker-compose build
    ```
 
* Start application with:
    ```bash
    docker-compose up
    ```

    App should start on `http://localhost:5000/`

## Sample requests

* POST

    ```bash
    curl \
    -X POST \
    -H 'Content-Type: application/json' \
    --data-raw '{"original_url":"https://yandex.by"}' \
    http://172.18.0.3:5000/createURL
    ``` 

    sample output:
    ```bash
    {
        "short_link": "http://localhost:5000//getURL/AQM=", 
        "original_url": "https://yandex.by", 
        "expire_date": "2021-12-26"
    }
    ```

* GET:

    ```bash
    curl -X GET http://localhost:5000/getURL/AQE=
    ```

## Load testing

* не змаглі запусьціць Overload на кастамных reqest'ах :(

  сервіс выдаваў альбо 400 Bad Reqest, альбо 500 Internal Error.

* паспрабуем выправіць і дадаць аналіз нагрузкі да заліку


<!-- 73 good
GET /getURL/AQE= HTTP/1.0
Host: 172.18.0.3:5000
User-Agent: xxx (shell 1) 

296 good
POST /createURL HTTP/1.0
Host: 172.18.0.3:5000
User-Agent: xxx (shell 1)
Content-Type: application/json

{"original_url":"https://yandex.by"}

-->