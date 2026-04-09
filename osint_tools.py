# OSINT Tools

This module provides tools for Open Source Intelligence (OSINT) gathering.

## Features
- **Domain Lookup**: Provides information about a domain.
- **IP Geolocation**: Finds geographical information about an IP address.
- **Email Verification**: Verifies the validity of an email address.
- **Social Media Search**: Searches social media profiles based on usernames.

## Usage
```python
# Example usage of the OSINT Tools module

domain_info = domain_lookup('example.com')
print(domain_info)

ip_info = ip_geolocation('8.8.8.8')
print(ip_info)

email_valid = verify_email('user@example.com')
print(email_valid)

social_profiles = social_media_search('username')
print(social_profiles)
```
