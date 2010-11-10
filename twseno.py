#!/usr/bin/env python
# -*- coding: utf-8 -*-

class twseno(object):
  def __init__(self):
    self.allstockno = STOCKNO

  @property
  def allstock(self):
    """ Return all stock no and name by dict. """
    return self.allstockno

  def search(self,q):
    """ Search. """
    import re
    pattern = re.compile("%s" % q)
    result = {}
    for i in self.allstockno:
      b = re.search(pattern, self.allstockno[i])
      try:
        b.group()
        result[i] = self.allstockno[i]
      except:
        pass

    return result

  def searchbyno(self,q):
    """ Search by no. """
    import re
    pattern = re.compile("%s" % q[0:2])
    result = {}
    for i in self.allstockno:
      b = re.search(pattern, i)
      try:
        b.group()
        result[i] = self.allstockno[i]
      except:
        pass

    return result

##### stock no list #####
STOCKNO = {'1101':'台泥',
'1102':'亞泥',
'1103':'嘉泥',
'1104':'環泥',
'1108':'幸福',
'1109':'信大',
'1110':'東泥',
'1201':'味全',
'1203':'味王',
'1210':'大成',
'1213':'大飲',
'1215':'卜蜂',
'1216':'統一',
'1217':'愛之味',
'1218':'泰山',
'1219':'福壽',
'1220':'台榮',
'1225':'福懋油',
'1227':'佳格',
'1229':'聯華',
'1231':'聯華食',
'1232':'大統益',
'1233':'天仁',
'1234':'黑松',
'1235':'興泰',
'1236':'宏亞',
'1301':'台塑',
'1303':'南亞',
'1304':'台聚',
'1305':'華夏',
'1307':'三芳',
'1308':'亞聚',
'1309':'台達化',
'1310':'台苯',
'1312':'國喬',
'1313':'聯成',
'1314':'中石化',
'1315':'達新',
'1316':'上曜',
'1319':'東陽',
'1321':'大洋',
'1323':'永裕',
'1324':'地球',
'1325':'恆大',
'1326':'台化',
'1402':'遠東新',
'1409':'新纖',
'1410':'南染',
'1413':'宏洲',
'1414':'東和',
'1416':'廣豐',
'1417':'嘉裕',
'1418':'東華',
'1419':'新紡',
'1423':'利華',
'1432':'大魯閣',
'1434':'福懋',
'1435':'中福',
'1436':'福益',
'1437':'勤益',
'1438':'裕豐',
'1439':'中和',
'1440':'南紡',
'1441':'大東',
'1442':'名軒',
'1443':'立益',
'1444':'力麗',
'1445':'大宇',
'1446':'宏和',
'1447':'力鵬',
'1449':'佳和',
'1451':'年興',
'1452':'宏益',
'1453':'大將',
'1454':'台富',
'1455':'集盛',
'1456':'怡華',
'1457':'宜進',
'1459':'聯發',
'1460':'宏遠',
'1463':'強盛',
'1464':'得力',
'1465':'偉全',
'1466':'聚隆',
'1467':'南緯',
'1468':'昶和',
'1469':'理隆',
'1470':'大統染',
'1471':'首利',
'1472':'三洋纖',
'1473':'台南',
'1474':'弘裕',
'1475':'本盟',
'1476':'儒鴻',
'1477':'聚陽',
'1503':'士電',
'1504':'東元',
'1506':'正道',
'1507':'永大',
'1512':'瑞利',
'1513':'中興電',
'1514':'亞力',
'1515':'力山',
'1516':'川飛',
'1517':'利奇',
'1519':'華城',
'1521':'大億',
'1522':'堤維西',
'1524':'耿鼎',
'1525':'江申',
'1526':'日馳',
'1527':'鑽全',
'1528':'恩德',
'1529':'樂士',
'1530':'亞崴',
'1531':'高林股',
'1532':'勤美',
'1533':'車王電',
'1535':'中宇',
'1536':'和大',
'1537':'廣隆',
'1538':'正峰新',
'1539':'巨庭',
'1540':'喬福',
'1541':'錩泰',
'1560':'中砂',
'1582':'信錦',
'1583':'程泰',
'1603':'華電',
'1604':'聲寶',
'1605':'華新',
'1608':'華榮',
'1609':'大亞',
'1611':'中電',
'1612':'宏泰',
'1613':'台一',
'1614':'三洋電',
'1615':'大山',
'1616':'億泰',
'1617':'榮星',
'1618':'合機',
'1701':'中化',
'1702':'南僑',
'1704':'榮化',
'1707':'葡萄王',
'1708':'東鹼',
'1709':'和益',
'1710':'東聯',
'1711':'永光',
'1712':'興農',
'1713':'國化',
'1714':'和桐',
'1715':'亞化',
'1716':'永信',
'1717':'長興',
'1718':'中纖',
'1720':'生達',
'1721':'三晃',
'1722':'台肥',
'1723':'中碳',
'1724':'台硝',
'1725':'元禎',
'1726':'永記',
'1727':'中華化',
'1729':'必翔',
'1730':'花仙子',
'1731':'美吾華',
'1732':'毛寶',
'1733':'五鼎',
'1734':'杏輝',
'1735':'日勝化',
'1736':'喬山',
'1737':'臺鹽',
'1773':'勝一',
'1802':'台玻',
'1805':'寶徠',
'1806':'冠軍',
'1808':'國賓大',
'1809':'中釉',
'1810':'和成',
'1902':'台紙',
'1903':'士紙',
'1904':'正隆',
'1905':'華紙',
'1906':'寶隆',
'1907':'永豐餘',
'1909':'榮成',
'2002':'中鋼',
'2006':'東鋼',
'2007':'燁興',
'2008':'高興昌',
'2009':'第一銅',
'2010':'春源',
'2012':'春雨',
'2013':'中鋼構',
'2014':'中鴻',
'2015':'豐興',
'2017':'官田鋼',
'2020':'美亞',
'2022':'聚亨',
'2023':'燁輝',
'2024':'志聯',
'2025':'千興',
'2027':'大成鋼',
'2028':'威致',
'2029':'盛餘',
'2030':'彰源',
'2031':'新光鋼',
'2032':'新鋼',
'2033':'佳大',
'2034':'允強',
'2038':'海光',
'2049':'上銀',
'2059':'川湖',
'2062':'橋椿',
'2101':'南港',
'2102':'泰豐',
'2103':'台橡',
'2104':'中橡',
'2105':'正新',
'2106':'建大',
'2107':'厚生',
'2108':'南帝',
'2109':'華豐',
'2201':'裕隆',
'2204':'中華',
'2206':'三陽',
'2207':'和泰車',
'2208':'台船',
'2227':'裕日車',
'2301':'光寶科',
'2302':'麗正',
'2303':'聯電',
'2305':'全友',
'2308':'台達電',
'2311':'日月光',
'2312':'金寶',
'2313':'華通',
'2314':'台揚',
'2315':'神達',
'2316':'楠梓電',
'2317':'鴻海',
'2321':'東訊',
'2323':'中環',
'2324':'仁寶',
'2325':'矽品',
'2327':'國巨',
'2328':'廣宇',
'2329':'華泰',
'2330':'台積電',
'2331':'精英',
'2332':'友訊',
'2337':'旺宏',
'2338':'光罩',
'2340':'光磊',
'2342':'茂矽',
'2344':'華邦電',
'2345':'智邦',
'2347':'聯強',
'2348':'力廣',
'2349':'錸德',
'2351':'順德',
'2352':'佳世達',
'2353':'宏碁',
'2354':'鴻準',
'2355':'敬鵬',
'2356':'英業達',
'2357':'華碩',
'2358':'美格',
'2359':'所羅門',
'2360':'致茂',
'2361':'鴻友',
'2362':'藍天',
'2363':'矽統',
'2364':'倫飛',
'2365':'昆盈',
'2367':'燿華',
'2368':'金像電',
'2369':'菱生',
'2371':'大同',
'2373':'震旦行',
'2374':'佳能',
'2375':'智寶',
'2376':'技嘉',
'2377':'微星',
'2379':'瑞昱',
'2380':'虹光',
'2382':'廣達',
'2383':'台光電',
'2384':'勝華',
'2385':'群光',
'2387':'精元',
'2388':'威盛',
'2390':'云辰',
'2392':'正崴',
'2393':'億光',
'2395':'研華',
'2397':'友通',
'2399':'映泰',
'2401':'凌陽',
'2402':'毅嘉',
'2403':'友尚',
'2404':'漢唐',
'2405':'浩鑫',
'2406':'國碩',
'2408':'南科',
'2409':'友達',
'2412':'中華電',
'2413':'環科',
'2414':'精技',
'2415':'錩新',
'2417':'圓剛',
'2419':'仲琦',
'2420':'新巨',
'2421':'建準',
'2423':'固緯',
'2424':'隴華',
'2425':'承啟',
'2426':'鼎元',
'2427':'三商電',
'2428':'興勤',
'2429':'永兆',
'2430':'燦坤',
'2431':'聯昌',
'2433':'互盛電',
'2434':'統懋',
'2436':'偉詮電',
'2437':'旺詮',
'2438':'英誌',
'2439':'美律',
'2440':'太空梭',
'2441':'超豐',
'2442':'美齊',
'2443':'新利虹',
'2444':'友旺',
'2448':'晶電',
'2449':'京元電',
'2450':'神腦',
'2451':'創見',
'2453':'凌群',
'2454':'聯發科',
'2455':'全新',
'2456':'奇力新',
'2457':'飛宏',
'2458':'義隆',
'2459':'敦吉',
'2460':'建通',
'2461':'光群雷',
'2462':'良得電',
'2463':'研揚',
'2464':'盟立',
'2465':'麗臺',
'2466':'冠西電',
'2467':'志聖',
'2468':'華經',
'2471':'資通',
'2472':'立隆電',
'2473':'思源',
'2474':'可成',
'2475':'華映',
'2476':'鉅祥',
'2477':'美隆電',
'2478':'大毅',
'2480':'敦陽科',
'2481':'強茂',
'2482':'連宇',
'2483':'百容',
'2484':'希華',
'2485':'兆赫',
'2486':'一詮',
'2488':'漢平',
'2489':'瑞軒',
'2491':'吉祥全',
'2492':'華新科',
'2493':'揚博',
'2495':'普安',
'2496':'卓越',
'2497':'怡利電',
'2498':'宏達電',
'2499':'東貝',
'2501':'國建',
'2504':'國產',
'2505':'國揚',
'2506':'太設',
'2509':'全坤建',
'2511':'太子',
'2514':'龍邦',
'2515':'中工',
'2516':'新建',
'2520':'冠德',
'2524':'京城',
'2527':'宏璟',
'2528':'皇普',
'2530':'華建',
'2534':'宏盛',
'2535':'達欣工',
'2536':'宏普',
'2537':'聯上發',
'2538':'基泰',
'2539':'櫻花建',
'2540':'金尚昌',
'2542':'興富發',
'2543':'皇昌',
'2545':'皇翔',
'2546':'根基',
'2547':'日勝生',
'2548':'華固',
'2597':'潤弘',
'2601':'益航',
'2603':'長榮',
'2605':'新興',
'2606':'裕民',
'2607':'榮運',
'2608':'大榮',
'2609':'陽明',
'2610':'華航',
'2611':'志信',
'2612':'中航',
'2613':'中櫃',
'2614':'東森',
'2615':'萬海',
'2616':'山隆',
'2617':'台航',
'2618':'長榮航',
'2701':'萬企',
'2702':'華園',
'2704':'國賓',
'2705':'六福',
'2706':'第一店',
'2707':'晶華',
'2801':'彰銀',
'2809':'京城銀',
'2812':'台中銀',
'2816':'旺旺保',
'2820':'華票',
'2823':'中壽',
'2832':'台產',
'2833':'台壽保',
'2834':'臺企銀',
'2836':'高雄銀',
'2837':'萬泰銀',
'2838':'聯邦銀',
'2841':'台開',
'2845':'遠東銀',
'2847':'大眾銀',
'2849':'安泰銀',
'2850':'新產',
'2851':'中再保',
'2852':'第一保',
'2854':'寶來證',
'2855':'統一證',
'2856':'元富證',
'2880':'華南金',
'2881':'富邦金',
'2882':'國泰金',
'2883':'開發金',
'2884':'玉山金',
'2885':'元大金',
'2886':'兆豐金',
'2887':'台新金',
'2888':'新光金',
'2889':'國票金',
'2890':'永豐金',
'2891':'中信金',
'2892':'第一金',
'2901':'欣欣',
'2903':'遠百',
'2904':'匯僑',
'2905':'三商行',
'2906':'高林',
'2908':'特力',
'2910':'統領',
'2911':'麗嬰房',
'2912':'統一超',
'2913':'農林',
'2915':'潤泰全',
'3002':'歐格',
'3003':'健和興',
'3004':'豐達科',
'3005':'神基',
'3006':'晶豪科',
'3008':'大立光',
'3010':'華立',
'3011':'今皓',
'3013':'晟銘電',
'3014':'聯陽',
'3015':'全漢',
'3016':'嘉晶',
'3017':'奇鋐',
'3018':'同開',
'3019':'亞光',
'3021':'衛展',
'3022':'威達電',
'3023':'信邦',
'3024':'憶聲',
'3025':'星通',
'3026':'禾伸堂',
'3027':'盛達',
'3028':'增你強',
'3029':'零壹',
'3030':'德律',
'3031':'佰鴻',
'3032':'偉訓',
'3033':'威健',
'3034':'聯詠',
'3035':'智原',
'3036':'文曄',
'3037':'欣興',
'3038':'全台',
'3040':'遠見',
'3041':'揚智',
'3042':'晶技',
'3043':'科風',
'3044':'健鼎',
'3045':'台灣大',
'3045R':'台灣甲',
'3045T':'台灣丙',
'3046':'建碁',
'3047':'訊舟',
'3048':'益登',
'3049':'和鑫',
'3050':'鈺德',
'3051':'力特',
'3052':'夆典',
'3054':'萬國',
'3055':'蔚華科',
'3056':'駿億',
'3057':'喬鼎',
'3058':'立德',
'3059':'華晶科',
'3060':'銘異',
'3061':'璨圓',
'3062':'建漢',
'3080':'威力盟',
'3090':'日電貿',
'3094':'聯傑',
'3130':'一零四',
'3164':'景岳',
'3189':'景碩',
'3209':'全科',
'3229':'晟鈦',
'3231':'緯創',
'3296':'勝德',
'3305':'昇貿',
'3308':'聯德',
'3311':'閎暉',
'3315':'宣昶',
'3356':'奇偶',
'3367':'英華達',
'3376':'新日興',
'3380':'明泰',
'3383':'新世紀',
'3406':'玉晶光',
'3419':'譁裕',
'3443':'創意',
'3450':'聯鈞',
'3474':'華亞科',
'3481':'奇美電',
'3494':'誠研',
'3501':'維熹',
'3504':'揚明光',
'3514':'昱晶',
'3515':'華擎',
'3518':'柏騰',
'3519':'綠能',
'3532':'台勝科',
'3533':'嘉澤',
'3534':'雷凌',
'3535':'晶彩科',
'3536':'誠創',
'3545':'旭曜',
'3550':'聯穎',
'3557':'嘉威',
'3559':'全智科',
'3561':'昇陽科',
'3573':'穎台',
'3576':'新日光',
'3579':'尚志',
'3584':'介面光電',
'3588':'通嘉',
'3593':'力銘',
'3596':'智易',
'3605':'宏致',
'3607':'谷崧',
'3617':'碩天',
'3622':'洋華',
'3638':'IML',
'3653':'健策',
'3673':'TPK',
'3686':'達能',
'3701':'大眾控',
'3702':'大聯大',
'3703':'欣陸',
'3704':'合勤控',
'4104':'佳醫',
'4106':'雃博',
'4108':'懷特',
'4119':'旭富',
'4133':'亞諾法',
'4306':'炎洲',
'4414':'如興',
'4526':'東台',
'4532':'瑞智',
'4725':'信昌化',
'4904':'遠傳',
'4906':'正文',
'4930':'燦星網',
'4938':'和碩',
'5203':'訊連',
'5305':'敦南',
'5388':'中磊',
'5434':'崇越',
'5469':'瀚宇博',
'5471':'松翰',
'5484':'慧友',
'5515':'建國',
'5522':'遠雄',
'5525':'順天',
'5531':'鄉林',
'5533':'皇鼎',
'5534':'長虹',
'5607':'遠雄港',
'5608':'四維航',
'5854':'合庫',
'6005':'群益證',
'6012':'金鼎證',
'6108':'競國',
'6112':'聚碩',
'6115':'鎰勝',
'6116':'彩晶',
'6117':'迎廣',
'6119':'大傳',
'6120':'輔祥',
'6128':'上福',
'6131':'悠克',
'6133':'金橋',
'6136':'富爾特',
'6139':'亞翔',
'6141':'柏承',
'6142':'友勁',
'6145':'勁永',
'6152':'百一',
'6153':'嘉聯益',
'6155':'鈞寶',
'6164':'華興',
'6165':'捷泰',
'6166':'凌華',
'6168':'宏齊',
'6172':'互億',
'6176':'瑞儀',
'6184':'大豐電',
'6189':'豐藝',
'6191':'精成科',
'6192':'巨路',
'6196':'帆宣',
'6197':'佳必琪',
'6201':'亞弘電',
'6202':'盛群',
'6205':'詮欣',
'6206':'飛捷',
'6209':'今國光',
'6213':'聯茂',
'6215':'和椿',
'6216':'居易',
'6224':'聚鼎',
'6225':'天瀚',
'6226':'光鼎',
'6230':'超眾',
'6235':'華孚',
'6239':'力成',
'6243':'迅杰',
'6251':'定穎',
'6257':'矽格',
'6269':'台郡',
'6271':'同欣電',
'6277':'宏正',
'6278':'台表科',
'6281':'全國電',
'6282':'康舒',
'6283':'淳安',
'6285':'啟碁',
'6286':'立錡',
'6289':'華上',
'6505':'台塑化',
'6605':'帝寶',
'8008':'建興電',
'8016':'矽創',
'8021':'尖點',
'8033':'雷虎',
'8039':'台虹',
'8046':'南電',
'8070':'長華',
'8072':'陞泰',
'8078':'華寶',
'8081':'致新',
'8101':'華冠',
'8103':'瀚荃',
'8105':'凌巨',
'8110':'華東',
'8112':'至上',
'8131':'福懋科',
'8163':'達方',
'8201':'無敵',
'8213':'志超',
'8249':'菱光',
'8261':'富鼎',
'8374':'羅昇',
'8926':'台汽電',
'8940':'新天地',
'9902':'台火',
'9904':'寶成',
'9905':'大華',
'9906':'興達',
'9907':'統一實',
'9908':'大台北',
'9910':'豐泰',
'9911':'櫻花',
'9912':'偉聯',
'9914':'美利達',
'9917':'中保',
'9918':'欣天然',
'9919':'康那香',
'9921':'巨大',
'9924':'福興',
'9925':'新保',
'9926':'新海',
'9927':'泰銘',
'9928':'中視',
'9929':'秋雨',
'9930':'中聯資',
'9931':'欣高',
'9933':'中鼎',
'9934':'成霖',
'9935':'慶豐富',
'9937':'全國',
'9938':'百和',
'9939':'宏全',
'9940':'信義',
'9941':'裕融',
'9942':'茂順',
'9943':'好樂迪',
'9944':'新麗',
'9945':'潤泰新',
'9955':'佳龍',
'9958':'世紀鋼'}
