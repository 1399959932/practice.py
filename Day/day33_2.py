Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from urllib import request
>>> req = request.Request('http://www.douban.com/')
>>> req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
>>> with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

    
Status: 200 OK
Date: Sat, 12 May 2018 12:23:24 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11690
Connection: close
Vary: Accept-Encoding
X-Xss-Protection: 1; mode=block
X-Douban-Mobileapp: 0
Expires: Sun, 1 Jan 2006 01:00:00 GMT
Pragma: no-cache
Cache-Control: must-revalidate, no-cache, private
Set-Cookie: talionnav_show_app="0"
Set-Cookie: bid=_t08rmclS7Y; Expires=Sun, 12-May-19 12:23:24 GMT; Domain=.douban.com; Path=/
X-DOUBAN-NEWBID: _t08rmclS7Y
X-DAE-Node: hador1
X-DAE-App: talion
Server: dae
Strict-Transport-Security: max-age=15552000;
X-Content-Type-Options: nosniff
Data: 


<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/WebPage">
    <head>
        <meta charset="UTF-8">
        <title>豆瓣(手机版)</title>
        <meta name="viewport" content="width=device-width, height=device-height, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
        <meta name="format-detection" content="telephone=no">
        <link rel="canonical" href="
http://m.douban.com/">
        <link href="https://img3.doubanio.com/f/talion/454d91e5b3534c7d91d7cb911cefe2b33042958f/css/card/base.css" rel="stylesheet">
        
    <meta name="description" content="读书、看电影、涨知识、学穿搭...，加入兴趣小组，获得达人们的高质量生活经验，找到有相同爱好的小伙伴。">
    <meta name="keywords" content="豆瓣,手机豆瓣,豆瓣手机版,豆瓣电影,豆瓣读书,豆瓣同城">
    
    

    <!-- Schema.org markup for Google+ -->
    <meta itemprop="name" content="豆瓣">
    <meta itemprop="description" content="读书、看电影、涨知识、学穿搭...，加入兴趣小组，获得达人们的高质量生活经验，找到有相同爱好的小伙伴。">
    <meta itemprop="image" content="https://img3.doubanio.com/f/talion/8e7b9cbd097c02972c4191aa03fdb084524505c4/pics/icon/m_logo_180.png">
    <!-- Twitter meta -->
    <meta name="twitter:card" content="summary" />
    <!-- Open Graph meta -->
    <meta property="og:title" content="豆瓣" />
    <meta property="og:description" content="读书、看电影、涨知识、学穿搭...，加入兴趣小组，获得达人们的高质量生活经验，找到有相同爱好的小伙伴。" />
    <meta property="og:site_name" content="豆瓣(手机版)" />
    <meta property="og:url" content="https://m.douban.com/" />
    <meta property="og:image" content="https://img3.doubanio.com/f/talion/8e7b9cbd097c02972c4191aa03fdb084524505c4/pics/icon/m_logo_180.png" />
    <meta property="og:image:type" content="image/png" />
    <meta property="og:image:width" content="300" />
    <meta property="og:image:height" content="300" />
    <meta property="og:type" content="article" />
    <!-- Wechat meta -->
    <meta property="weixin:timeline_title" content="豆瓣" />
    <meta property="weixin:chat_title" content="豆瓣" />
    <meta property="weixin:description" content="读书、看电影、涨知识、学穿搭...，加入兴趣小组，获得达人们的高质量生活经验，找到有相同爱好的小伙伴。" />
    <meta property="weixin:image" content="https://img3.doubanio.com/f/talion/8e7b9cbd097c02972c4191aa03fdb084524505c4/pics/icon/m_logo_180.png" />
    


        <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/468e9211d89502ad.css">
        <link rel="icon" type="image/png" sizes="16x16" href="https://img3.doubanio.com/f/talion/c970bb0d720963a7392f7dd6c77068bb9925caaf/pics/icon/dou16.png">
        <link rel="icon" type="image/png" sizes="32x32" href="https://img3.doubanio.com/f/talion/2f3c0bc0f35b031d4535fd993ae3936f4e40e6c8/pics/icon/dou32.png">
        <link rel="icon" type="image/png" sizes="48x48" href="https://img3.doubanio.com/f/talion/10a4a913a5715f628e4b598f7f9f2c18621bdcb3/pics/icon/dou48.png">
        <!-- iOS touch icon -->
        <link rel="apple-touch-icon-precomposed" href="https://img3.doubanio.com/f/talion/997f2018d82979da970030a5eb84c77f0123ae5f/pics/icon/m_logo_76.png">
        <link rel="apple-touch-icon-precomposed" sizes="76x76" href="https://img3.doubanio.com/f/talion/997f2018d82979da970030a5eb84c77f0123ae5f/pics/icon/m_logo_76.png">
        <link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://img3.doubanio.com/f/talion/18932a3e71a60ed7150ca2ca7ebf21ddadd7092e/pics/icon/m_logo_120.png">
        <link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://img3.doubanio.com/f/talion/b99497ff8538c54b9ba6f40867da932396ab2562/pics/icon/m_logo_152.png">
        <link rel="apple-touch-icon-precomposed" sizes="167x167" href="https://img3.doubanio.com/f/talion/0c233ada957a95e632f81607e30230d16e8293e8/pics/icon/m_logo_167.png">
        <link rel="apple-touch-icon-precomposed" sizes="180x180" href="https://img3.doubanio.com/f/talion/8e7b9cbd097c02972c4191aa03fdb084524505c4/pics/icon/m_logo_180.png">
        <link rel="apple-touch-icon-precomposed" sizes="200x200" href="https://img3.doubanio.com/f/talion/7c6364aadf368dc0210173c940cfd0f64ceddc66/pics/icon/m_logo_200.png">
        <!-- For Android -->
        <link rel="icon" sizes="128x128" href="https://img3.doubanio.com/f/talion/b99497ff8538c54b9ba6f40867da932396ab2562/pics/icon/m_logo_152.png">
        <link rel="icon" sizes="192x192" href="https://img3.doubanio.com/f/talion/7c6364aadf368dc0210173c940cfd0f64ceddc66/pics/icon/m_logo_200.png">
        <!-- For Web App Manifest -->
        
  
  
  <link rel="manifest" href="/pwa/manifest?path=/&short_name=%E8%B1%86%E7%93%A3%28%E6%89%8B%E6%9C%BA%E7%89%88%29&name=%E8%B1%86%E7%93%A3%28%E6%89%8B%E6%9C%BA%E7%89%88%29">
  <meta name="theme-color" content="#42bd56">


        <link type="application/opensearchdescription+xml" rel="search" href="/opensearch"/>
            <!-- hm baidu -->
            <script type="text/javascript">
            var _hmt = _hmt || [];
            (function() {
              var hm = document.createElement("script");
              hm.src = "https://hm.baidu.com/hm.js?6d4a8cfea88fa457c3127e14fb5fabc2";
              var s = document.getElementsByTagName("script")[0];
              s.parentNode.insertBefore(hm, s);
            })();
            </script>
    </head>
    <body ontouchstart="">
        
        

        
    
    
        <div id="TalionNav"><header class="TalionNav"><div class="TalionNav-primary"><a href="/"><h1>豆瓣</h1></a><nav><ul><li><a href="/movie" style="color: #2384E8;">电影</a></li><li><a href="/book" style="color: #9F7860;">图书</a></li><li><a href="/status" style="color: #E4A813;">广播</a></li><li><a href="/group" style="color: #2AB8CC;">小组</a></li></ul><span class=""></span></nav></div><div class="TalionNav-secondary"><a class="close-nav" href="javascript:;">关闭</a><form action="/search" method="GET"><div><input name="query" type="search"></div></form><ul><li><div><a href="/movie" target="_blank"><strong style="color: #2384E8;">电影</strong><span>影院热映</span></a><a href="https://douban.com/location" target=""><strong style="color: #E6467E;">同城</strong><span>周末活动</span></a><a href="https://read.douban.com" target=""><strong style="color: #9F7860;">阅读</strong><span>电子书</span></a><a href="/status" target="_blank"><strong style="color: #E1644D;">广播</strong><span>友邻动态</span></a></div></li><li><div><a href="/tv" target="_blank"><strong style="color: #7A6ADB;">电视</strong><span>正在热播</span></a><a href="/group" target="_blank"><strong style="color: #2AB8CC;">小组</strong><span>志趣相投</span></a><a href="/game" target="_blank"><strong style="color: #5774C5;">游戏</strong><span>虚拟世界</span></a><a href="https://douban.fm" target=""><strong style="color: #40CFA9;">FM</strong><span>红心歌单</span></a></div></li><li><div><a href="/book" target="_blank"><strong style="color: #9F7860;">图书</strong><span>畅销排行</span></a><a href="/music" target="_blank"><strong style="color: #F48F2E;">音乐</strong><span>新碟榜</span></a><a href="/mobileapp" target="_blank"><strong style="color: #596CDD;">应用</strong><span>玩手机</span></a><a href="https://market.douban.com/?utm_campaign=mobile_web_douban_nav&amp;utm_source=douban&amp;utm_medium=mobile_web" target=""><strong style="color: #42BD56;">市集</strong><span>购买原创</span></a></div></li></ul><div class="navBottom"><div class="nav-item"><a class="toUser" href="/mine/">我的豆瓣</a><a class="toExit" href="https://accounts.douban.com/logout?ck=undefined">退出豆瓣</a></div><div class="nav-item"><a class="toPC" href="/to_pc/?url=about%3Ablank">使用桌面版</a><a class="toApp">使用豆瓣App</a></div></div></div></header></div>


        <div class="page">
            
    <div class="card">
        <ul class="quick-nav">
            <li>
                <a href="/movie/nowintheater?loc_id=108288">影院热映</a>
            </li>
              <li>
                  <a href="/group/explore/rent/">租房找室友</a>
              </li>
            <li>
                <a id="hot-topics" href="https://m.douban.com/time/?dt_time_source=douban-msite_shortcut">豆瓣时间</a>
            </li>
            <li>
                <a href="https://www.douban.com/doubanapp/app?channel=card_home&direct_dl=1">使用豆瓣App</a>
            </li>
        </ul>
        <section id="recommend-feed"></section>
    </div>

        </div>

        <script src="https://img3.doubanio.com/f/talion/ee8e0c54293aefb5709ececbdf082f8091ad5e49/js/card/zepto.min.js"></script>
        <script src="https://img3.doubanio.com/f/talion/5c296dff1a57cf667bef8fb0f45ef96d68955a24/js/card/main.js"></script>
        <script src="https://img3.doubanio.com/f/talion/f53cc45d4a16969b8592d776f476d9784a283e4a/js/lib/douban-ad-helper.js"></script>



        
    
  


        
  

  
        <script src="https://img3.doubanio.com/f/talion/88fc2b21c8dda5c93aa4c011eb15b74f8850978f/js/lib/react/15.3.0/react-all.min.js"></script>


  <script type="text/javascript">
    var userCfg = {}
  </script>

  

  
  



        <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/9294d648aac763c.js"></script>
        


<script type="text/javascript" data-mobile="true">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = '_t08rmclS7Y',
            criteria = '3:/',
            preview = '',
            debug = false;

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/cdc904d1376a43e44bbf399a0aff51973016cd77/ad.release.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>


        
  


        <script type='text/javascript'>
            
            ;(function(global) {
                if (window.DoubanAdRequest) {
                    window.DoubanAdRequest.filter = []
                }
                global.DoubanAdSlots = global.DoubanAdSlots || []
            })(window);
        </script>
            <!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-NZHN7H" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-NZHN7H');</script>
<!-- End Google Tag Manager -->
<!-- Google Analytics -->
<script>
window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
ga('create', 'UA-53594431-3', {'sampleRate': 4});
ga('send', 'pageview');
</script>
<script async src='//www.google-analytics.com/analytics.js'></script>
<!-- End Google Analytics -->

        






    </body>
</html>















>>> from urllib import request, parse
>>> print('Login to weibo.cn...')
Login to weibo.cn...
>>> email = imput('Email:')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    email = imput('Email:')
NameError: name 'imput' is not defined
>>> email = input('Email:')
Email:
>>> passwd = input('Password')
Password
>>> login_data = parse.ur;encode([
	('username', email),
	('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
	])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    login_data = parse.ur;encode([
AttributeError: module 'urllib.parse' has no attribute 'ur'
>>> login_data = parse.ur;encode([
	('username', email),
	('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    login_data = parse.ur;encode([
AttributeError: module 'urllib.parse' has no attribute 'ur'
>>> login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
>>> req = request.Request('https://passport.weibo.cn/sso/login')
>>> req.add_header('Origin', 'https://passport.weibo.cn')
>>> req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
>>> req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
>>> with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

    
Status: 200 OK
Server: nginx/1.6.1
Date: Sat, 12 May 2018 13:00:23 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: close
Vary: Accept-Encoding
Cache-Control: no-cache, must-revalidate
Expires: Sat, 26 Jul 1997 05:00:00 GMT
Pragma: no-cache
Access-Control-Allow-Origin: https://passport.weibo.cn
Access-Control-Allow-Credentials: true
DPOOL_HEADER: lich78
Set-Cookie: login=81272d1749a34b78139b2ac96fdac143; Path=/
Data: {"retcode":50011007,"msg":"\u8bf7\u8f93\u5165\u7528\u6237\u540d","data":{"errline":318}}
>>> proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
SyntaxError: multiple statements found while compiling a single statement
>>> proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
NameError: name 'urllib' is not defined
>>> proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
NameError: name 'urllib' is not defined
>>> from urllib import request
>>> proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
NameError: name 'urllib' is not defined
>>> 
