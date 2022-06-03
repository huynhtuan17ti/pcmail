import poweroff from 'src/assets/power-off.png';
import process from 'src/assets/process.png';
import screenshot from 'src/assets/screenshot.png';
import video from 'src/assets/video.png';
import test from 'assets/test.png';
import restart from 'assets/restart.jpg';

export const extensions = [
  'basic',
  'shutdown',
  'list_process',
  'screenshot',
  'webcam',
  'restart',
];

export const extensionImages = {
  basic: test,
  shutdown: poweroff,
  list_process: process,
  screenshot: screenshot,
  webcam: video,
  restart: restart,
};
