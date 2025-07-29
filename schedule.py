# schedule.py
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from agent import parse_grocery_note
from blinkit_bot import search_blinkit

UPLOAD_FOLDER = "uploads"

def process_grocery_file():
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.endswith(".txt"):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            with open(filepath, "r") as f:
                note = f.read()
                print(f"\n📄 Processing file: {filename}")

                ai_output = parse_grocery_note(note)

                try:
                    grocery_list = eval(ai_output)
                except:
                    grocery_list = []

                for item in grocery_list:
                    result = search_blinkit(item["item"])
                    print(f"✅ {result['item']} → {result['product_name']} at {result['price']}")
            print("🛒 Done for:", filename)

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Weekly at Monday 10:00 AM
    scheduler.add_job(process_grocery_file, 'cron', day_of_week='mon', hour=10, minute=0)
    scheduler.start()
    print("⏰ Scheduler started...")

    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("❌ Scheduler stopped.")


if __name__ == "__main__":
    start_scheduler()

scheduler.add_job(process_grocery_file, 'interval', seconds=30)


scheduler.add_job(process_grocery_file, 'cron', day_of_week='mon', hour=10, minute=0)
