from res_facenet.models import model_920, model_921

DEBUG = True

THREADS_PER_PAGE = 2

APP_NAME = 'Demo Face Embedding'

models = [
    dict(
        model=model_920,
        acc=0.920
    ),
    dict(
        model=model_921,
        acc=.92135
    )
]

USE_MODEL = models[1]

SECRET_KEY = "cBWegL8d367vPzTp9Y2pJudLLtaKi5Jtw8//WsRjZrc="
