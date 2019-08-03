from PIL import Image
from flask import Blueprint, render_template, request, jsonify

from util import is_same, ModelLoaded

base = Blueprint('base', __name__)
THRESHOLD = .6


@base.route('/')
def index():
    return render_template('index.html')


@base.route('/predict', methods=['post'])
def predict():
    files = request.files
    img_left = Image.open(files.get('imgLeft'))
    img_right = Image.open(files.get('imgRight'))
    distance, similar = is_same(img_left, img_right, THRESHOLD)
    model_acc = ModelLoaded.acc
    return jsonify(same=('BERBEDA', 'SAMA')[similar.item()], score=distance.item(),
                   model_acc=model_acc,
                   threshold=THRESHOLD)
