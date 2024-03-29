# Password Manager (PassMan)

<img src='./screenshots/Password_Manager_screenshot1.png' width='700'>

> [!NOTE]
> This is how program looks. "Generate" button will generate a random strong password.
> In website entry user can type the name of the website or paste website's login page link.
> E-mail has a default value of "abcdef@gmail.com", this can be change in my code marked with 🔴 EMAIL in the screenshot below.
> The value of EMAIL will be a defult value for "Email/Username" entry, even after restarting my program.

<img src='./screenshots/Password_Manager_screenshot2.png' width='700'>

<img src='./screenshots/Password_Manager_screenshot3.png' width='700'>

> [!CAUTION]
> If user left entries empty before hitting "Add" button, this message is going to pop-out, asking a user to not leave any empty fields.
> To leave the pop-out window just click "Ok" at the bottom right corner.

<img src='./screenshots/Password_Manager_screenshot4.png' width='700'>

> [!NOTE]
> When user succesfully fill all of the empty entries and hit "Add" Button, the window will pop-out with the title of the website name / link.
> Showing user's entries and asking if it is ok to save them.
> Generated password will be copied to the clipboard, user can paste it by hitting "CTRL+V" (paste shortcut).
> I used [pyperclip](https://pypi.org/project/pyperclip/) for that.

<img src='./screenshots/Password_Manager_screenshot5.png' width='700'>

> [!IMPORTANT]
> User's entries will be saved in a data.json file, using always the same format as in the screenshot above.

<img src='./screenshots/Password_Manager_screenshot6.png' width='700'>

> [!NOTE]
> When user has typed existing data in website entry and has pressed search button the window will pop-out with the title of the website containing details of login (email and password)

<img src='./screenshots/Password_Manager_screenshot7.png' width='700'>

> [!CAUTION]
> If user tries to search for details of not existing data, window that is in the screenshot above will pop-out.

> [!WARNING]
> What you need to download:
>- main.py (Only file that needs to be open, in order to start my program)
>- logo.png (Just a logo with a catching name for my program)
