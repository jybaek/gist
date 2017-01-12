## summary
It gets the number and titles of all issues. (open + closed)

## note
If you do not have a username and password query is limited to 50 circuits per hour.   
If you have a username and password, you can query up to 5,000 times per hour.  

document: https://developer.github.com/v3/#rate-limiting

## usage
Code modify `user`, `password`, `github_target`, `github_repo` in get_github_issue.php

    $ php get_github_issue.php
    # [number] title
	[17] test issue
	[16] hello world
	[15] fix error
	...
