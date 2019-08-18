<?php
require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;

// Source http://docs.guzzlephp.org/en/stable/quickstart.html

$client = new Client([
    // Base URI is used with relative requests
    'base_uri' => 'http://httpbin.org',
    // You can set any number of default request options.
    'timeout'  => 2.0,
]);
$response = $client->request('GET', '/json');
$body = $response->getBody();
$stringBody = (string) $body;

die($stringBody);