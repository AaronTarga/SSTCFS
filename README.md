# SSTCFS
This is a python script made to collect steam trading cards by clicking through list during steam sales.

For this script you need to install selenium on python. [Here are instructions to download selenium for python.](https://selenium-python.readthedocs.io/installation.html)
Download and use chrome driver or geckodriver as instructed in the documentation from selenium.

Then you need to change some things in the file:
Set the value of the cookies in the config.yml file by copying cookies while signed in, in the browser. You can do that with the firefox or chrome web developer tools. But it's more convenient if you use a plugin like [Cookie Editor](https://addons.mozilla.org/de/firefox/addon/cookie-editor/).
After that you can start your script by executing it like a normal python script `python steamv2.py`. (You can use multiple accounts as shown in the example).

Example config.yml:
```yaml
steam:
  - sessionId: first_sessionId
    steamLoginSecure: first_steamLoginSecure
  - sessionId: second_sessionId
    steamLoginSecure: second_steamLoginSecure

loops:
  first: 1
  second: 12
```


