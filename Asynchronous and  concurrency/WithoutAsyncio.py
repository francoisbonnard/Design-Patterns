import time

def handle_event(event):
    print(f"Événement reçu : {event}")

def generate_events():
    for i in range(1, 6):
        time.sleep(1)  
        event = f"Événement {i}"
        handle_event(event)

def main():
    generate_events()

main()
