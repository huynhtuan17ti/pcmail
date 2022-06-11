export const end_email = 'networkingass20120015@gmail.com';
export const subject = '[PCMAIL] Request';
export const message = {
  basic: 'TEST MESSAGE',
  shutdown: 'SHUTDOWN',
  restart: 'RESTART',
  list_process: 'LIST PROCESSES',
  kill_process: 'KILL ',
  webcam: 'VIDEO',
  screenshot: 'SCREENSHOT',
  copy: 'COPY ',
  keyboard: 'CATCH KEYBOARD',
  registry: 'REG ',
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
  keyboard: 'Catch keyboard',
  registry: 'Update entry in registry',
};

export const sending_format = {
  basic: null,
  shutdown: null,
  restart: null,
  list_process: null,
  kill_process: '[process_id]',
  webcam: null,
  screenshot: null,
  copy: '[source] [dest]',
  keyboard: null,
  registry: '[path] [entry_name] [entry_value]',
};

export const detail = {
  basic: 'Sending a testing message.',
  shutdown: 'Shutdown your computer.',
  restart: 'Restart your computer.',
  list_process:
    'List all apps and processes that are running on your computer.',
  kill_process: 'Kill a process or an app via a process id',
  webcam: 'Video capture by webcam of your computer',
  screenshot: 'Capture desktop screen of your computer',
  copy: 'Copy a file to other directory',
  keyboard: 'Catch your keyboard',
  registry: 'Update one entry in your PC registry',
};

export const response = {
  basic: null,
  shutdown: 'Success or Fail',
  restart: 'Success or Fail',
  list_process: 'A list with process id',
  kill_process: 'Success or Fail',
  webcam: 'A capture video',
  screenshot: 'Screenshot image',
  copy: 'Success or Fail',
  keyboard: 'A list of catched key',
  registry: 'Success or Fail',
};
