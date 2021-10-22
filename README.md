![](https://img.shields.io/badge/python-3-orange?style=flat-square)

# web-sudoku
A flask webapp to solve sudoku from image input

![](files/solved1.png)

[Demo link](https://www.linkedin.com/posts/yash-indane-aa6534179_aws-flask-python-activity-6803238011279548416-jjeQ)

## Requirements

```
$ pip install flask
```

```
$ pip install boto3
```

```
$ pip install Pillow
```

## AWS CLI configuration

to configure use the command ->

```
$ aws configure
```

The user should have power to access S3 and Textract services or the user can have Power user and Admin user access.

In the `app2.py` file, region and bucket name should be mentioned

```py
region = ""
bucket_name = ""
```

## How it works

The user first clicks a pic of there sudoku board and submits it. The `data_uri` of the image goes to backend `app2.py` script through the form on user click.
Using `base64`, `ìo` and `PIL` libraries, the image is saved in the server and then uploaded to `S3` bucket. Now using `AWS Textract`, the digits from the image in bucket are extracted and send back to the `app2.py`. This digits in a double array are fed to the function `sudoku3.solve()`, which returns the solution to the problem. This diits are then rendered on the `output.html` page.

Pull requests and new Ideas are welcome!
