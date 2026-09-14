# ioc-log-parser

A small Python tool that uses regular expressions to parse Apache/Nginx-style
access logs (`access.log`) into structured fields: client IP, timestamp,
HTTP method, requested path, status code, response size, referer, and user
agent.

## Status

Work in progress. The regex successfully matches and extracts fields from a
combined log format line. Does not as of yet sort or flag logs per results of extraction.

## Usage

```bash
python log_parser.py
```

Reads `access.log` in the current directory line by line, extracts fields
with the regex pattern, and prints the parsed result for each line.

## Sample data

`access.log` contains synthetic log lines using IP ranges reserved for
documentation/testing (RFC 5737: 203.0.113.0/24, 198.51.100.0/24) — no real
traffic data.
