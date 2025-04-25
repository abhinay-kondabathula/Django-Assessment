# TASK 1: DJANGO SIGNALS

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
import time
import threading

class SyncTest(models.Model):
    name = models.CharField(max_length=100)

# QUESTION 01 : Signal handler that simulates a slow task (for testing)

@receiver(post_save, sender=SyncTest)
def slow_signal_handler(sender, instance, **kwargs):
    print("[SYNC TEST] Signal triggered. Sleeping...")
    time.sleep(5)
    print("[SYNC TEST] Signal done sleeping.")
    
# QUESTION 02 : Signal handler to check which thread is running the signal

@receiver(post_save, sender=SyncTest)
def thread_check(sender, instance, **kwargs):
    #print("Signal thread:", threading.current_thread().name)
    #print("Created by thread:", threading.current_thread().name)
    print("[THREAD CHECK] Signal thread:", threading.current_thread().name)

# QUESTION 03 : Signal handler that checks if the signal runs inside a transaction

@receiver(post_save, sender=SyncTest)
def transactional_signal(sender, instance, **kwargs):
    if not transaction.get_connection().in_atomic_block:
        print("NOT in transaction")# Logs if not inside a transaction
    else:
        print("Inside a transaction")# Logs if inside a transaction

#................................................................................................................................................

# TESTING : 

# Open New Terminal and type: ( copy the content below )

# working on ------- test01 env

# ( go to the abhiporject folder ) 

"""
cd abhiproject

#{Only if needed.}

python manage.py runserver

#{Only if needed.}
"""

""" 
python manage.py makemigrations
python manage.py migrate 
python manage.py shell 
"""
# This sopen the shell, now type the testing code : copy it here :
"""
import threading
import time
from django.db import transaction
from myapp01.models import SyncTest  # Replace 'myapp' with your app name

print("[MAIN] Main thread:", threading.current_thread().name)

start = time.time()
with transaction.atomic():
    SyncTest.objects.create(name="FinalTest")
end = time.time()

print(f"[MAIN] Main execution time: {end - start:.2f} seconds")

"""
#please WAIT for the OUTPUT . THANKYOU .


# the Output looks  like:
"""
[MAIN] Main thread: MainThread
[SYNC TEST] Signal triggered. Sleeping...
[SYNC TEST] Signal done sleeping.
[THREAD CHECK] Signal thread: MainThread
Inside a transaction
[MAIN] Main execution time: 5.02 seconds

"""

