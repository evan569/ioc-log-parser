import re
log_pattern = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<time_stamp>[^\]]+)\] 'r'"(?P<method>\S+) (?P<path>\S+) \S+" ' r'(?P<status>\d+) (?P<size>\S+)' r' "(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"')
def parse(log_file):
    match = log_pattern.search(log_file)
    if not match:
        return None
    return match.groupdict()
with open('access.log') as f:
    for line as f:
        result = parse(line)
        print(result)
