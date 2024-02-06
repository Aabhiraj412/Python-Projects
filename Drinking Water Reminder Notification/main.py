import time
from plyer import notification

if __name__  == "__main__":
 while True:   
  notification.notify(
        title = "Time To Drink Water",
        message  = "Sir, It Been a While, You Must Drink A Glass Of Water Now.",
        app_icon = "D:\Programs\Python Projects\Drinking Water Reminder Notification\icon.ico",
        timeout=20
    )
  time.sleep(60*5)

    
