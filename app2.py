from flask import Flask, render_template, request
from base64 import b64decode
from PIL import Image
from io import BytesIO
import boto3
import sudoku3

app = Flask("webcam_sudoku")

@app.route("/input")
def take_image():
  return render_template("webcam3.html")

@app.route("/imagepro" , methods=["GET"])
def process_image():

  #getting the image
  uri_string = request.args.get("ur")
  uri_string = uri_string[uri_string.index(",") + 1:]
  im = Image.open(BytesIO(b64decode(uri_string)))
  im.save('image23.png', 'PNG')

  #putting image in S3
  region = ""
  bucket_name = ""
  filename = "image23.png"
  s3 = boto3.resource("s3")
  s3.Bucket(bucket_name).upload_file(filename, filename)

  #calling Textract
  textract = boto3.client("textract", region_name = region)
  response = textract.analyze_document(
    Document = {
      "S3Object" : {
        "Bucket" : bucket_name,
        "Name" : filename
       }
    },
    FeatureTypes = ["TABLES"]
  )
  
  temp_array = []
  p = 0
  for i in range(1 , 81):
   if p == 81:
       break
   else:
      text = response['Blocks'][i]['Text']
      split_text = text.split(" ")
      chunkf = []
      if (len(split_text) == 9):
          for n in split_text:

              try : temp_array.append(int(n))
              except: temp_array.append(1)
          p += 9

      else:
          try : temp_array.append(int(split_text[0]))
          except: temp_array.append(1)
          p += 1

  sudoku_array = [temp_array[9*x:9*(x+1)] for x in range(9)]

  solved_array = sudoku3.solve(sudoku_array)
  solved_array = [solved_array[9*x:9*(x+1)] for x in range(9)]
 
  
  sa = solved_array
  


  
  
  return render_template("output.html" , 
  a1=sa[0][0] , a2=sa[0][1] , a3=sa[0][2] , a4=sa[0][3] , a5=sa[0][4] , a6=sa[0][5] , a7=sa[0][6] , a8=sa[0][7] , a9=sa[0][8] , 
  a10=sa[1][0] , a11=sa[1][1] , a12=sa[1][2] , a13=sa[1][3] , a14=sa[1][4] , a15=sa[1][5] , a16=sa[1][6] , a17=sa[1][7] , a18=sa[1][8] ,  
  a19=sa[2][0] , a20=sa[2][1] , a21=sa[2][2] , a22=sa[2][3] , a23=sa[2][4] , a24=sa[2][5] , a25=sa[2][6] , a26=sa[2][7] , a27=sa[2][8] ,  
  a28=sa[3][0] , a29=sa[3][1] , a30=sa[3][2] , a31=sa[3][3] , a32=sa[3][4] , a33=sa[3][5] , a34=sa[3][6] , a35=sa[3][7] , a36=sa[3][8] ,  
  a37=sa[4][0] , a38=sa[4][1] , a39=sa[4][2] , a40=sa[4][3] , a41=sa[4][4] , a42=sa[4][5] , a43=sa[4][6] , a44=sa[4][7] , a45=sa[4][8] ,  
  a46=sa[5][0] , a47=sa[5][1] , a48=sa[5][2] , a49=sa[5][3] , a50=sa[5][4] , a51=sa[5][5] , a52=sa[5][6] , a53=sa[5][7] , a54=sa[5][8] ,  
  a55=sa[6][0] , a56=sa[6][1] , a57=sa[6][2] , a58=sa[6][3] , a59=sa[6][4] , a60=sa[6][5] , a61=sa[6][6] , a62=sa[6][7] , a63=sa[6][8] ,  
  a64=sa[7][0] , a65=sa[7][1] , a66=sa[7][2] , a67=sa[7][3] , a68=sa[7][4] , a69=sa[7][5] , a70=sa[7][6] , a71=sa[7][7] , a72=sa[7][8] ,  
  a73=sa[8][0] , a74=sa[8][1] , a75=sa[8][2] , a76=sa[8][3] , a77=sa[8][4] , a78=sa[8][5] , a79=sa[8][6] , a80=sa[8][7] , a81=sa[8][8])

app.run(host="0.0.0.0", port="228")