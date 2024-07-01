'''

:: NOTES

1. TQDM Progress Bar is easy to implement but basic.
2. Colorama Progress Bar is comparatively harder to implement but looks better.

'''



import time
from tqdm import tqdm
from colorama import Fore, Style


choice = int(input("::: PROGRESS BARS :::\n\nChoose your style:\n1. TQDM\n2. COLORAMA\n3. Exit\n\n"))
# switch(choice):               PYTHON DOESNT HAVE SWITCH CASE STATEMENT
while(choice):
    if choice == 1:
        # Iterate over a range of 100 with a progress bar
        for i in tqdm(range(100)):
        # Simulate some processing (can be replaced with your actual code)
            time.sleep(0.01)  # Sleep for 0.01 seconds (adjust as needed)
        print("Done!")
        break
    elif choice == 2:
        bar_length = 50  # Adjust the length of the progress bar
        progress_char = Fore.YELLOW + '█' + Style.RESET_ALL  # Colored progress character
        remaining_char = ' '

        def print_progress_bar(progress, total):
            # Calculate completion percentage
            percent = int((progress / total) * 100)

            # Fill progress bar with colored characters
            filled_length = int(percent / 100 * bar_length)
            progress_bar = progress_char * filled_length

            # Fill remaining space with empty characters
            remaining_bar = remaining_char * (bar_length - filled_length)

            # Print the progress bar and percentage
            print(f"{progress_bar}{remaining_bar} {percent}%", end='\r')

        # Example usage
        total = 100
        for i in range(total):
            # Simulate some processing (can be replaced with your actual code)
            time.sleep(0.01)  # Sleep for 0.01 seconds (adjust as needed)

            # Update progress bar
            print_progress_bar(i + 1, total)

        # Print completion message after the loop
        print(Fore.GREEN + "Done!" + Style.RESET_ALL)
        break
    else:
        print("Exiting...")
        time.sleep(1)
        exit(0)


# END OF CODE