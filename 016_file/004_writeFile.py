log_message = "User logged in at 21:55\n"
with open("server_log.txt", "w") as file:
    file.write(log_message)

# with open("server_log.txt", "a") as file:
#     file.write(log_message)

# with open("server_log.txt", "x") as file:
#     file.write(log_message)