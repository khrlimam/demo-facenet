# Demo Face Embedding with Trained Facenet Model
The pretrained model can be found at [khrlimam/res-facenet](https://github.com/khrlimam/res-facenet). Please open that repo If you want to do _transfer learning_.

### Steps to test this app
  1. `pip install -r requirements.txt`
  2. `export FLASK_APP=server.py`
  3. `export FLASK-DEBUG=True`
  4. `flask run`
  
### Try the deployed demo app:
https://demo-facenet.herokuapp.com

You can switch which model to use in `config.py` file