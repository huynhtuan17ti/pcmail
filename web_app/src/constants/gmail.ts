export const end_email = 'networkingass20120015@gmail.com';
export const subject = '[PCMAIL] Request';
export const message = {
  basic: 'This is a testing message. No valuable!',
  shutdown: 'SHUTDOWN',
  restart: 'RESTART',
  list_process: 'LIST PROCESSES',
  kill_process: 'KILL ',
  webcam: 'VIDEO',
  screenshot: 'SCREENSHOT',
  copy: 'COPY ',
  // TODO: add more, based on pc_app
};

export const message_title = {
  basic: 'Send test mail',
  shutdown: 'Shutdown computer',
  restart: 'Restart computer',
  list_process: 'List processes',
  kill_process: 'Kill process',
  webcam: 'Capture webcam',
  screenshot: 'Screenshot',
  copy: 'Copy file',
};

export const sending_format = {
  basic: null,
  shutdown: null,
  restart: null,
  list_process: null,
  kill_process: 'process_id',
  webcam: null,
  screenshot: null,
  copy: 'path_to_A path_to_B',
};
