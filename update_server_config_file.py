def update_server_config(file_path,key,value):
  with open(file_path,"r") as file:
    read_lines=file.readlines()

  with open(file_path,"w") as file:
    for scan_value in read_lines:
      if key in scan_value:
        file.write(key + "=" + value + "\n")
      else:
        file.write(scan_value)

update_server_config("server.config","password","abcdedf123")
