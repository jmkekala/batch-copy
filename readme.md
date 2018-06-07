# Batch Copy
Recently I had a problem with the Microsoft [OneDrive for Business](https://onedrive.live.com/about/fi-FI/business/). I attempted to push 100k files to the system thru filesync but alas, it got stuck on "Processing Changes" for days.

This little script attempts to solve the issue by copying files slowly. By default the script delays every file copy by 0.5 s and after 100 copied files there is a 1 minute waiting period. With this method I was able to push these files to the cloud.

Licence:
MIT
