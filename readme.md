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

### Sample requests

* TODO: replace with new ones

    ```bash
    curl -d '{"url": "www.helloworld.com"}' -H "Content-Type: application/json" -H "Accept: application/json" -X POST http://localhost:5000/shorten_url
    ``` 