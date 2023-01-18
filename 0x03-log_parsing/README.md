# 0x03-log_parsing

Write a script that reads stdin line by line and computes metrics:

+ Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
+ After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:

  + Total file size: File size: <total size>
  + where <total size> is the sum of all previous <file size> (see input format above)
