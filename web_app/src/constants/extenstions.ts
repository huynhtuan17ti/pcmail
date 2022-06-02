import poweroff from 'src/assets/power-off.png';
import process from 'src/assets/process.png';
import screenshot from 'src/assets/screenshot.png';
import video from 'src/assets/video.png';
import basic from 'assets/basic.jpg';

export const extensions = [
  'basic',
  'shutdown',
  'list_process',
  'screenshot',
  'webcam',
];

export const extensionImages = {
  basic: basic,
  shutdown: poweroff,
  list_process: process,
  screenshot: screenshot,
  webcam: video,
};
