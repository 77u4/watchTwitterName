# watchTwitterName
Watch your favourite unsued twitter usernames in order to grab them when they become available again

# About this program
This program makes it easy to watch your favorite twitter username using the [urlwatch](https://github.com/thp/urlwatch) program by [thp](https://github.com/thp). It's basically an easy way to install _urlwatch_, _python futures_ and configuring the watched URLs **plus** applying advanced filters for Twitter.com.

# Installation
execute ``` ./install.sh ```. You will need super user privileges.

After installing urlwatch you just need to execute ``` urlwatch ``` to see if anything has changed. If you want to watch your URLs more often, you can create a cronjob using 
```
*/5 * * * * urlwatch 
```
(this cronjob executes urlwatch every 5 minutes) 

You can also pipe the output into your mailing program to get notified if anything has changed.

```
*/5 * * * * urlwatch | mailx -E -s "Your fav twitter username is available again" your@email.tld
```