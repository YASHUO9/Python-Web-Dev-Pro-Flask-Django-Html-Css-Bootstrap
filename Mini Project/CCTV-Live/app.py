from flask import Flask, render_template, Response
import cv2



app = Flask(__name__)
camera = cv2.VideoCapture(0) # use 0 for web camera


def cctv_live():
    while True:
        success, frame = camera.read() # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame) # encode the frame in JPEG format
            frame = buffer.tobytes() # convert the frame into bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')   # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(cctv_live(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)


