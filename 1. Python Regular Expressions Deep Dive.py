import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Exclude emails from 'exclude.com' domain
exclude_domain = 'exclude.com'
pattern = rf'\b[A-Za-z0-9._%+-]+@(?!{re.escape(exclude_domain)})[A-Za-z0-9.-]+\.[A-Za-z]{{2,}}\b'

emails = re.findall(pattern, text)
print(emails)