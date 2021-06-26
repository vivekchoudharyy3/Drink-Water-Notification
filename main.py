import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drinking Water Reminder",
            message = "This is a reminder to drink water and stay hydrated",
            app_icon = 'icon.ico',
            timeout = 5
        )
        time.sleep(60*60)