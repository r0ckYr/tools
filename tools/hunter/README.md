# hunter
hunter.py can be used to check for working http and https servers and fetching urls. It saves the output in a directory called **./out** all the text in a directory named **text** and headers in **headers** inside **out**. It also extract all the javascript file names/links from the page and saves the urls which gives an error in a file **errors**

**Example:**

![hunter-data](https://user-images.githubusercontent.com/73944333/125824700-ed315199-11ed-40aa-be1f-698e5791eb51.png)


# Install
```
git clone https://github.com/r0ckYr/hunter
cd hunter
pip3 install -r requirements.txt
python3 hunter.py urls.txt
```

# Usage:

**urls.txt**
```
https://www.example.com
https://www.example.com/robot.txt
https://www.example.com/all.js
http://example.com
https://example.com
http://example.net
api.example.com
aa.wiki.com
www.google.com/all.js
```

```
python3 hunter.py -t 20 -timeout 10 urls.txt
```

```
arguments:
    -h             Prints help information
    -t             Number of threads (default 20)
    -p             ports to scan (eg., 80,8443,443,8080)
    -timeout       Timeout in seconds (default 10)
    --no-redirect  Don't allow redirects (default true)
    --no-save      Don't save response (defatult true)
```

# Output
**1. Inside the ```out``` directory**

![hunter-data](https://user-images.githubusercontent.com/73944333/125824700-ed315199-11ed-40aa-be1f-698e5791eb51.png)

**2. index file**
```
   1 http://coinbasecustody.com Registered & Protected by MarkMonitor (200) [1612]
   2 https://api.coinbase-test.com (403) [35]
   3 https://api.commerce.coinbase.com (404) [52]
   4 https://api.custody.coinbase.com (404) [135]
   5 https://api.coinbase.com Coinbase Digital Currency API (200) [588852]
   6 http://coingbase.com Registered & Protected by MarkMonitor (200) [1612]
   7 https://api.exchange.coinbase.com (404) [69]
   8 https://api.gdax.com api.gdax.com | 526: Invalid SSL certificate (526) [6198]
   9 http://coinibase.com Registered & Protected by MarkMonitor (200) [1612]
  10 https://api.pro.coinbase.com (404) [69]
  11 https://api.wallet.coinbase.com (200) [15]
  12 https://api3.coinbase-test.com Error 404 (Not Found)!!1 (404) [1557]
  13 https://api.paradex.io Coinbase – Buy & Sell Bitcoin, Ethereum, and more with trust (200) [1012697]
  14 https://20.tagomi.com 403 Forbidden (403) [146]
```

**3. headers**
```
Date: Thu, 15 Jul 2021 16:08:23 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Cache-Control: no-store
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-eval' https://maps.googleapis.com; style-src 'self' 'unsafe-inline'; object-src 'none'; base-uri 'self'; connect-src 'self' https://*.coinbase.com; font-src 'self' https://fonts.gstatic.com/s/googlesans; frame-src 'self'; img-src 'self'; manifest-src 'self'; media-src 'self'; report-uri https://www.coinbase.com/csp-logging; worker-src 'none'
Last-Modified: Wed, 30 Jun 2021 20:08:59 GMT
Strict-Transport-Security: max-age=15552000; includeSubDomains
Via: 1.1 15d56bef7b8d30c7328ed4685742279e.cloudfront.net (CloudFront)
X-Amz-Cf-Id: iNIymIY1mABLL97LlSXal5me-ySBHDzrIAJ_PP4Oc3yo_4Z6c2A0aw==
X-Amz-Cf-Pop: IAD79-C3
X-Cache: Miss from cloudfront
X-Content-Type-Options: nosniff
X-Dns-Prefetch-Control: off
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Xss-Protection: 1; mode=block
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 66f43fc26d8a69a1-BOM
Content-Encoding: gzip
```

**4. jsfiles**
```
https://api.coinbase.com/../../javascripts/all.js
https://assets.coinbase.com/assets/webpack-runtime-eb7a2cff0e1cbbba497d.js
https://assets.coinbase.com/assets/polyfill-7d3a99bfa2060ae638a1.chunk.js
https://assets.coinbase.com/assets/vendorsapi-a5343f042e89f49b37e6.chunk.js
https://assets.coinbase.com/assets/react-4e18781c5ceb51381280.chunk.js
https://assets.coinbase.com/assets/vendors~main-c2c58b8c5929ec1bd916.chunk.js
https://assets.coinbase.com/assets/main-7f700925f89fdb501e4b.chunk.js
```

# TODO
1.Add colors (might be!)

2.Performance?

3.add -paths option

