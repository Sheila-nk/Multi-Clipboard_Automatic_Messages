# MULTI-CLIPBOARD AUTOMATIC MESSAGES
## Description
This python program allows a user to copy multiple preset messages to the clipboard.
This is made possible by using the **pyperclip** module which can be installed using *pip*
``` pip install pyperclip ```
## Usage
To try out this program, clone the repository:
``` ```
You can use the already preset messages contained in the table below or update the dictionary with your own messages:
| **Phrase** | **Message** |
|-------------- | -------------- |
| response | I appreciate your swift response! I will work on the recommended changes. |
| unsure | I am unfamiliar with the intricacies of this situation. I will get back to you on it after some research. |
| feeback | I appreciate your feedback. I will implement the recommended changes. |
| resources | Thank you for the resources. I will be sure to check them out. |
| review | Please review my pull request. I have provided the link below. |
| merge | Thank you for reviewing and merging my pull request. |
| agree | Yes, I agree. That sounds fine to me. |
To run the script on your terminal:
```python clipboard.py <phrase> ```
This command copies the message to the clipboard which can then be pasted anywhere else.
**TO-DO**:  *The batch file does not work as expected to allow for output when run on Windows with the WIN-R Run window*