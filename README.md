# PCmail

<p align="center">
  <img src="design/images/PCMAIL.png" alt="PC mail" style="border-radius:50%"/>
</p>

## Overview
PC controller app via gmail. This project consists of 2 applications:  
- Website (for remote controller)  
- PC app  (setup in local PC)  

Our system provides several control operations:
- Shutdown or restart.  
- List processes or kill a process.  
- Screenshot or webcam capture.  
- Copy files.  
- Update an entry in registry (only window).  
- Catch keyboards.  
## System diagram
![](design/illustration/system_diagram.png)

## Some captures of the website
### 1. Login screen
![](design/images/login_screen.png)

### 2. Main screen
![](design/images/main_screen.png)

### 3. Controller diaglog
![](design/images/control_dialog.png)

### 4. Help table
![](design/images/help_table.png)

## Technologies
#### 1. Website
**Frameworks**  
```
VueJs
Quasar
GmailAPI
GoogleAPI
```
**Languages**  
```
Javascript
Typescript
Vue
CSS
HTML
```
#### 2. PC application
**Packages**  
```
open-cv
PyQt
imaplib
pyautogui
email
winreg
```
**Languages**  
```
Python
```