<?php
$user = "id";		/* auth id */
$password = "pwd";	/* auth password */

$github_target = "target_id"; /* target id */
$github_repo = "target_repo"; 	/* target repository */

$idx = 1;
function set_default_opt(&$ch, $url)
{
	global $user;
	global $password;
	curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36");
	curl_setopt($ch, CURLOPT_TIMEOUT, 30);
	curl_setopt($ch, CURLOPT_USERPWD, "$user:$password");
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
}
function get_issue()
{
	global $idx;
	global $github_target;
	global $github_repo;
	$ch = curl_init();

	$url = "https://api.github.com/repos/$github_target/$github_repo/issues?state=all&page=${idx}&per_page=500";
	set_default_opt($ch, $url);

	$res = curl_exec ($ch);
	curl_close($ch);

	$obj = json_decode($res);
	$obj_cnt = count($obj);

	for ($i = 0; $i < $obj_cnt; $i++) {
		if ($obj[$i]->{'pull_request'} || !$obj[$i]->{'title'})
			continue;

		/* XXX. To add another object edit here. */
		printf("[%s]%s \n", $obj[$i]->{'number'}, $obj[$i]->{'title'});
	}

	$idx++;

	return 0;
}

function get_pageCount()
{
	global $github_target;
	global $github_repo;

	$ch = curl_init();
	$url = "https://api.github.com/repos/$github_target/$github_repo/issues?state=all";

	set_default_opt($ch, $url);
	curl_setopt($ch, CURLOPT_HEADER, 1);

	$res = curl_exec ($ch);

	$header_size = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
	$header = substr($res, 0, $header_size);

	$header = explode("\r\n", $header);

	for ($i = 0; $i < count($header); $i++) {
		list($key, $value) = explode(":", $header[$i], 2);

		if ($key != "Link") 
			continue;

		$arr = explode(" ", $value);
		sscanf($arr[3], "%[^&]&page=%[^>]>;", $tmp, $page);
		break;
	}

	curl_close($ch);
	return $page;
}

$maxpage = get_pageCount();

for ($i = 0; $i < $maxpage; $i++) {
	get_issue();
}
?>
