![](https://img.shields.io/badge/python-3-orange?style=flat-square)

# web-sudoku
A flask webapp to solve sudoku from image input

![](files/solved1.png)

## Requirements

```
pip install flask
```

```
pip install boto3
```

```
pip install Pillow
```

## AWS CLI configuration

to configure use the command ->

```
aws configure
```

The user should have power to access S3 and Textract services or the user can have Power user and Admin user access.

In the `app2.py` file, region and bucket name should be mentioned

```
region = ""
bucket_name = ""
```


