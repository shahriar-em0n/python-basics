log_message = "User logged in at 25 minute"
with open("016_file/server_log.txt", "w") as file:  # windows issue /
    file.write(log_message) 