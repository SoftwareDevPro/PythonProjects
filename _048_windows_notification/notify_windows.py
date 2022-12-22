
import win10toast
import argparse

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t','--title',help='the title for the notification')
parser.add_argument('-m','--message',help='the notification message')
args = parser.parse_args()

notifier = win10toast.ToastNotifier()

# title message, time
notifier.show_toast(args.title, args.message, duration=5)
