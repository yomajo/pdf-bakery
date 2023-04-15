# PDF Bakery

## About

Example of HTML to PDF conversion problem with dockerized Flask application using [pdfkit](https://pypi.org/project/pdfkit/) and [wkhtmltopdf](https://wkhtmltopdf.org/usage/wkhtmltopdf.txt).

- image encoding
- custom stylesheets
- page breaks
- `wkhtmltopdf` options

![image](https://user-images.githubusercontent.com/45366313/232234385-10974beb-f14f-4183-9349-6c1a136274e0.png)

![image](https://user-images.githubusercontent.com/45366313/232234439-a3d99ea4-fd27-4903-95b3-5fc6d97e2aea.png)


## Requirements

- docker, and preferably `docker compose`
- rename `.env.sample` to `.env` 

Have not run un-dockerized as it requires `wkhtmltopdf` installation on system.

## Run

`docker compose up -d --build`

Play at [127.0.0.1:5000](127.0.0.1:5000)


### Acknowledgements

`wkhtmltopdf` dependencies dokerized by R.S. Thank you, Mate!

