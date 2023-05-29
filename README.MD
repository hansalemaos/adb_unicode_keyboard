### Send any Unicode character to your Android device

```python
pip install adb-unicode-keyboard

from adb_unicode_keyboard import  AdbUnicodeKeyboard
from time import sleep
adbkeyboard = AdbUnicodeKeyboard(adb_path = "C:\\Users\\Gamer\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe",
deviceserial = "localhost:5735", exit_keys="ctrl+x")
adbkeyboard.connect_to_adb()
oldkeyboard = adbkeyboard.get_all_installed_keyboards()[0]
adbkeyboard.install_adb_keyboard() # installs "https://github.com/senzhk/ADBKeyBoard/raw/master/ADBKeyboard.apk"
adbkeyboard.activate_adb_keyboard()
if adbkeyboard.is_keyboard_shown():

    adbkeyboard.send_unicode_text('öü')
    adbkeyboard.send_unicode_text_with_delay('öü', delay_range=(0.05, 0.3))
    sleep(1)
    adbkeyboard.longpress_66_keycode_enter() # not executed with ADBKeyBoard / all keycodes are available as methods
    sleep(1)
    adbkeyboard.press_66_keycode_enter() # not executed with ADBKeyBoard  / all keycodes are available as methods

adbkeyboard.disable_adb_keyboard(new_keyboard_name=None) # If no keyboard name is passed, will be reset to default
adbkeyboard.disable_adb_keyboard(new_keyboard_name=oldkeyboard)

#adbkeyboard.uninstall_adb_keyboard()

# Chaining is possible
adbkeyboard.connect_to_adb().activate_adb_keyboard().send_unicode_text('böb&oö').disable_adb_keyboard()

```

