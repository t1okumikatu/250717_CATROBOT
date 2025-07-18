from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

image_list = ['img1.png', 'img2.png', 'img3.png']
current_index = 0

@app.route('/')
def index():
    current_image = image_list[current_index]
    client_ip = request.remote_addr
    show_buttons = client_ip != '192.168.11.7'  # ← このIP以外はボタン表示
    #show_buttons = client_ip != '192.168.11.10'  # ← このIP以外はボタン表示
    return render_template('index.html', image_file=current_image, show_buttons=show_buttons)

@app.route('/next')
def next_image():
    global current_index
    current_index = (current_index + 1) % len(image_list)
    return redirect(url_for('index'))

@app.route('/prev')
def prev_image():
    global current_index
    current_index = (current_index - 1) % len(image_list)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
