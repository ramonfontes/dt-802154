# Real-to-Virtual Data Replay

This section describes the procedure used to execute the emulated network and replay real sensor data inside the Mininet-WiFi environment. The setup integrates virtual IEEE 802.15.4/6LoWPAN nodes with physical sensor devices, enabling direct comparison between real traffic and its replicated virtual counterpart.

## Running the emulated network

The emulated network is launched on the laptop using Mininet-WiFi extended with 802.15.4 and 6LoWPAN support. A physical sensor node is also attached to the laptop and bridged to the virtual topology.

```
sudo python topo.py
```

## Activating the Physical Device (Computer #1)

Each physical device uses the script `phy-only.py`. The script expects two arguments:

- Argument 1: IPv6 address (including prefix)
- Argument 2: Node ID

```
sudo python phy-only.py fe80::2/64 1
```

## Activating the Physical Device (Computer #2)


```
sudo python phy-only.py fe80::3/64 2
```


## Comparing PCAP Traces

To validate the replay accuracy, the captured physical traffic (phy.pcap) is compared against the virtual network traffic (e.g., sensor1.pcap).

Run the comparison tool:

```
python pcap_compare.py phy.pcap sensor1.pcap

[INFO] UDP packets with payload in phy.pcap: 114
[INFO] UDP packets with payload in sensor1.pcap: 114

======== SIMILARITY METRICS ========
Jaccard similarity:       100.00%
Same-size payload ratio:  100.00%
Identical payloads:       114
Unique in PCAP 1:         0
Unique in PCAP 2:         0

======== IDENTICAL UDP DATA ========
  HASH: 45b336a2392c28828d74aab2e60c5a8425f5cc28010355f8c5e584ef35145cbe   SIZE: 8 bytes
  HASH: 4beda276541aa3856108536eafa74b70f9cb141f239658ea63b903125c604063   SIZE: 8 bytes
  HASH: 7e95b8a2ad8cfb7fa408aa930c7c11a77a1e33cfeeb395466266282025042636   SIZE: 8 bytes
  HASH: 4e7b0e46eff81611704bb4ff80d8c7f9dee33952cf415ba4d0996ad30f62164f   SIZE: 8 bytes
  HASH: 1352ea2e94f4b8e3fbfee099124a2eb266427cfd098d42c5922ca179b4f46308   SIZE: 8 bytes
  HASH: 38a8b4b62286605994447fce1b521295cb2a74af94ef77cbb665b795374b2ec7   SIZE: 8 bytes
  HASH: 10f74529905905ba2a395ba922c966ba52d94efd33b59bfbcef6bbc66ec40db1   SIZE: 8 bytes
  HASH: 955db60f26cbaef76f13c75f90e217049d87320550f39624087e8597bda4ab16   SIZE: 8 bytes
  HASH: 80cbeefb8651fb195e73ae6c61ef21e07353607852c36e2047867b68f86c9238   SIZE: 8 bytes
  HASH: 1bbbf083aed3017b3e5f8fd1fb7edbde77ebb99c7ffd0d2061647b435f8eeb70   SIZE: 8 bytes
  HASH: df1d16aac23cc569fa3747a3847d0d77f15bca3aa252bdc92837df3e94c75e02   SIZE: 8 bytes
  HASH: a0b86384fcef3e29e835d90cc1ccacab86f4b85e6a68737be560b27a213c8222   SIZE: 8 bytes
  HASH: 4427c6094d38a48ae6aecef5020f81004f239e1cc3d2de1b4f5dd64df62175ee   SIZE: 8 bytes
  HASH: 2075f2ffa193caafbb3240af34d217f75e548cec97e71029a66433fd0497fef0   SIZE: 8 bytes
  HASH: fc8f5b936f1c1754632d161569c2bab089611f06826803213ad25e128f31b7ca   SIZE: 8 bytes
  HASH: effaf8e411c7971bc0c84be11e644b73030ea28354422a20ad5c23b244939d8c   SIZE: 8 bytes
  HASH: 74d13c1073b518bbc3ba2b0f158dc0f21b65c4d2439c8094e3948b80f2d8e01f   SIZE: 8 bytes
  HASH: bbea75487a63fc909ed6142564251c6a45f81ddf88c650e2a3db6e7e52e58137   SIZE: 8 bytes
  HASH: edc605d30ce21d9f40c91e942336dbb4a58a6f6ac984f9c5d34a4d68bb75039a   SIZE: 8 bytes
  HASH: 479f97e18611af44355c0e02b5c498c450e7a9d384f1d4e03593995b5dff70af   SIZE: 8 bytes
  HASH: f6aa8d5ef5fa237781da65891e7442db30820337c0b671497152f954ac1e2ab6   SIZE: 8 bytes
  HASH: 1d594849071132dd97ed1ad2e07cfebbd9dd42143dd2646a2d4fd7ddd66e3e62   SIZE: 8 bytes
  HASH: 3347c41f20a91149c14be4a1f019b7d51dd3d9180d23a396b93727329f23ab36   SIZE: 8 bytes
  HASH: 7667b07a9927bbf99b482439c26a757abe4dcdbf20f6be6d5d63e0b2be20b97f   SIZE: 8 bytes
  HASH: 1914356ad3478cd475fcae3b5e13d16ebd50aa262d0ac949b132d569fd5411d8   SIZE: 8 bytes
  HASH: 8774b5a60acd8a7786871b7f1a432c13cfdb8c936b056b19b29fbfd9258e31e6   SIZE: 8 bytes
  HASH: d5f8d82c361f447ebad08839a722d2250b52ebf755eaa1ba7dedf5749bfa5cd6   SIZE: 8 bytes
  HASH: d99cd09f75c5ee66fac31e7328f5344597d671a99d8b6c139d6505a43c605071   SIZE: 8 bytes
  HASH: cb0398bab03b1f019325eb67162291990833683e0290f64874dd0b125775902f   SIZE: 8 bytes
  HASH: ef3af6911c2c552748996850ad168b21c8fd0d01da4b1b89e60de8449fe315fb   SIZE: 8 bytes
  HASH: a54219b629be013fd2669e1cb3e7267cce7857e95344a614614dce0e44378083   SIZE: 8 bytes
  HASH: 6e95030bf7f35ad2bd084dea477662a01e725f59e5fb059805d9af36db56a996   SIZE: 8 bytes
  HASH: 29558ea1e0d58a9fd47d4b97a248bb16dba873b99f1421c43635b30a6d9667c7   SIZE: 8 bytes
  HASH: f9461dbf09e8ee597ca1ad8b85f494639cb08e2ad1ebc8e5ea98f81d47448574   SIZE: 8 bytes
  HASH: c0697734aba1073690d37ef9890c1f637715108130077394aa95f66f5a7888b9   SIZE: 8 bytes
  HASH: 6c72f6e82bdc59a4d11872daf5c60598e8655383cf0d2f3ee0d49113ba7669fc   SIZE: 8 bytes
  HASH: f00b7a2e785bfc60728e1e6f0a9b6c24c8a7645d94a829b03f61b47eb4a24a09   SIZE: 8 bytes
  HASH: 82e93d1755cf9c442150a79f98e383b48b42479dae358fb4d0c3a419794fe647   SIZE: 8 bytes
  HASH: cf054ec0122ef0c7db7d1453cd7da1fd849dec6d38ea36ad20defc0cb6a6b0e1   SIZE: 8 bytes
  HASH: f04f7fad298650535e54e510624d6b96ff86976827e3c66a7bd781a373e1edea   SIZE: 8 bytes
  HASH: 43a46114b976350ea732a436c9dc75b25f32d197584509c2826db4c0d8f7262c   SIZE: 8 bytes
  HASH: 5754c812cb581437431ebc2b611c52c1c3f4ace8c078a51541d92bd83e042465   SIZE: 8 bytes
  HASH: 4d2b47c97e740e6f9942c60322bb59b339c90283bf26f0297110a205e38ecb06   SIZE: 8 bytes
  HASH: 8c350bde567ccdceff96a12a6b1f7cf1ae31bb06242ea28c79ac7e6da01c994e   SIZE: 8 bytes
  HASH: c0da6f6f0de2dc5f0ec43110d793fb78a58a97123560e384fb14fcc1fe5543eb   SIZE: 8 bytes
  HASH: 2045ab7889e5fae92ebbac1d79703a328ec0bd8b7e7d8f6c5ecb94bf2ea177ec   SIZE: 8 bytes
  HASH: a60b74627684cd5ac9fce39dec1c89c3a7fa1b4d43e0be04d391501cd1406226   SIZE: 8 bytes
  HASH: 94d5d7641cdeb8f498f7c8a768dbb6fd0d37e8bba4caf6a45f2abdd24c60756b   SIZE: 8 bytes
  HASH: 0445a7e007f661379453ad02239cc8155e7b3371f6a70e0b1246b0b373a53ed0   SIZE: 8 bytes
  HASH: 1572029b40fe043bd7b216d609fd384765306f74b106b46605bd84d980543bcb   SIZE: 8 bytes
  HASH: e8fae2540d99dcdbeb356e3c6f2d323b76e32b6a493f82dc7656d201171efaea   SIZE: 8 bytes
  HASH: ea1371b404b82a9da46bf9899b149a51dc6d1d8f99f878f38ac0a8fb2c6f1849   SIZE: 8 bytes
  HASH: 45916620c8f88e9e40e11f17ae6749e768fead66d32a56f1752b4f72b03651c2   SIZE: 8 bytes
  HASH: 3c44a07f07e7a550a369cb8679202df7fb4c193793a09a295abf18aba210a3b4   SIZE: 8 bytes
  HASH: 993dac9ff531c838a7aa4b5597ecfc0730a0b44fe051062cd238467103dea955   SIZE: 8 bytes
  HASH: 359c7d0a0659c12c05d5fa51f2dc711695e2b0dcc164cf1b2729b785f29a715c   SIZE: 8 bytes
  HASH: 057e9283790a42447c772fe72668aee5a2792bca4f970d627ec8467565e680f9   SIZE: 8 bytes
  HASH: e12d780328a8f6f7253f54b2f460352298661b73741d47674c720fe6a0c3a6a4   SIZE: 8 bytes
  HASH: 8933c8fbc377ec33077742d964e9a9207837a0a976fa19089541de84b2233873   SIZE: 8 bytes
  HASH: 7e434736b01229d83c525712efe2f92eafe8956785574e4aba28c7482d30006b   SIZE: 8 bytes
  HASH: ed939aee63b51b5f4cd959ba5db36b195003f8ea262a5b61cd8fda6f5cb823ae   SIZE: 8 bytes
  HASH: 7874de89d4641e5e8a355297ca7dcb568598e9b78464005e9e9ef58bbac4cb9f   SIZE: 8 bytes
  HASH: 4ce61968570bc25fa64d95ad6b06105fe2479466c23be3062cbc4fe13f05f3e4   SIZE: 8 bytes
  HASH: 195116172cf6df5c8585327c1f6b4193662056acad94edbc01354d60d9f8fec0   SIZE: 8 bytes
  HASH: f649fd3d3ff08ffda0efe2e0b9622b686317067b48e006b100a2d25c2391f997   SIZE: 8 bytes
  HASH: 4b3f6bbb2a246d6b2d0ee832558a9e0a98bc41a26745d7aba575a61b8b9e7fea   SIZE: 8 bytes
  HASH: 2cf74c22854470899576864f6206a433dbe6faf0abb9693216ff843ae83bc46b   SIZE: 8 bytes
  HASH: c5b1191192d8619492267bdca292010b7fc4642f5e1e1d5091b9c4b7f2012e49   SIZE: 8 bytes
  HASH: 7d20f42f4122d17df8e1c7b8709cb578f533d0ade547d537cdc1fc76718d7168   SIZE: 8 bytes
  HASH: 7c058ea414adbdd3a80dbad037ea51c70604f682c1f980ced87f13eb29a83ad9   SIZE: 8 bytes
  HASH: f3a95f212af3b51d39d77aef7f12ad8f35aadcdcf8863a6686e6527601c5856d   SIZE: 8 bytes
  HASH: 90b3d3d81037cb8b73a072396c4ba9cb0abc741018afe2b0b9141d215c739fa5   SIZE: 8 bytes
  HASH: 05ad0ae8fc95ff6557f775eb920d5bb682abd0d032eaca2c96ec72c68154adef   SIZE: 8 bytes
  HASH: ad7c1c457d8fcfb1783f572467056d9b102eb3cd77288df6fc1560778bb8d415   SIZE: 8 bytes
  HASH: 0746c3d089b4db4d65d1853bc820bb8ec731b50d9f7ff6eb54b184413d0bedff   SIZE: 8 bytes
  HASH: 375b14b49581eb9b1b9c22b7697133ce892e06944c4b5fe6120a0d2c30321335   SIZE: 8 bytes
  HASH: f4ddb669e91718a3b5fb7110af4c341f66e2e029cfd9ac4853f4c656f899f59c   SIZE: 8 bytes
  HASH: 3d477ee07afb1bf87af957f7ba96d3848f9a2ca7f42f8d7fe3f2d46f805622fe   SIZE: 8 bytes
  HASH: 59da1a615e4c69f220f44292bc58afc38ff69d22bdb66873d1ad87c5a898004b   SIZE: 8 bytes
  HASH: 98ffcc16b2b8833aab99b0d2a1c4dd9dbe330605108cf02d56a634e68b2a9edb   SIZE: 8 bytes
  HASH: 6111deb98b78f929ee20463576b4de2ad5c5c7d684073fcce14703a56d45c06a   SIZE: 8 bytes
  HASH: ec48fae12f9a63cdef4f3a0649e015d8f8eeb18175327cfef8a79bfd10995a30   SIZE: 8 bytes
  HASH: c017b64de839fa17e2070094f0b025e17a5628bf7614f12b4e37b395398e0f42   SIZE: 8 bytes
  HASH: 52d958bef6359b5c5db03ed33ecb4cb6b3ad2da7323c9a7bfb3c7371763e7ac0   SIZE: 8 bytes
  HASH: fcd248e40bf6ec534627a1c006121d1130c78da0ae8cc71478d61708729cde9c   SIZE: 8 bytes
  HASH: a49defdcb912b7a76475f846192046d49df1c45c98fbab18b86af52fae4fb00a   SIZE: 8 bytes
  HASH: 96fb79bc6db0c09fbee8f6bcf147a01e1127ba9b22e987028c174005fe5d4544   SIZE: 8 bytes
  HASH: f5990e67cc5e32925579726432aab2ae8e96338812c35be7ec8054998d659650   SIZE: 8 bytes
  HASH: 41aa8ab953bbe83f89acd196872a056f78bf6d57f63e1fd8adfe9587e587d4c8   SIZE: 8 bytes
  HASH: 83fa52688c4f2af964ee0bad5acaddf4dcb4a091813fce68504aa68c6576fad9   SIZE: 8 bytes
  HASH: a520ad6dbf9b45c7fd52d5b53a2e6d327ac8f848e974549abe2367eb2ecb920b   SIZE: 8 bytes
  HASH: b74ca220249914632da09d81e1a412898e251b51b2262ecb299ddda2908343cd   SIZE: 8 bytes
  HASH: 9c85cbdae490f349db241a2131548709f0a44771afed95ad20e6d21548895552   SIZE: 8 bytes
  HASH: 5c145d0eb4cd33bdd956f34846319c1b54e1ed850b6d52c6d9af3d333043fbb6   SIZE: 8 bytes
  HASH: 365d2da51d15b5d26a7311c1e80efe23ce2c44f566a93ac54a8ea59bdecfd2c9   SIZE: 8 bytes
  HASH: 8f6b8f68dff01988f09ebe421ca85e59ecf8e35ab69e7fc0dbf63528a269a811   SIZE: 8 bytes
  HASH: 45743e17990a25d8e7f4199cedb5b2808e30f772a0b26ed3a3a238cd48755527   SIZE: 8 bytes
  HASH: f3deb204f3dbb19fbb931f057c3725f8329d05f844ed1255dec398a56dae4474   SIZE: 8 bytes
  HASH: 759495688c22bf769d0e1dfacd6d0f20a17f8312ab9565905be415ffa4f8f70a   SIZE: 8 bytes
  HASH: 1d2d0df8eac830d458b077dc6133f4cf7f88f209f6e469183691d7d63cc6a653   SIZE: 8 bytes
  HASH: f6ecb5df7eeca83e69f9365d8766275095d81d1d39fe8da0a5d1a4f0719e8bfa   SIZE: 8 bytes
  HASH: 50f50ed34d58afd94562bde1a0ce724dea35c04becf8862378956e95b54d1ea4   SIZE: 8 bytes
  HASH: 339d5da576d0a79f66aa688cd40335cccd9f193a8daa6a45e2bcb3f2f969ddf3   SIZE: 8 bytes
  HASH: d7f479b165ffc09cb4d3d15b2b3db57b0090490c04b0d2b40934934a8537a123   SIZE: 8 bytes
  HASH: 3e05a7288ba3416d36690baf8c069040e1004b8c7d0bbb08d2cb1df9ae878e16   SIZE: 8 bytes
  HASH: cae2f46c2a27595532e1dda51d40f569316a21874dae77cf047e90407190c480   SIZE: 8 bytes
  HASH: 2f17d21f1fe13dc8f1405411a8b86eca427f8d8e72df2522a3cc295036f745e8   SIZE: 8 bytes
  HASH: 282b92cae6d5599ff9329e1ff35e88c30234ef4ff26790677d2bdf5514ba808e   SIZE: 8 bytes
  HASH: 2cacff5bbd9366e2fbe589365233b546cd760a9f15744a6e0ccf972fb2416660   SIZE: 8 bytes
  HASH: 1f8b408e52d4ee12253598878cf700e40729fd51f76143d5153d022d4683bb8d   SIZE: 8 bytes
  HASH: ad40dc8f24cdbcb567d164d5d1c7ec86239ccb21c1336baec58238b84061ca6f   SIZE: 8 bytes
  HASH: 53702c88f570ab57264bf0503b3fdeeb75eaeabbcc159d0a12be1f808593f93c   SIZE: 8 bytes
  HASH: 91f0d3f583b128d8105a01515a10eb4256792c5cef65b88439939771225d3c9d   SIZE: 8 bytes
  HASH: 12bd433ed826fda92d6cb027c5d4cd3572bbc61a158ad139abc2d5b489e4d68a   SIZE: 8 bytes

======== UNIQUE UDP DATA IN PCAP 1 ========

======== UNIQUE UDP DATA IN PCAP 2 ========

[OK] UDP-only data comparison finished.
```

This script analyzes only UDP payloads, computes similarity metrics, and identifies matching and non-matching packets between the real and virtual traces.