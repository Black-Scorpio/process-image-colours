from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from PIL import Image
import webcolors
from collections import Counter
from sklearn.cluster import KMeans
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def resize_image(image, max_width, max_height):
    # Calculate the appropriate resize dimensions maintaining the aspect ratio
    aspect_ratio = min(max_width / image.width, max_height / image.height)
    new_size = (int(image.width * aspect_ratio), int(image.height * aspect_ratio))
    return image.resize(new_size, Image.LANCZOS)


def extract_common_colors(image_path, num_colors=10):
    image = Image.open(image_path)
    image = resize_image(image, 800, 600)  # Resize image to max 800x600
    image = image.convert("RGB")  # Ensure image is in RGB mode

    # Convert image data to numpy array for clustering
    image_data = np.array(image)
    image_data = image_data.reshape((-1, 3))

    # Use KMeans to cluster colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(image_data)
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Count frequency of each cluster
    label_counts = Counter(labels)

    # Get colors in hex format
    hex_colors = []
    for cluster_center, count in zip(cluster_centers, label_counts.values()):
        hex_color = webcolors.rgb_to_hex(tuple(map(int, cluster_center)))
        hex_colors.append((hex_color, count))

    return hex_colors


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        common_colors = extract_common_colors(filepath)
        image_url = f'/uploads/{filename}'
        return jsonify({'success': True, 'filename': filename, 'image_url': image_url, 'colors': common_colors})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
