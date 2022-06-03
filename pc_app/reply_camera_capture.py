import cv2
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from my_utils import finish_and_send

def reply_camera_capture(original_email, USERNAME, PASSWORD):
    cap = cv2.VideoCapture(0) 

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    output = cv2.VideoWriter('reply_video.mp4', fourcc, 20, (width, height))

    while(cap.isOpened()):
        try:
            ret, frame = cap.read()
            if ret == True:
                output.write(frame)
                cv2.waitKey(1)
        except:
            break

    output.release()
    cap.release()
    cv2.destroyAllWindows()

    rep = MIMEMultipart('mixed')
    with open('reply_video.mp4', 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        
    encoders.encode_base64(part)
    
    part.add_header(
        'Content-Disposition',
        f'attachment; filename= reply_video.mp4',
    )
    
    rep.attach(part)
    finish_and_send(rep, original_email, USERNAME, PASSWORD)
