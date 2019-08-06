from PIL import Image
from flask import Blueprint, render_template, request, jsonify
from torch_mtcnn import detect_faces

from util import is_same, ModelLoaded

base = Blueprint('base', __name__)
THRESHOLD = 1.5


@base.route('/')
def index():
    return render_template('index.html')


@base.route('/predict', methods=['post'])
def predict():
    files = request.files
    img_left = Image.open(files.get('imgLeft')).convert('RGB')
    img_right = Image.open(files.get('imgRight')).convert('RGB')
    bbox_left, _ = detect_faces(img_left)
    bbox_right, _ = detect_faces(img_right)
    if bbox_left.shape[0] > 0:
        a, b, c, d, _ = bbox_left[0]
        img_left = img_left.crop((a, b, c, d))
    if bbox_right.shape[0] > 0:
        a, b, c, d, _ = bbox_right[0]
        img_right = img_right.crop((a, b, c, d))
    distance, similar = is_same(img_left, img_right, THRESHOLD)
    model_acc = ModelLoaded.acc
    return jsonify(same=('BERBEDA', 'SAMA')[similar.item()],
                   score=distance.item(),
                   model_acc=model_acc,
                   threshold=THRESHOLD)
