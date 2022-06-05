import poweroff from 'src/assets/power-off.png';
import process from 'src/assets/process.png';
import screenshot from 'src/assets/screenshot.png';
import video from 'src/assets/video.png';
import test from 'assets/test.png';
import restart from 'assets/restart.png';
import kill_process from 'assets/kill_process.png';
import folder from 'assets/folder.jpg';

export const extensions = [
  'basic',
  'shutdown',
  'list_process',
  'screenshot',
  'webcam',
  'restart',
  'kill_process',
  'copy',
];

export const extensionImages = {
  basic: test,
  shutdown: poweroff,
  list_process: process,
  kill_process: kill_process,
  screenshot: screenshot,
  webcam: video,
  restart: restart,
  copy: folder,
};
